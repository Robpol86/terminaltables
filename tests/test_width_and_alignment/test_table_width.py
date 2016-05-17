"""Test function in module."""

from terminaltables.width_and_alignment import table_width


def test_empty():
    """Test with zero-length cells."""
    assert table_width([['']], 0, 0, 0) == 0
    assert table_width([['', '', '']], 0, 0, 0) == 0
    assert table_width([['', '', ''], ['', '', '']], 0, 0, 0) == 0

    assert table_width([['']], 2, 1, 2) == 4
    assert table_width([['', '', '']], 2, 1, 2) == 10
    assert table_width([['', '', ''], ['', '', '']], 2, 1, 2) == 10


def test_single_line():
    """Test with single-line cells."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]

    # '| Lettuce | green | vegetable |'
    outer, inner, padding = 2, 1, 2
    assert table_width(table_data, outer, inner, padding) == 31

    # ' Lettuce | green | vegetable '
    outer = 0
    assert table_width(table_data, outer, inner, padding) == 29

    # '| Lettuce  green  vegetable |'
    outer, inner = 2, 0
    assert table_width(table_data, outer, inner, padding) == 29

    # ' Lettuce  green  vegetable '
    outer = 0
    assert table_width(table_data, outer, inner, padding) == 27

    # '|Lettuce |green |vegetable |'
    outer, inner, padding = 2, 1, 1
    assert table_width(table_data, outer, inner, padding) == 28

    # '|Lettuce     |green     |vegetable     |'
    padding = 5
    assert table_width(table_data, outer, inner, padding) == 40

    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green', 'fruit'],
    ]
    outer, inner, padding = 2, 1, 2
    assert table_width(table_data, outer, inner, padding) == 34


def test_multi_line():
    """Test with multi-line cells."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', ('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                     'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    outer, inner, padding = 2, 1, 2
    assert table_width(table_data, outer, inner, padding) == 100
