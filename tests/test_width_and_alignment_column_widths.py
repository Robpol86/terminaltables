"""Tests for column widths."""

from terminaltables.width_and_alignment import column_widths


def test_empty():
    """Test empty tables."""
    assert column_widths([]) == []
    assert column_widths([[]]) == []
    assert column_widths([['']]) == [0]
    assert column_widths([[' ']]) == [1]
    assert column_widths([[' '], ['', '  ']]) == [1, 2]
    assert column_widths([['', ''], [' ', ' ']]) == [1, 1]


def test_simple():
    """Easy test."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    assert column_widths(table_data) == [7, 5, 9]

    table_data.append(['Watermelon', 'green', 'fruit'])
    assert column_widths(table_data) == [10, 5, 9]


def test_multi_line():
    """Multi-line test."""
    assert column_widths([['One\nTwo', 'Buckle\nMy\nShoe']]) == [3, 6]

    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', ('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                     'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    assert column_widths(table_data) == [10, 83]
