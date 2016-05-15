"""Functions that handle alignment, padding, widths, etc."""

import re
import unicodedata

RE_COLOR_ANSI = re.compile(r'(\033\[([\d;]+)m)')


def visible_width(string):
    """Get the visible width of a unicode string.

    Some CJK unicode characters are more than one byte unlike ASCII and latin unicode characters.

    From: https://github.com/Robpol86/terminaltables/pull/9

    :param str string: String to measure.

    :return: String's width.
    :rtype: int
    """
    if '\033' in string:
        string = RE_COLOR_ANSI.sub('', string)

    # Convert to unicode.
    try:
        decoded = string.decode('u8')
    except (AttributeError, UnicodeEncodeError):
        decoded = string

    width = 0
    for char in decoded:
        if unicodedata.east_asian_width(char) in ('F', 'W'):
            width += 2
        else:
            width += 1

    return width


def align_and_pad_cell(string, align, dimensions, padding, space=' '):
    """Align a string horizontally and vertically. Also add additional padding in both dimensions.

    :param str string: Input string to operate on.
    :param tuple align: Tuple that contains one of left/center/right and/or top/middle/bottom.
    :param tuple dimensions: Width and height ints to expand string to without padding.
    :param tuple padding: 4-int tuple. Number of space chars for left, right, top, and bottom.
    :param str space: Character to use as white space for resizing/padding (use single visible chars only).

    :return: Modified string.
    :rtype: str
    """
    # Handle trailing newlines or empty strings, str.splitlines() does not satisfy.
    lines = string.splitlines() or ['']
    if string.endswith('\n'):
        lines.append('')

    # Vertically align and pad.
    if 'bottom' in align:
        lines = ([''] * (dimensions[1] - len(lines) + padding[2])) + lines + ([''] * padding[3])
    elif 'middle' in align:
        delta = dimensions[1] - len(lines)
        lines = ([''] * (delta // 2 + delta % 2 + padding[2])) + lines + ([''] * (delta // 2 + padding[3]))
    else:
        lines = ([''] * padding[2]) + lines + ([''] * (dimensions[1] - len(lines) + padding[3]))

    # Horizontally align and pad.
    for i, line in enumerate(lines):
        new_width = dimensions[0] + len(line) - visible_width(line)
        if 'right' in align:
            lines[i] = line.rjust(padding[0] + new_width, space) + (space * padding[1])
        elif 'center' in align:
            lines[i] = (space * padding[0]) + line.center(new_width, space) + (space * padding[1])
        else:
            lines[i] = (space * padding[0]) + line.ljust(new_width + padding[1], space)

    return '\n'.join(lines)


def column_widths(table_data):
    """Get maximum widths of each column in the table.

    :param iter table_data: List of list of strings. The unpadded table data.

    :return: Column widths.
    :rtype: list
    """
    if not table_data:
        return list()

    number_of_columns = max(len(r) for r in table_data)
    widths = [0] * number_of_columns

    for row in table_data:
        for i in range(len(row)):
            if not row[i]:
                continue
            widths[i] = max(widths[i], visible_width(max(row[i].splitlines(), key=len)))

    return widths
