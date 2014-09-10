import fcntl
import struct
import sys
import termios

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '1.0.0'


def _align_and_pad(input_, align, width, height, lpad, rpad):
    """Aligns a string with center/rjust/ljust and adds additional padding.

    Positional arguments:
    input_ -- input string to operate on.
    align -- 'left', 'right', or 'center'.
    width -- align to this column width.
    height -- pad newlines and spaces to set cell to this height.
    lpad -- number of spaces to pad on the left.
    rpad -- number of spaces to pad on the right.

    Returns:
    Modified string.
    """
    # Handle trailing newlines or empty strings, str.splitlines() does not satisfy.
    lines = input_.splitlines() or ['']
    if input_.endswith('\n'):
        lines.append('')

    # Align.
    if align == 'center':
        aligned = '\n'.join(l.center(width) for l in lines)
    elif align == 'right':
        aligned = '\n'.join(l.rjust(width) for l in lines)
    else:
        aligned = '\n'.join(l.ljust(width) for l in lines)

    # Pad.
    padded = '\n'.join((' ' * lpad) + l + (' ' * rpad) for l in aligned.splitlines() or [''])

    # Increase height.
    additional_padding = height - 1 - padded.count('\n')
    if additional_padding > 0:
        padded += ('\n{0}'.format(' ' * (width + lpad + rpad))) * additional_padding

    return padded


def set_terminal_title(title):
    """Sets the terminal title.

    Positional arguments:
    title -- the title to set.
    """
    sys.stdout.write('\033]0;{0}\007'.format(title))


