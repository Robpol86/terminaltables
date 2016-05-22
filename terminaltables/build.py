"""Combine cells into rows."""


def combine(line, left, intersect, right):
    """Zip borders between items in `line`.

    e.g. ('l', '1', 'c', '2', 'c', '3', 'r')

    :param iter line: List to iterate.
    :param left: Left border.
    :param intersect: Column separator.
    :param right: Right border.

    :return: Yields combined objects.
    """
    # Yield left border.
    if left:
        yield left

    # Yield items with intersect characters.
    if intersect:
        try:
            for j, i in enumerate(line, start=-len(line) + 1):
                yield i
                if j:
                    yield intersect
        except TypeError:  # Generator.
            try:
                item = next(line)
            except StopIteration:  # Was empty all along.
                pass
            else:
                while True:
                    yield item
                    try:
                        peek = next(line)
                    except StopIteration:
                        break
                    yield intersect
                    item = peek
    else:
        for i in line:
            yield i

    # Yield right border.
    if right:
        yield right


def build_border(column_widths, horizontal, left, intersect, right):
    """Build the top/bottom/middle row. Optionally embed the table title within the border.

    Example return value:
    ('<', '-----', '+', '------', '+', '-------', '>')

    :param iter column_widths: List of integers representing column widths.
    :param str horizontal: Character to stretch across each column.
    :param str left: Left border.
    :param str intersect: Column separator.
    :param str right: Right border.

    :return: Prepared border as a tuple of strings.
    :rtype: tuple
    """
    return tuple(combine((horizontal * c for c in column_widths), left, intersect, right))
