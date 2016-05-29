"""Test function in module."""

from terminaltables.build import flatten


def test_one_line():
    """Test with one line cells."""
    table = [
        ['>', 'Left Cell', '|', 'Center Cell', '|', 'Right Cell', '<'],
    ]
    actual = flatten(table)
    expected = '>Left Cell|Center Cell|Right Cell<'
    assert actual == expected


def test_two_line():
    """Test with two line cells."""
    table = [
        ['>', 'Left ', '|', 'Center', '|', 'Right', '<'],
        ['>', 'Cell1', '|', 'Cell2 ', '|', 'Cell3', '<'],
    ]
    actual = flatten(table)
    expected = ('>Left |Center|Right<\n'
                '>Cell1|Cell2 |Cell3<')
    assert actual == expected
