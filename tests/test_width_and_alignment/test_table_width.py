"""Test function in module."""

from terminaltables.width_and_alignment import max_dimensions, table_width, SEPARATOR


def test_empty():
    """Test with zero-length cells."""
    assert table_width(max_dimensions([['']])[2], 0, 0) == 0
    assert table_width(max_dimensions([[SEPARATOR]])[2], 0, 0) == 0
    assert table_width(max_dimensions([['', '', '']])[2], 0, 0) == 0
    assert table_width(max_dimensions([['', '', ''], ['', '', '']])[2], 0, 0) == 0

    assert table_width(max_dimensions([['']], 1, 1)[2], 2, 1) == 4
    assert table_width(max_dimensions([['', '', '']], 1, 1)[2], 2, 1) == 10
    assert table_width(max_dimensions([['', '', ''], ['', '', '']], 1, 1)[2], 2, 1) == 10


def test_single_line():
    """Test with single-line cells."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]

    # '| Lettuce | green | vegetable |'
    outer, inner, outer_widths = 2, 1, max_dimensions(table_data, 1, 1)[2]
    assert table_width(outer_widths, outer, inner) == 31

    # ' Lettuce | green | vegetable '
    outer = 0
    assert table_width(outer_widths, outer, inner) == 29

    # '| Lettuce  green  vegetable |'
    outer, inner = 2, 0
    assert table_width(outer_widths, outer, inner) == 29

    # ' Lettuce  green  vegetable '
    outer = 0
    assert table_width(outer_widths, outer, inner) == 27

    # '|Lettuce |green |vegetable |'
    outer, inner, outer_widths = 2, 1, max_dimensions(table_data, 1)[2]
    assert table_width(outer_widths, outer, inner) == 28

    # '|Lettuce     |green     |vegetable     |'
    outer_widths = max_dimensions(table_data, 3, 2)[2]
    assert table_width(outer_widths, outer, inner) == 40

    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green', 'fruit'],
    ]
    outer, inner, outer_widths = 2, 1, max_dimensions(table_data, 1, 1)[2]
    assert table_width(outer_widths, outer, inner) == 34


def test_multi_line():
    """Test with multi-line cells."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', ('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                     'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    outer, inner, outer_widths = 2, 1, max_dimensions(table_data, 1, 1)[2]
    assert table_width(outer_widths, outer, inner) == 100
