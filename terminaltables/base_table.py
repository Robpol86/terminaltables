"""Main table class."""

from terminaltables import width_and_alignment
from terminaltables.build import build_border, build_row, flatten
from terminaltables.terminal_io import terminal_size


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

    def horizontal_border(self, style, outer_widths):
        """Build any kind of horizontal border for the table.

        :param str style: Type of border to return.
        :param iter outer_widths: List of widths (with padding) for each column.

        :return: Prepared border as a tuple of strings.
        :rtype: tuple
        """
        if style == 'top':
            left = self.CHAR_CORNER_UPPER_LEFT
            center = self.CHAR_INTERSECT_TOP if self.inner_column_border else ''
            right = self.CHAR_CORNER_UPPER_RIGHT
            title = self.title
        elif style == 'bottom':
            left = self.CHAR_CORNER_LOWER_LEFT
            center = self.CHAR_INTERSECT_BOTTOM if self.inner_column_border else ''
            right = self.CHAR_CORNER_LOWER_RIGHT
            title = None
        else:
            left = self.CHAR_INTERSECT_LEFT if self.outer_border else ''
            center = self.CHAR_INTERSECT_CENTER if self.inner_column_border else ''
            right = self.CHAR_INTERSECT_RIGHT if self.outer_border else ''
            title = None
        return build_border(outer_widths, self.CHAR_HORIZONTAL, left, center, right, title)

    def gen_row_lines(self, row, inner_widths, height):
        r"""Combine cells in row and group them into lines with vertical borders.

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
        :param iter inner_widths: List of widths (no padding) for each column.
        :param int height: Inner height (no padding) (number of lines) to expand row to.

        :return: Yields lines split into components in a list. Caller must ''.join() line.
        """
        cells_in_row = list()

        # Resize row if it doesn't have enough cells.
        if len(row) != len(inner_widths):
            row = row + [''] * (len(inner_widths) - len(row))

        # Pad and align each cell. Split each cell into lines to support multi-line cells.
        for i, cell in enumerate(row):
            align = (self.justify_columns.get(i),)
            inner_dimensions = (inner_widths[i], height)
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

    def gen_table(self, inner_widths, inner_heights, outer_widths):
        """Combine everything and yield every line of the entire table with borders.

        :param iter inner_widths: List of widths (no padding) for each column.
        :param iter inner_heights: List of heights (no padding) for each row.
        :param iter outer_widths: List of widths (with padding) for each column.
        :return:
        """
        # Yield top border.
        if self.outer_border:
            yield self.horizontal_border('top', outer_widths)

        # Yield table body.
        row_count = len(self.table_data)
        last_row_index, before_last_row_index = row_count - 1, row_count - 2
        for i, row in enumerate(self.table_data):
            # Yield the row line by line (e.g. multi-line rows).
            for line in self.gen_row_lines(row, inner_widths, inner_heights[i]):
                yield line
            # If this is the last row then break. No separator needed.
            if i == last_row_index:
                break
            # Yield header separator.
            if self.inner_heading_row_border and i == 0:
                yield self.horizontal_border('heading', outer_widths)
            # Yield footer separator.
            elif self.inner_footing_row_border and i == before_last_row_index:
                yield self.horizontal_border('footing', outer_widths)
            # Yield row separator.
            elif self.inner_row_border:
                yield self.horizontal_border('row', outer_widths)

        # Yield bottom border.
        if self.outer_border:
            yield self.horizontal_border('bottom', outer_widths)

    def column_max_width(self, column_number):
        """Return the maximum width of a column based on the current terminal width.

        :param int column_number: The column number to query.

        :return: The max width of the column.
        :rtype: int
        """
        inner_widths = width_and_alignment.max_dimensions(self.table_data)[0]
        outer_border = 2 if self.outer_border else 0
        inner_border = 1 if self.inner_column_border else 0
        padding = self.padding_left + self.padding_right
        return width_and_alignment.column_max_width(inner_widths, column_number, outer_border, inner_border, padding)

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
    def table(self):
        """Return a large string of the entire table ready to be printed to the terminal."""
        inner_widths, inner_heights, outer_widths = width_and_alignment.max_dimensions(
            self.table_data, self.padding_left, self.padding_right
        )[:3]
        return flatten(self.gen_table(inner_widths, inner_heights, outer_widths))

    @property
    def table_width(self):
        """Return the width of the table including padding and borders."""
        outer_widths = width_and_alignment.max_dimensions(self.table_data, self.padding_left, self.padding_right)[2]
        outer_border = 2 if self.outer_border else 0
        inner_border = 1 if self.inner_column_border else 0
        return width_and_alignment.table_width(outer_widths, outer_border, inner_border)
