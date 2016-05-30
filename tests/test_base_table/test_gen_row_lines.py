"""Test method in BaseTable class."""

import pytest

from terminaltables.base_table import BaseTable


@pytest.mark.parametrize('style', ['heading', 'footing', 'row'])
def test_single_line(style):
    """Test with single-line row.

    :param str style: Passed to method.
    """
    row = ['Row One Column One', 'Two', 'Three']
    table = BaseTable([row])
    actual = [tuple(i) for i in table.gen_row_lines(row, style, [18, 3, 5], 1)]
    expected = [
        ('|', ' Row One Column One ', '|', ' Two ', '|', ' Three ', '|'),
    ]
    assert actual == expected


@pytest.mark.parametrize('style', ['heading', 'footing', 'row'])
def test_multi_line(style):
    """Test with multi-line row.

    :param str style: Passed to method.
    """
    row = ['Row One\nColumn One', 'Two', 'Three']
    table = BaseTable([row])
    actual = [tuple(i) for i in table.gen_row_lines(row, style, [10, 3, 5], 2)]
    expected = [
        ('|', ' Row One    ', '|', ' Two ', '|', ' Three ', '|'),
        ('|', ' Column One ', '|', '     ', '|', '       ', '|'),
    ]
    assert actual == expected


@pytest.mark.parametrize('style', ['heading', 'footing', 'row'])
def test_no_padding_no_borders(style):
    """Test without padding or borders.

    :param str style: Passed to method.
    """
    row = ['Row One\nColumn One', 'Two', 'Three']
    table = BaseTable([row])
    table.inner_column_border = False
    table.outer_border = False
    table.padding_left = 0
    table.padding_right = 0
    actual = [tuple(i) for i in table.gen_row_lines(row, style, [10, 3, 5], 2)]
    expected = [
        ('Row One   ', 'Two', 'Three'),
        ('Column One', '   ', '     '),
    ]
    assert actual == expected


@pytest.mark.parametrize('style', ['heading', 'footing', 'row'])
def test_uneven(style):
    """Test with row missing cells.

    :param str style: Passed to method.
    """
    row = ['Row One Column One']
    table = BaseTable([row])
    actual = [tuple(i) for i in table.gen_row_lines(row, style, [18, 3, 5], 1)]
    expected = [
        ('|', ' Row One Column One ', '|', '     ', '|', '       ', '|'),
    ]
    assert actual == expected


@pytest.mark.parametrize('style', ['heading', 'footing', 'row'])
def test_empty_table(style):
    """Test empty table.

    :param str style: Passed to method.
    """
    row = []
    table = BaseTable([row])
    actual = [tuple(i) for i in table.gen_row_lines(row, style, [], 0)]
    expected = [
        ('|', '|'),
    ]
    assert actual == expected