class AsciiTable(object):
    CHAR_CORNER_LOWER_LEFT = '+'
    CHAR_CORNER_LOWER_RIGHT = '+'
    CHAR_CORNER_UPPER_LEFT = '+'
    CHAR_CORNER_UPPER_RIGHT = '+'
    CHAR_HORIZONTAL = '-'
    CHAR_INTERSECT_BOTTOM = '-'
    CHAR_INTERSECT_CENTER = '+'
    CHAR_INTERSECT_LEFT = '|'
    CHAR_INTERSECT_RIGHT = '|'
    CHAR_INTERSECT_TOP = '-'
    CHAR_VERTICAL = '|'

    def __init__(self, table_data, title=None):
        self.table_data = table_data
        self.title = title

        self.inner_column_border = True
        self.inner_heading_row_border = True
        self.inner_row_border = True
        self.justify_columns = dict()  # {0: 'right', 1: 'left', 2: 'center'}
        self.outer_border = True
        self.padding_left = 1
        self.padding_right = 1

    def column_max_width(self, column_number):
        """Returns the maximum width of a column based on the current terminal width.

        Positional arguments:
        column_number -- the column number to query.

        Returns:
        The max width of the column (integer).
        """
        column_widths = self.column_widths
        borders_padding = (len(column_widths) * self.padding_left) + (len(column_widths) * self.padding_right)
        if self.outer_border:
            borders_padding += 2
        if self.inner_column_border:
            borders_padding += len(column_widths) - 1
        other_column_widths = sum(column_widths) - column_widths[column_number]
        return self.terminal_width - other_column_widths - borders_padding

    @property
    def column_widths(self):
        if not self.table_data:
            return list()

        number_of_columns = max(len(r) for r in self.table_data)
        widths = [0] * number_of_columns

        for row in self.table_data:
            for i in range(len(row)):
                if not row[i]:
                    continue
                widths[i] = max(widths[i], len(max(row[i].splitlines(), key=len)))

        return widths

    @property
    def padded_table_data(self):
        if not self.table_data:
            return list()

        # Set all rows to the same number of columns.
        max_columns = max(len(r) for r in self.table_data)
        new_table_data = [r + [''] * (max_columns - len(r)) for r in self.table_data]

        # Pad strings in each cell, and apply text-align/justification.
        column_widths = self.column_widths
        for row in new_table_data:
            height = max([c.count('\n') for c in row] or [0]) + 1
            for i in range(len(row)):
                align = self.justify_columns.get(i, 'left')
                cell = _align_and_pad(row[i], align, column_widths[i], height, self.padding_left, self.padding_right)
                row[i] = cell

        return new_table_data

    @property
    def table(self):
        padded_table_data = self.padded_table_data
        column_widths = [len(c) for c in padded_table_data[0]]
        borders_padding = (len(column_widths) * self.padding_left) + (len(column_widths) * self.padding_right)
        separator_cells = [(c + borders_padding) * self.CHAR_HORIZONTAL for c in column_widths]
        top_border, bottom_border, heading_border, row_border = list(), list(), list(), list()

        # Build internal table data (within outer borders).
        inner_column_border = '{l}{c}{r}'.format(c=(self.CHAR_VERTICAL if self.inner_column_border else ''),
                                                 l=(' ' * self.padding_left), r=(' ' * self.padding_right))
        table_data = [inner_column_border.join(r) for r in padded_table_data]

        # Build top and bottom borders.
        if self.outer_border:
            if self.title is not None and len(self.title) < sum([len(c) for c in separator_cells]):
                top_border = ['{0}{1}{2}'.format(
                    self.CHAR_CORNER_UPPER_LEFT,
                    self.title + self.CHAR_INTERSECT_TOP.join(separator_cells)[len(self.title):],
                    self.CHAR_CORNER_UPPER_RIGHT
                )]
            else:
                top_border = ['{0}{1}{2}'.format(self.CHAR_CORNER_UPPER_LEFT,
                                                 self.CHAR_INTERSECT_TOP.join(separator_cells),
                                                 self.CHAR_CORNER_UPPER_RIGHT)]
            bottom_border = ['{0}{1}{2}'.format(self.CHAR_CORNER_LOWER_LEFT,
                                                self.CHAR_INTERSECT_BOTTOM.join(separator_cells),
                                                self.CHAR_CORNER_LOWER_RIGHT)]

        # Build heading separator.
        if table_data and self.inner_heading_row_border:
            table_data.insert(1, ['{0}{1}{2}'.format(self.CHAR_INTERSECT_LEFT,
                                                     self.CHAR_INTERSECT_CENTER.join(separator_cells),
                                                     self.CHAR_INTERSECT_RIGHT)])

        raise NotImplementedError

    @property
    def terminal_height(self):
        return struct.unpack('hhhh', fcntl.ioctl(0, termios.TIOCGWINSZ, '\000' * 8))[0]

    @property
    def terminal_width(self):
        return struct.unpack('hhhh', fcntl.ioctl(0, termios.TIOCGWINSZ, '\000' * 8))[1]


class UnixTable(AsciiTable):
    CHAR_CORNER_LOWER_LEFT = '\033(0\x6d\033(B'
    CHAR_CORNER_LOWER_RIGHT = '\033(0\x6a\033(B'
    CHAR_CORNER_UPPER_LEFT = '\033(0\x6c\033(B'
    CHAR_CORNER_UPPER_RIGHT = '\033(0\x6b\033(B'
    CHAR_HORIZONTAL = '\033(0\x71\033(B'
    CHAR_INTERSECT_BOTTOM = '\033(0\x76\033(B'
    CHAR_INTERSECT_CENTER = '\033(0\x6e\033(B'
    CHAR_INTERSECT_LEFT = '\033(0\x74\033(B'
    CHAR_INTERSECT_RIGHT = '\033(0\x75\033(B'
    CHAR_INTERSECT_TOP = '\033(0\x77\033(B'
    CHAR_VERTICAL = '\033(0\x78\033(B'


class DosSingleTable(AsciiTable):
    pass


class DosDoubleTable(AsciiTable):
    pass


class UnicodeSingleTable(AsciiTable):
    pass


class UnicodeDoubleTable(AsciiTable):
    pass
