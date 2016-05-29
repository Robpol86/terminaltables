"""Combine cells into rows."""

from terminaltables.width_and_alignment import visible_width


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


def build_border(outer_widths, horizontal, left, intersect, right, title=None):
    """Build the top/bottom/middle row. Optionally embed the table title within the border.

    Title is hidden if it doesn't fit between the left/right characters/edges.

    Example return value:
    ('<', '-----', '+', '------', '+', '-------', '>')
    ('<', 'My Table', '----', '+', '------->')

    :param iter outer_widths: List of widths (with padding) for each column.
    :param str horizontal: Character to stretch across each column.
    :param str left: Left border.
    :param str intersect: Column separator.
    :param str right: Right border.
    :param str title: Overlay the title on the border between the left and right characters.

    :return: Prepared border as a tuple of strings.
    :rtype: tuple
    """
    length = 0

    # Hide title if it doesn't fit.
    if title and outer_widths:
        length = visible_width(title)
        if length > sum(outer_widths) + len(intersect) * (len(outer_widths) - 1):
            title = None

    # Handle no title.
    if not title or not outer_widths or not horizontal:
        return tuple(combine((horizontal * c for c in outer_widths), left, intersect, right))

    # Handle title fitting in the first column.
    if length == outer_widths[0]:
        return tuple(combine([title] + [horizontal * c for c in outer_widths[1:]], left, intersect, right))
    if length < outer_widths[0]:
        columns = [title + horizontal * (outer_widths[0] - length)] + [horizontal * c for c in outer_widths[1:]]
        return tuple(combine(columns, left, intersect, right))

    # Handle wide titles/narrow columns.
    columns_and_intersects = [title]
    for width in combine(outer_widths, None, bool(intersect), None):
        # If title is taken care of.
        if length < 1:
            columns_and_intersects.append(intersect if width is True else horizontal * width)
        # If title's last character overrides an intersect character.
        elif width is True and length == 1:
            length = 0
        # If this is an intersect character that is overridden by the title.
        elif width is True:
            length -= 1
        # If title's last character is within a column.
        elif width >= length:
            columns_and_intersects[0] += horizontal * (width - length)  # Append horizontal chars to title.
            length = 0
        # If remainder of title won't fit in a column.
        else:
            length -= width

    return tuple(combine(columns_and_intersects, left, None, right))


def build_row(row, left, center, right):
    """Combine single or multi-lined cells into a single row of list of lists including borders.

    Row must already be padded and extended so each cell has the same number of lines.

    Example return value:
    [
        ['>', 'Left ', '|', 'Center', '|', 'Right', '<'],
        ['>', 'Cell1', '|', 'Cell2 ', '|', 'Cell3', '<'],
    ]

    :param iter row: List of cells for one row.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.

    :return: Prepared row as a list of tuple of strings.
    :rtype: tuple
    """
    if not row or not row[0]:
        return [tuple(combine((), left, center, right))]
    combined = list()
    for row_index in range(len(row[0])):
        combined.append(tuple(combine((c[row_index] for c in row), left, center, right)))
    return combined


def flatten(table):
    """Flatten table data into a single string with newlines.

    :param iter table: Padded and bordered table data.

    :return: Joined rows/cells.
    :rtype: str
    """
    return '\n'.join(''.join(r) for r in table)
