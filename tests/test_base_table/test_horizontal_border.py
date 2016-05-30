"""Test method in BaseTable class."""

import pytest

from terminaltables.base_table import BaseTable
from terminaltables.width_and_alignment import max_dimensions

SINGLE_LINE = (
    ('Name', 'Color', 'Type'),
    ('Avocado', 'green', 'nut'),
    ('Tomato', 'red', 'fruit'),
    ('Lettuce', 'green', 'vegetable'),
)


@pytest.mark.parametrize('inner_column_border', [True, False])
@pytest.mark.parametrize('style', ['top', 'bottom'])
def test_top_bottom(inner_column_border, style):
    """Test top and bottom borders.

    :param bool inner_column_border: Passed to table class.
    :param str style: Passed to method.
    """
    table = BaseTable(SINGLE_LINE, 'Example')
    table.inner_column_border = inner_column_border
    outer_widths = max_dimensions(table.table_data, table.padding_left, table.padding_right)[2]

    # Determine expected.
    if style == 'top' and inner_column_border:
        expected = '+Example--+-------+-----------+'
    elif style == 'top':
        expected = '+Example--------------------+'
    elif style == 'bottom' and inner_column_border:
        expected = '+---------+-------+-----------+'
    else:
        expected = '+---------------------------+'

    # Test.
    actual = ''.join(table.horizontal_border(style, outer_widths))
    assert actual == expected


@pytest.mark.parametrize('inner_column_border', [True, False])
@pytest.mark.parametrize('outer_border', [True, False])
@pytest.mark.parametrize('style', ['heading', 'footing'])
def test_heading_footing(inner_column_border, outer_border, style):
    """Test heading and footing borders.

    :param bool inner_column_border: Passed to table class.
    :param bool outer_border: Passed to table class.
    :param str style: Passed to method.
    """
    table = BaseTable(SINGLE_LINE)
    table.inner_column_border = inner_column_border
    table.outer_border = outer_border
    outer_widths = max_dimensions(table.table_data, table.padding_left, table.padding_right)[2]

    # Determine expected.
    if style == 'heading' and outer_border:
        expected = '+---------+-------+-----------+' if inner_column_border else '+---------------------------+'
    elif style == 'heading':
        expected = '---------+-------+-----------' if inner_column_border else '---------------------------'
    elif style == 'footing' and outer_border:
        expected = '+---------+-------+-----------+' if inner_column_border else '+---------------------------+'
    else:
        expected = '---------+-------+-----------' if inner_column_border else '---------------------------'

    # Test.
    actual = ''.join(table.horizontal_border(style, outer_widths))
    assert actual == expected


@pytest.mark.parametrize('inner_column_border', [True, False])
@pytest.mark.parametrize('outer_border', [True, False])
def test_row(inner_column_border, outer_border):
    """Test inner borders.

    :param bool inner_column_border: Passed to table class.
    :param bool outer_border: Passed to table class.
    """
    table = BaseTable(SINGLE_LINE)
    table.inner_column_border = inner_column_border
    table.outer_border = outer_border
    outer_widths = max_dimensions(table.table_data, table.padding_left, table.padding_right)[2]

    # Determine expected.
    if inner_column_border and outer_border:
        expected = '+---------+-------+-----------+'
    elif inner_column_border:
        expected = '---------+-------+-----------'
    elif outer_border:
        expected = '+---------------------------+'
    else:
        expected = '---------------------------'

    # Test.
    actual = ''.join(table.horizontal_border('row', outer_widths))
    assert actual == expected
