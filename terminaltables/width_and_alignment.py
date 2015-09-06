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
    if hasattr(string, 'value_no_colors'):
        # Colorclass instance.
        string = string.value_no_colors

    if isinstance(string, str) and hasattr(string, 'decode'):
        # Convert to unicode.
        string = string.decode('u8')

    width = 0
    for char in string:
        if unicodedata.east_asian_width(char) in ('F', 'W'):
            width += 2
        else:
            width += 1

    return width


def align_and_pad_cell(string, align, width, height, lpad, rpad):
    """Align a string with center/rjust/ljust and adds additional padding.

    :param str string: Input string to operate on.
    :param str align: 'left', 'right', or 'center'.
    :param int width: Align to this column width.
    :param int height: Pad newlines and spaces to set cell to this height.
    :param int lpad: Number of spaces to pad on the left.
    :param int rpad: Number of spaces to pad on the right.

    :return: Modified string.
    :rtype: str
    """
    # Handle trailing newlines or empty strings, str.splitlines() does not satisfy.
    lines = string.splitlines() or ['']
    if string.endswith('\n'):
        lines.append('')

    # Align.
    if align == 'center':
        aligned = '\n'.join(l.center(width + len(l) - string_width(l)) for l in lines)
    elif align == 'right':
        aligned = '\n'.join(l.rjust(width + len(l) - string_width(l)) for l in lines)
    else:
        aligned = '\n'.join(l.ljust(width + len(l) - string_width(l)) for l in lines)

    # Pad.
    padded = '\n'.join((' ' * lpad) + l + (' ' * rpad) for l in aligned.splitlines() or [''])

    # Increase height.
    additional_padding = height - 1 - padded.count('\n')
    if additional_padding > 0:
        padded += ('\n{0}'.format(' ' * (width + lpad + rpad))) * additional_padding

    return padded
