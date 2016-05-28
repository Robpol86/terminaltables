"""Test method in BaseTable class."""

import pytest

from terminaltables.base_table import BaseTable
from terminaltables.width_and_alignment import max_dimensions


@pytest.mark.parametrize('vertical_borders', [True, False])
def test(vertical_borders):
    """Test with and without inner_column_border.

    :param bool vertical_borders: Enable/disable vertical borders.
    """
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = BaseTable(table_data, 'Example')
    table.inner_column_border = vertical_borders
    table.outer_border = vertical_borders
    outer_widths = max_dimensions(table.table_data, (table.padding_left, table.padding_right, 0, 0))[0]

    expected = '+Example--+-------+-----------+' if vertical_borders else 'Example--------------------'
    actual = ''.join(table.horizontal_border('top', outer_widths))
    assert actual == expected

    expected = '+---------+-------+-----------+' if vertical_borders else '---------------------------'
    actual = ''.join(table.horizontal_border('row', outer_widths))
    assert actual == expected

    expected = '+---------+-------+-----------+' if vertical_borders else '---------------------------'
    actual = ''.join(table.horizontal_border('bottom', outer_widths))
    assert actual == expected
