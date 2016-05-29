"""User-facing tables defined here."""

import os

from terminaltables.base_table import BaseTable
from terminaltables.build import combine


class AsciiTable(BaseTable):
    """Draw a table using regular ASCII characters, such as `+`, `|`, and `-`."""

    pass


class UnixTable(BaseTable):
    """Draw a table using box-drawing characters on Unix platforms. Table borders won't have any gaps between lines.

    Similar to the tables shown on PC BIOS boot messages, but not double-lined.
    """

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

    @property
    def table(self):
        """Return a large string of the entire table ready to be printed to the terminal."""
        ascii_table = super(UnixTable, self).table
        optimized = ascii_table.replace('\033(B\033(0', '')
        return optimized


class WindowsTable(BaseTable):
    """Draw a table using box-drawing characters on Windows platforms. This uses Code Page 437. Single-line borders.

    From: http://en.wikipedia.org/wiki/Code_page_437#Characters
    """

    CHAR_CORNER_LOWER_LEFT = b'\xc0'.decode('ibm437')
    CHAR_CORNER_LOWER_RIGHT = b'\xd9'.decode('ibm437')
    CHAR_CORNER_UPPER_LEFT = b'\xda'.decode('ibm437')
    CHAR_CORNER_UPPER_RIGHT = b'\xbf'.decode('ibm437')
    CHAR_HORIZONTAL = b'\xc4'.decode('ibm437')
    CHAR_INTERSECT_BOTTOM = b'\xc1'.decode('ibm437')
    CHAR_INTERSECT_CENTER = b'\xc5'.decode('ibm437')
    CHAR_INTERSECT_LEFT = b'\xc3'.decode('ibm437')
    CHAR_INTERSECT_RIGHT = b'\xb4'.decode('ibm437')
    CHAR_INTERSECT_TOP = b'\xc2'.decode('ibm437')
    CHAR_VERTICAL = b'\xb3'.decode('ibm437')


class WindowsTableDouble(BaseTable):
    """Draw a table using box-drawing characters on Windows platforms. This uses Code Page 437. Double-line borders."""

    CHAR_CORNER_LOWER_LEFT = b'\xc8'.decode('ibm437')
    CHAR_CORNER_LOWER_RIGHT = b'\xbc'.decode('ibm437')
    CHAR_CORNER_UPPER_LEFT = b'\xc9'.decode('ibm437')
    CHAR_CORNER_UPPER_RIGHT = b'\xbb'.decode('ibm437')
    CHAR_HORIZONTAL = b'\xcd'.decode('ibm437')
    CHAR_INTERSECT_BOTTOM = b'\xca'.decode('ibm437')
    CHAR_INTERSECT_CENTER = b'\xce'.decode('ibm437')
    CHAR_INTERSECT_LEFT = b'\xcc'.decode('ibm437')
    CHAR_INTERSECT_RIGHT = b'\xb9'.decode('ibm437')
    CHAR_INTERSECT_TOP = b'\xcb'.decode('ibm437')
    CHAR_VERTICAL = b'\xba'.decode('ibm437')


class SingleTable(WindowsTable if os.name == 'nt' else UnixTable):
    """Cross-platform table with single-line box-drawing characters."""

    pass


class DoubleTable(WindowsTableDouble):
    """Cross-platform table with box-drawing characters. On Windows it's double borders, on Linux/OSX it's unicode."""

    pass


class GithubFlavoredMarkdownTable(BaseTable):
    """Github flavored markdown table.

    https://help.github.com/articles/github-flavored-markdown/#tables
    """

    CHAR_HORIZONTAL = '-'

    def __init__(self, table_data):
        """Constructor.

        :param iter table_data: List (empty or list of lists of strings) representing the table.
        """
        # Github flavored markdown table won't support title.
        super(GithubFlavoredMarkdownTable, self).__init__(table_data)

    def horizontal_border(self, _, outer_widths):
        """Handle the GitHub header border.

        E.g.:
        |:---|:---:|---:|----|

        :param _: Unused.
        :param iter outer_widths: List of widths (with padding) for each column.

        :return: Prepared border strings in a generator.
        :rtype: iter
        """
        columns = list()
        for i, width in enumerate(outer_widths):
            justify = self.justify_columns.get(i)
            width = max(3, width)  # Width should be at least 3 so justification can be applied.
            if justify == 'left':
                columns.append(':' + self.CHAR_HORIZONTAL * (width - 1))
            elif justify == 'right':
                columns.append(self.CHAR_HORIZONTAL * (width - 1) + ':')
            elif justify == 'center':
                columns.append(':' + self.CHAR_HORIZONTAL * (width - 2) + ':')
            else:
                columns.append(self.CHAR_HORIZONTAL * width)

        return combine(columns, self.CHAR_VERTICAL, self.CHAR_VERTICAL, self.CHAR_VERTICAL)

    def gen_table(self, inner_widths, inner_heights, outer_widths):
        """Combine everything and yield every line of the entire table with borders.

        :param iter inner_widths: List of widths (no padding) for each column.
        :param iter inner_heights: List of heights (no padding) for each row.
        :param iter outer_widths: List of widths (with padding) for each column.
        :return:
        """
        for i, row in enumerate(self.table_data):
            # Yield the row line by line (e.g. multi-line rows).
            for line in self.gen_row_lines(row, inner_widths, inner_heights[i]):
                yield line
            # Yield header separator.
            if i == 0:
                yield self.horizontal_border(None, outer_widths)
