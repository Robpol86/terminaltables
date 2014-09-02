import fcntl
import struct
import sys
import termios


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

        self.first_row_heading = False
        self.justify_right = False
        self.no_inner_border = False
        self.no_outer_border = False
        self.partial_border = False
        self.padding_bottom = 0
        self.padding_left = 1
        self.padding_right = 1
        self.padding_top = 0

    @property
    def column_widths(self):
        padded_table_data = self.padded_table_data
        if not padded_table_data:
            return []
        return [len(c) for c in padded_table_data[0]]

    @property
    def padded_table_data(self):
        if not self.table_data:
            return []
        max_columns = max(len(r) for r in self.table_data)
        new_table_data = [r + [''] * (max_columns - len(r)) for r in self.table_data]
        return new_table_data

    @property
    def terminal_height(self):
        return struct.unpack('hh',  fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ, '1234'))[0]

    @property
    def terminal_width(self):
        return struct.unpack('hh',  fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ, '1234'))[1]


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
