"""Main table class."""

from terminaltables import width_and_alignment
from terminaltables.build import build_border, build_row
from terminaltables.terminal_io import terminal_size


def join_row(row, left, middle, right):
    """Convert a row (list of strings) into a joined string with left and right borders. Supports multi-lines.

    :param iter row: List of strings representing one row.
    :param str left: Left border.
    :param str middle: Column separator.
    :param str right: Right border.

    :return: String representation of a row.
    :rtype: str
    """
    if not row:
        return left + right

    if not any('\n' in c for c in row):
        return left + middle.join(row) + right

    # Split cells in the row by newlines. This creates new rows.
    split_cells = [(c.splitlines() or ['']) + ([''] if c.endswith('\n') else []) for c in row]
    height = len(split_cells[0])

    # Merge rows into strings.
    converted_rows = list()
    for row_number in range(height):
        converted_rows.append(left + middle.join([c[row_number] for c in split_cells]) + right)
    return '\n'.join(converted_rows)


class BaseTable(object):
    """Base table class."""

    CHAR_CORNER_LOWER_LEFT = '+'
    CHAR_CORNER_LOWER_RIGHT = '+'
    CHAR_CORNER_UPPER_LEFT = '+'
    CHAR_CORNER_UPPER_RIGHT = '+'
    CHAR_HORIZONTAL = '-'
    CHAR_INTERSECT_BOTTOM = '+'
    CHAR_INTERSECT_CENTER = '+'
    CHAR_INTERSECT_LEFT = '+'
    CHAR_INTERSECT_RIGHT = '+'
    CHAR_INTERSECT_TOP = '+'
    CHAR_VERTICAL = '|'

    def __init__(self, table_data, title=None):
        """Constructor.

        :param iter table_data: List (empty or list of lists of strings) representing the table.
        :param str title: Optional title to show within the top border of the table.
        """
        self.table_data = table_data
        self.title = title

        self.inner_column_border = True
        self.inner_heading_row_border = True
        self.inner_footing_row_border = False
        self.inner_row_border = False
        self.justify_columns = dict()  # {0: 'right', 1: 'left', 2: 'center'}
        self.outer_border = True
        self.padding_left = 1
        self.padding_right = 1

    def gen_cell_lines(self, row, widths, height):
        r"""Combine cells in row and group them into lines with borders.

        Caller is expected to pass yielded lines to ''.join() to combine them into a printable line. Caller must append
        newline character to the end of joined line.

        In:
        ['Row One Column One', 'Two', 'Three']
        Out:
        [
            ('|', ' Row One Column One ', '|', ' Two ', '|', ' Three ', '|'),
        ]

        In:
        ['Row One\nColumn One', 'Two', 'Three'],
        Out:
        [
            ('|', ' Row One    ', '|', ' Two ', '|', ' Three ', '|'),
            ('|', ' Column One ', '|', '     ', '|', '       ', '|'),
        ]

        :param iter row: One row in the table. List of cells.
        :param iter widths: List of inner widths (no padding) for each column.
        :param int height: Inner height (no padding) (number of lines) to expand row to.

        :return: Yields lines split into components in a list. Caller must ''.join() line.
        """
        cells_in_row = list()

        # Resize row if it doesn't have enough cells.
        if len(row) != len(widths):
            row = row + [''] * (len(widths) - len(row))

        # Pad and align each cell. Split each cell into lines to support multi-line cells.
        for i, cell in enumerate(row):
            align = (self.justify_columns.get(i),)
            inner_dimensions = (widths[i], height)
            padding = (self.padding_left, self.padding_right, 0, 0)
            cells_in_row.append(width_and_alignment.align_and_pad_cell(cell, align, inner_dimensions, padding))

        # Combine cells and borders.
        lines = build_row(
            cells_in_row,
            self.CHAR_VERTICAL if self.outer_border else '',
            self.CHAR_VERTICAL if self.inner_column_border else '',
            self.CHAR_VERTICAL if self.outer_border else ''
        )

        # Yield each line.
        for line in lines:
            yield line

    def column_max_width(self, column_number):
        """Return the maximum width of a column based on the current terminal width.

        :param int column_number: The column number to query.

        :return: The max width of the column.
        :rtype: int
        """
        outer_border = 2 if self.outer_border else 0
        inner_border = 1 if self.inner_column_border else 0
        padding = self.padding_left + self.padding_right
        return width_and_alignment.column_max_width(self.table_data, column_number, outer_border, inner_border, padding)

    @property
    def column_widths(self):
        """Return a list of integers representing the widths of each table column without padding."""
        if not self.table_data:
            return list()
        return width_and_alignment.max_dimensions(self.table_data)[0]

    @property
    def ok(self):  # Too late to change API. # pylint: disable=invalid-name
        """Return True if the table fits within the terminal width, False if the table breaks."""
        return self.table_width <= terminal_size()[0]

    @property
    def padded_table_data(self):
        """Return a list of lists of strings. It's self.table_data but with the cells padded with spaces and newlines.

        Most of the work in this class is done here.
        """
        if not self.table_data:
            return list()

        # Set all rows to the same number of columns.
        max_columns = max(len(r) for r in self.table_data)
        new_table_data = [r + [''] * (max_columns - len(r)) for r in self.table_data]

        # Pad strings in each cell, and apply text-align/justification.
        widths = self.column_widths
        for row in new_table_data:
            height = max([c.count('\n') for c in row] or [0]) + 1
            for i in range(len(row)):
                align = (self.justify_columns.get(i, 'left'),)
                dimensions = (widths[i], height)
                padding = (self.padding_left, self.padding_right, 0, 0)
                cell = '\n'.join(width_and_alignment.align_and_pad_cell(row[i], align, dimensions, padding))
                row[i] = cell

        return new_table_data

    @property
    def table(self):
        """Return a large string of the entire table ready to be printed to the terminal."""
        widths = [c + self.padding_left + self.padding_right for c in self.column_widths]
        inner_widths, inner_heights = width_and_alignment.max_dimensions(self.table_data)
        final_table_data = list()

        # Append top border.
        if self.outer_border:
            final_table_data.append(''.join(build_border(
                widths,
                self.CHAR_HORIZONTAL,
                self.CHAR_CORNER_UPPER_LEFT,
                self.CHAR_INTERSECT_TOP if self.inner_column_border else '',
                self.CHAR_CORNER_UPPER_RIGHT,
                self.title
            )))

        # Build table body.
        indexes = range(len(self.table_data))
        for i in indexes:
            for line in self.gen_cell_lines(self.table_data[i], inner_widths, inner_heights[i]):
                final_table_data.append(''.join(line))

            # Insert row separator.
            if i == indexes[-1]:
                continue  # Last row.
            if self.inner_row_border or (self.inner_heading_row_border and i == 0):
                final_table_data.append(''.join(build_border(
                    widths,
                    self.CHAR_HORIZONTAL,
                    self.CHAR_INTERSECT_LEFT if self.outer_border else '',
                    self.CHAR_INTERSECT_CENTER if self.inner_column_border else '',
                    self.CHAR_INTERSECT_RIGHT if self.outer_border else ''
                )))

            if i == indexes[-2] and self.inner_footing_row_border:
                final_table_data.append(''.join(build_border(
                    widths,
                    self.CHAR_HORIZONTAL,
                    self.CHAR_INTERSECT_LEFT if self.outer_border else '',
                    self.CHAR_INTERSECT_CENTER if self.inner_column_border else '',
                    self.CHAR_INTERSECT_RIGHT if self.outer_border else ''
                )))

        # Append bottom border.
        if self.outer_border:
            final_table_data.append(''.join(build_border(
                widths,
                self.CHAR_HORIZONTAL,
                self.CHAR_CORNER_LOWER_LEFT,
                self.CHAR_INTERSECT_BOTTOM if self.inner_column_border else '',
                self.CHAR_CORNER_LOWER_RIGHT
            )))

        return '\n'.join(final_table_data)

    @property
    def table_width(self):
        """Return the width of the table including padding and borders."""
        outer_border = 2 if self.outer_border else 0
        inner_border = 1 if self.inner_column_border else 0
        padding = self.padding_left + self.padding_right
        return width_and_alignment.table_width(self.table_data, outer_border, inner_border, padding)
