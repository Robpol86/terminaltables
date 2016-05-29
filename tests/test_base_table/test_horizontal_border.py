"""Test method in BaseTable class."""

import pytest

from terminaltables.base_table import BaseTable
from terminaltables.width_and_alignment import max_dimensions


@pytest.mark.parametrize('inner_column_border', [True, False])
@pytest.mark.parametrize('outer_border', [True, False])
@pytest.mark.parametrize('style', ['top', 'bottom', 'row'])
def test(inner_column_border, outer_border, style):
    """Test method.

    :param bool inner_column_border: Passed to table class.
    :param bool outer_border: Passed to table class.
    :param str style: Passed to method.
    """
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = BaseTable(table_data, 'Example')
    table.inner_column_border = inner_column_border
    table.outer_border = outer_border
    outer_widths = max_dimensions(table.table_data, table.padding_left, table.padding_right)[2]

    # Skip illogical.
    if outer_border and style in ('top', 'bottom'):
        return pytest.skip('Not expected to be called with no outer border.')

    # Determine expected.
    if style == 'top':
        expected = '+Example--+-------+-----------+' if inner_column_border else '+Example--------------------+'
    elif style == 'bottom':
        expected = '+---------+-------+-----------+' if inner_column_border else '+---------------------------+'
    elif inner_column_border and outer_border:
        expected = '+---------+-------+-----------+'
    elif inner_column_border:
        expected = '---------+-------+-----------'
    elif outer_border:
        expected = '+---------------------------+'
    else:
        expected = '---------------------------'

    # Test.
    actual = ''.join(table.horizontal_border(style, outer_widths))
    assert actual == expected
