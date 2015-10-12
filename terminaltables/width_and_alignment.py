"""Functions that handle alignment, padding, widths, etc."""

import unicodedata


def string_width(string):
    """Get the visible width of a unicode string.

    Some CJK unicode characters are more than one byte unlike ASCII and latin unicode characters.

    From: https://github.com/Robpol86/terminaltables/pull/9

    :param str string: String to measure.

    :return: String's width.
    :rtype: int
    """
    # Colorclass instance.
    if hasattr(string, 'value_no_colors'):
        string = string.value_no_colors

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


def align_and_pad_cell(string, align, size_dims):
    """Align a string with center/rjust/ljust and adds additional padding.

    :param str string: Input string to operate on.
    :param str align: 'left', 'right', or 'center'.
    :param iter size_dims: Size and dimensions. A 4-item tuple of integers representing width, height, lpad, and rpad.

    :return: Modified string.
    :rtype: str
    """
    width, height, lpad, rpad = size_dims

    # Handle trailing newlines or empty strings, str.splitlines() does not satisfy.
    lines = string.splitlines() or ['']
    if string.endswith('\n'):
        lines.append('')

    # Align.
    if align == 'center':
        method = 'center'
    elif align == 'right':
        method = 'rjust'
    else:
        method = 'ljust'
    aligned = '\n'.join(getattr(l, method)(width + len(l) - string_width(l)) for l in lines)

    # Pad.
    padded = '\n'.join((' ' * lpad) + l + (' ' * rpad) for l in aligned.splitlines() or [''])

    # Increase height.
    additional_padding = height - 1 - padded.count('\n')
    if additional_padding > 0:
        padded += ('\n{0}'.format(' ' * (width + lpad + rpad))) * additional_padding

    return padded


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
            widths[i] = max(widths[i], string_width(max(row[i].splitlines(), key=len)))

    return widths
