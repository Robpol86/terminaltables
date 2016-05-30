"""Additional simple tables defined here."""

from terminaltables.ascii_table import AsciiTable
from terminaltables.terminal_io import IS_WINDOWS


class UnixTable(AsciiTable):
    """Draw a table using box-drawing characters on Unix platforms. Table borders won't have any gaps between lines.

    Similar to the tables shown on PC BIOS boot messages, but not double-lined.
    """

    CHAR_F_INNER_HORIZONTAL = '\033(0\x71\033(B'
    CHAR_F_INNER_INTERSECT = '\033(0\x6e\033(B'
    CHAR_F_INNER_VERTICAL = '\033(0\x78\033(B'
    CHAR_F_OUTER_LEFT_INTERSECT = '\033(0\x74\033(B'
    CHAR_F_OUTER_LEFT_VERTICAL = '\033(0\x78\033(B'
    CHAR_F_OUTER_RIGHT_INTERSECT = '\033(0\x75\033(B'
    CHAR_F_OUTER_RIGHT_VERTICAL = '\033(0\x78\033(B'
    CHAR_H_INNER_HORIZONTAL = '\033(0\x71\033(B'
    CHAR_H_INNER_INTERSECT = '\033(0\x6e\033(B'
    CHAR_H_INNER_VERTICAL = '\033(0\x78\033(B'
    CHAR_H_OUTER_LEFT_INTERSECT = '\033(0\x74\033(B'
    CHAR_H_OUTER_LEFT_VERTICAL = '\033(0\x78\033(B'
    CHAR_H_OUTER_RIGHT_INTERSECT = '\033(0\x75\033(B'
    CHAR_H_OUTER_RIGHT_VERTICAL = '\033(0\x78\033(B'
    CHAR_INNER_HORIZONTAL = '\033(0\x71\033(B'
    CHAR_INNER_INTERSECT = '\033(0\x6e\033(B'
    CHAR_INNER_VERTICAL = '\033(0\x78\033(B'
    CHAR_OUTER_BOTTOM_HORIZONTAL = '\033(0\x71\033(B'
    CHAR_OUTER_BOTTOM_INTERSECT = '\033(0\x76\033(B'
    CHAR_OUTER_BOTTOM_LEFT = '\033(0\x6d\033(B'
    CHAR_OUTER_BOTTOM_RIGHT = '\033(0\x6a\033(B'
    CHAR_OUTER_LEFT_INTERSECT = '\033(0\x74\033(B'
    CHAR_OUTER_LEFT_VERTICAL = '\033(0\x78\033(B'
    CHAR_OUTER_RIGHT_INTERSECT = '\033(0\x75\033(B'
    CHAR_OUTER_RIGHT_VERTICAL = '\033(0\x78\033(B'
    CHAR_OUTER_TOP_HORIZONTAL = '\033(0\x71\033(B'
    CHAR_OUTER_TOP_INTERSECT = '\033(0\x77\033(B'
    CHAR_OUTER_TOP_LEFT = '\033(0\x6c\033(B'
    CHAR_OUTER_TOP_RIGHT = '\033(0\x6b\033(B'

    @property
    def table(self):
        """Return a large string of the entire table ready to be printed to the terminal."""
        ascii_table = super(UnixTable, self).table
        optimized = ascii_table.replace('\033(B\033(0', '')
        return optimized


