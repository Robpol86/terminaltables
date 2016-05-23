"""Test method in BaseTable class."""

from terminaltables.base_table import BaseTable


def test_single_line():
    """Test with single-line row."""
    row = ['Row One Column One', 'Two', 'Three']
    table = BaseTable([row])
    actual = list(table.gen_cell_lines(row, [18, 3, 5], 1))
    expected = [
        ('|', ' Row One Column One ', '|', ' Two ', '|', ' Three ', '|'),
    ]
    assert actual == expected


def test_multi_line():
    """Test with multi-line row."""
    row = ['Row One\nColumn One', 'Two', 'Three']
    table = BaseTable([row])
    actual = list(table.gen_cell_lines(row, [10, 3, 5], 2))
    expected = [
        ('|', ' Row One    ', '|', ' Two ', '|', ' Three ', '|'),
        ('|', ' Column One ', '|', '     ', '|', '       ', '|'),
    ]
    assert actual == expected


def test_no_padding_no_borders():
    """Test without padding or borders."""
    row = ['Row One\nColumn One', 'Two', 'Three']
    table = BaseTable([row])
    table.inner_column_border = False
    table.outer_border = False
    table.padding_left = 0
    table.padding_right = 0
    actual = list(table.gen_cell_lines(row, [10, 3, 5], 2))
    expected = [
        ('Row One   ', 'Two', 'Three'),
        ('Column One', '   ', '     '),
    ]
    assert actual == expected


def test_uneven():
    """Test with row missing cells."""
    row = ['Row One Column One']
    table = BaseTable([row])
    actual = list(table.gen_cell_lines(row, [18, 3, 5], 1))
    expected = [
        ('|', ' Row One Column One ', '|', '     ', '|', '       ', '|'),
    ]
    assert actual == expected


def test_empty_table():
    """Test empty table."""
    row = []
    table = BaseTable([row])
    actual = list(table.gen_cell_lines(row, [], 0))
    expected = [
        ('|', '|'),
    ]
    assert actual == expected
