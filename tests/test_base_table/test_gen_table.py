"""Test method in BaseTable class."""

import pytest

from terminaltables.base_table import BaseTable
from terminaltables.build import flatten
from terminaltables.width_and_alignment import max_dimensions


@pytest.mark.parametrize('inner_heading_row_border', [True, False])
@pytest.mark.parametrize('inner_footing_row_border', [True, False])
@pytest.mark.parametrize('inner_row_border', [True, False])
def test_inner_row_borders(inner_heading_row_border, inner_footing_row_border, inner_row_border):
    """Test header/footer/row borders.

    :param bool inner_heading_row_border: Passed to table.
    :param bool inner_footing_row_border: Passed to table.
    :param bool inner_row_border: Passed to table.
    """
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = BaseTable(table_data)
    table.inner_heading_row_border = inner_heading_row_border
    table.inner_footing_row_border = inner_footing_row_border
    table.inner_row_border = inner_row_border
    inner_widths, inner_heights, outer_widths = max_dimensions(table_data, table.padding_left, table.padding_right)[:3]
    actual = flatten(table.gen_table(inner_widths, inner_heights, outer_widths))

    # Determine expected.
    if inner_row_border:
        expected = (
            '+---------+-------+-----------+\n'
            '| Name    | Color | Type      |\n'
            '+---------+-------+-----------+\n'
            '| Avocado | green | nut       |\n'
            '+---------+-------+-----------+\n'
            '| Tomato  | red   | fruit     |\n'
            '+---------+-------+-----------+\n'
            '| Lettuce | green | vegetable |\n'
            '+---------+-------+-----------+'
        )
    elif inner_heading_row_border and inner_footing_row_border:
        expected = (
            '+---------+-------+-----------+\n'
            '| Name    | Color | Type      |\n'
            '+---------+-------+-----------+\n'
            '| Avocado | green | nut       |\n'
            '| Tomato  | red   | fruit     |\n'
            '+---------+-------+-----------+\n'
            '| Lettuce | green | vegetable |\n'
            '+---------+-------+-----------+'
        )
    elif inner_heading_row_border:
        expected = (
            '+---------+-------+-----------+\n'
            '| Name    | Color | Type      |\n'
            '+---------+-------+-----------+\n'
            '| Avocado | green | nut       |\n'
            '| Tomato  | red   | fruit     |\n'
            '| Lettuce | green | vegetable |\n'
            '+---------+-------+-----------+'
        )
    elif inner_footing_row_border:
        expected = (
            '+---------+-------+-----------+\n'
            '| Name    | Color | Type      |\n'
            '| Avocado | green | nut       |\n'
            '| Tomato  | red   | fruit     |\n'
            '+---------+-------+-----------+\n'
            '| Lettuce | green | vegetable |\n'
            '+---------+-------+-----------+'
        )
    else:
        expected = (
            '+---------+-------+-----------+\n'
            '| Name    | Color | Type      |\n'
            '| Avocado | green | nut       |\n'
            '| Tomato  | red   | fruit     |\n'
            '| Lettuce | green | vegetable |\n'
            '+---------+-------+-----------+'
        )

    assert actual == expected


@pytest.mark.parametrize('outer_border', [True, False])
def test_outer_borders(outer_border):
    """Test left/right/top/bottom table borders.

    :param bool outer_border: Passed to table.
    """
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = BaseTable(table_data, 'Example Table')
    table.outer_border = outer_border
    inner_widths, inner_heights, outer_widths = max_dimensions(table_data, table.padding_left, table.padding_right)[:3]
    actual = flatten(table.gen_table(inner_widths, inner_heights, outer_widths))

    # Determine expected.
    if outer_border:
        expected = (
            '+Example Table----+-----------+\n'
            '| Name    | Color | Type      |\n'
            '+---------+-------+-----------+\n'
            '| Avocado | green | nut       |\n'
            '| Tomato  | red   | fruit     |\n'
            '| Lettuce | green | vegetable |\n'
            '+---------+-------+-----------+'
        )
    else:
        expected = (
            ' Name    | Color | Type      \n'
            '---------+-------+-----------\n'
            ' Avocado | green | nut       \n'
            ' Tomato  | red   | fruit     \n'
            ' Lettuce | green | vegetable '
        )

    assert actual == expected


@pytest.mark.parametrize('mode', ['row', 'one', 'blank', 'empty', 'none'])
@pytest.mark.parametrize('bare', [False, True])
def test_one_no_rows(mode, bare):
    """Test with one or no rows.

    :param str mode: Type of table contents to test.
    :param bool bare: Disable padding/borders.
    """
    if mode == 'row':
        table_data = [
            ['Avocado', 'green', 'nut'],
        ]
    elif mode == 'one':
        table_data = [
            ['Avocado'],
        ]
    elif mode == 'blank':
        table_data = [
            [''],
        ]
    elif mode == 'empty':
        table_data = [
            [],
        ]
    else:
        table_data = [
        ]
    table = BaseTable(table_data)
    if bare:
        table.inner_column_border = False
        table.inner_footing_row_border = False
        table.inner_heading_row_border = False
        table.inner_row_border = False
        table.outer_border = False
        table.padding_left = 0
        table.padding_right = 0
    inner_widths, inner_heights, outer_widths = max_dimensions(table_data, table.padding_left, table.padding_right)[:3]
    actual = flatten(table.gen_table(inner_widths, inner_heights, outer_widths))

    # Determine expected.
    if mode == 'row':
        if bare:
            expected = (
                'Avocadogreennut'
            )
        else:
            expected = (
                '+---------+-------+-----+\n'
                '| Avocado | green | nut |\n'
                '+---------+-------+-----+'
            )
    elif mode == 'one':
        if bare:
            expected = (
                'Avocado'
            )
        else:
            expected = (
                '+---------+\n'
                '| Avocado |\n'
                '+---------+'
            )
    elif mode == 'blank':  # Remember there's still padding.
        if bare:
            expected = (
                ''
            )
        else:
            expected = (
                '+--+\n'
                '|  |\n'
                '+--+'
            )
    elif mode == 'empty':
        if bare:
            expected = (
                ''
            )
        else:
            expected = (
                '++\n'
                '||\n'
                '++'
            )
    else:
        if bare:
            expected = (
                ''
            )
        else:
            expected = (
                '++\n'
                '++'
            )

    assert actual == expected