class WindowsTable(AsciiTable):
    """Draw a table using box-drawing characters on Windows platforms. This uses Code Page 437. Single-line borders.

    From: http://en.wikipedia.org/wiki/Code_page_437#Characters
    """

    CHAR_F_INNER_HORIZONTAL = b'\xc4'.decode('ibm437')
    CHAR_F_INNER_INTERSECT = b'\xc5'.decode('ibm437')
    CHAR_F_INNER_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_F_OUTER_LEFT_INTERSECT = b'\xc3'.decode('ibm437')
    CHAR_F_OUTER_LEFT_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_F_OUTER_RIGHT_INTERSECT = b'\xb4'.decode('ibm437')
    CHAR_F_OUTER_RIGHT_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_H_INNER_HORIZONTAL = b'\xc4'.decode('ibm437')
    CHAR_H_INNER_INTERSECT = b'\xc5'.decode('ibm437')
    CHAR_H_INNER_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_H_OUTER_LEFT_INTERSECT = b'\xc3'.decode('ibm437')
    CHAR_H_OUTER_LEFT_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_H_OUTER_RIGHT_INTERSECT = b'\xb4'.decode('ibm437')
    CHAR_H_OUTER_RIGHT_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_INNER_HORIZONTAL = b'\xc4'.decode('ibm437')
    CHAR_INNER_INTERSECT = b'\xc5'.decode('ibm437')
    CHAR_INNER_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_OUTER_BOTTOM_HORIZONTAL = b'\xc4'.decode('ibm437')
    CHAR_OUTER_BOTTOM_INTERSECT = b'\xc1'.decode('ibm437')
    CHAR_OUTER_BOTTOM_LEFT = b'\xc0'.decode('ibm437')
    CHAR_OUTER_BOTTOM_RIGHT = b'\xd9'.decode('ibm437')
    CHAR_OUTER_LEFT_INTERSECT = b'\xc3'.decode('ibm437')
    CHAR_OUTER_LEFT_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_OUTER_RIGHT_INTERSECT = b'\xb4'.decode('ibm437')
    CHAR_OUTER_RIGHT_VERTICAL = b'\xb3'.decode('ibm437')
    CHAR_OUTER_TOP_HORIZONTAL = b'\xc4'.decode('ibm437')
    CHAR_OUTER_TOP_INTERSECT = b'\xc2'.decode('ibm437')
    CHAR_OUTER_TOP_LEFT = b'\xda'.decode('ibm437')
    CHAR_OUTER_TOP_RIGHT = b'\xbf'.decode('ibm437')


class WindowsTableDouble(AsciiTable):
    """Draw a table using box-drawing characters on Windows platforms. This uses Code Page 437. Double-line borders."""

    CHAR_F_INNER_HORIZONTAL = b'\xcd'.decode('ibm437')
    CHAR_F_INNER_INTERSECT = b'\xce'.decode('ibm437')
    CHAR_F_INNER_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_F_OUTER_LEFT_INTERSECT = b'\xcc'.decode('ibm437')
    CHAR_F_OUTER_LEFT_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_F_OUTER_RIGHT_INTERSECT = b'\xb9'.decode('ibm437')
    CHAR_F_OUTER_RIGHT_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_H_INNER_HORIZONTAL = b'\xcd'.decode('ibm437')
    CHAR_H_INNER_INTERSECT = b'\xce'.decode('ibm437')
    CHAR_H_INNER_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_H_OUTER_LEFT_INTERSECT = b'\xcc'.decode('ibm437')
    CHAR_H_OUTER_LEFT_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_H_OUTER_RIGHT_INTERSECT = b'\xb9'.decode('ibm437')
    CHAR_H_OUTER_RIGHT_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_INNER_HORIZONTAL = b'\xcd'.decode('ibm437')
    CHAR_INNER_INTERSECT = b'\xce'.decode('ibm437')
    CHAR_INNER_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_OUTER_BOTTOM_HORIZONTAL = b'\xcd'.decode('ibm437')
    CHAR_OUTER_BOTTOM_INTERSECT = b'\xca'.decode('ibm437')
    CHAR_OUTER_BOTTOM_LEFT = b'\xc8'.decode('ibm437')
    CHAR_OUTER_BOTTOM_RIGHT = b'\xbc'.decode('ibm437')
    CHAR_OUTER_LEFT_INTERSECT = b'\xcc'.decode('ibm437')
    CHAR_OUTER_LEFT_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_OUTER_RIGHT_INTERSECT = b'\xb9'.decode('ibm437')
    CHAR_OUTER_RIGHT_VERTICAL = b'\xba'.decode('ibm437')
    CHAR_OUTER_TOP_HORIZONTAL = b'\xcd'.decode('ibm437')
    CHAR_OUTER_TOP_INTERSECT = b'\xcb'.decode('ibm437')
    CHAR_OUTER_TOP_LEFT = b'\xc9'.decode('ibm437')
    CHAR_OUTER_TOP_RIGHT = b'\xbb'.decode('ibm437')


class SingleTable(WindowsTable if IS_WINDOWS else UnixTable):
    """Cross-platform table with single-line box-drawing characters."""

    pass


class DoubleTable(WindowsTableDouble):
    """Cross-platform table with box-drawing characters. On Windows it's double borders, on Linux/OSX it's unicode."""

    pass
