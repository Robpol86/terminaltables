"""Functions that handle alignment, padding, widths, etc."""

import re
import unicodedata

from terminaltables.terminal_io import terminal_size

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

    :return: Padded cell split into lines.
    :rtype: list
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

    return lines


def max_dimensions(table_data):
    """Get maximum widths of each column and maximum height of each row.

    :param iter table_data: List of list of strings (unmodified table data).

    :return: 2-item tuple of n-item lists. Column widths and row heights.
    :rtype: tuple
    """
    widths = [0] * (max(len(r) for r in table_data) if table_data else 0)
    heights = [0] * len(table_data)

    for j, row in enumerate(table_data):
        for i, cell in enumerate(row):
            if not cell:
                continue
            heights[j] = max(heights[j], cell.count('\n') + 1)
            widths[i] = max(widths[i], *[visible_width(l) for l in cell.splitlines()])

    return widths, heights


def column_max_width(table_data, column_number, outer_border, inner_border, padding):
    """Determine the maximum width of a column based on the current terminal width.

    :param iter table_data: List of list of strings (unmodified table data).
    :param int column_number: The column number to query.
    :param int outer_border: Sum of left and right outer border visible widths.
    :param int inner_border: Visible width of the inner border character.
    :param int padding: Total padding per cell (left + right padding).

    :return: The maximum width the column can be without causing line wrapping.
    """
    column_widths = max_dimensions(table_data)[0]
    column_count = len(column_widths)
    terminal_width = terminal_size()[0]

    # Count how much space padding, outer, and inner borders take up.
    non_data_space = outer_border
    if column_count:
        non_data_space += inner_border * (column_count - 1)
        non_data_space += column_count * padding

    # Exclude selected column's width.
    data_space = sum(column_widths) - column_widths[column_number]

    return terminal_width - data_space - non_data_space


def table_width(table_data, outer_border, inner_border, padding):
    """Determine the width of the entire table including borders and padding.

    :param iter table_data: List of list of strings (unmodified table data).
    :param int outer_border: Sum of left and right outer border visible widths.
    :param int inner_border: Visible width of the inner border character.
    :param int padding: Total padding per cell (left + right padding).

    :return: The width of the table.
    :rtype: int
    """
    column_widths = max_dimensions(table_data)[0]
    column_count = len(column_widths)

    # Count how much space padding, outer, and inner borders take up.
    non_data_space = outer_border
    if column_count:
        non_data_space += inner_border * (column_count - 1)
        non_data_space += column_count * padding

    # Space of all columns.
    data_space = sum(column_widths)
    return data_space + non_data_space
