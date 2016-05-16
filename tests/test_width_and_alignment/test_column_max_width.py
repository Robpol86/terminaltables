"""Test function in module."""

from terminaltables.width_and_alignment import column_max_width


def test_empty(monkeypatch):
    """Test with zero-length cells.

    :param monkeypatch: pytest fixture.
    """
    monkeypatch.setattr('terminaltables.width_and_alignment.terminal_size', lambda: (79, 24))

    assert column_max_width([['']], 0, 0, 0, 0) == 79
    assert column_max_width([['', '', '']], 0, 0, 0, 0) == 79
    assert column_max_width([['', '', ''], ['', '', '']], 0, 0, 0, 0) == 79

    assert column_max_width([['']], 0, 2, 1, 2) == 75
    assert column_max_width([['', '', '']], 0, 2, 1, 2) == 69
    assert column_max_width([['', '', ''], ['', '', '']], 0, 2, 1, 2) == 69


def test_single_line(monkeypatch):
    """Test with single-line cells.

    :param monkeypatch: pytest fixture.
    """
    monkeypatch.setattr('terminaltables.width_and_alignment.terminal_size', lambda: (79, 24))

    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]

    # '| Lettuce | green | vegetable |'
    outer, inner, padding = 2, 1, 2
    assert column_max_width(table_data, 0, outer, inner, padding) == 55
    assert column_max_width(table_data, 1, outer, inner, padding) == 53
    assert column_max_width(table_data, 2, outer, inner, padding) == 57

    # ' Lettuce | green | vegetable '
    outer = 0
    assert column_max_width(table_data, 0, outer, inner, padding) == 57
    assert column_max_width(table_data, 1, outer, inner, padding) == 55
    assert column_max_width(table_data, 2, outer, inner, padding) == 59

    # '| Lettuce  green  vegetable |'
    outer, inner = 2, 0
    assert column_max_width(table_data, 0, outer, inner, padding) == 57
    assert column_max_width(table_data, 1, outer, inner, padding) == 55
    assert column_max_width(table_data, 2, outer, inner, padding) == 59

    # ' Lettuce  green  vegetable '
    outer = 0
    assert column_max_width(table_data, 0, outer, inner, padding) == 59
    assert column_max_width(table_data, 1, outer, inner, padding) == 57
    assert column_max_width(table_data, 2, outer, inner, padding) == 61

    # '|Lettuce |green |vegetable |'
    outer, inner, padding = 2, 1, 1
    assert column_max_width(table_data, 0, outer, inner, padding) == 58
    assert column_max_width(table_data, 1, outer, inner, padding) == 56
    assert column_max_width(table_data, 2, outer, inner, padding) == 60

    # '|Lettuce     |green     |vegetable     |'
    padding = 5
    assert column_max_width(table_data, 0, outer, inner, padding) == 46
    assert column_max_width(table_data, 1, outer, inner, padding) == 44
    assert column_max_width(table_data, 2, outer, inner, padding) == 48

    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green', 'fruit'],
    ]
    outer, inner, padding = 2, 1, 2
    assert column_max_width(table_data, 0, outer, inner, padding) == 55
    assert column_max_width(table_data, 1, outer, inner, padding) == 50
    assert column_max_width(table_data, 2, outer, inner, padding) == 54


def test_multi_line(monkeypatch):
    """Test with multi-line cells.

    :param monkeypatch: pytest fixture.
    """
    monkeypatch.setattr('terminaltables.width_and_alignment.terminal_size', lambda: (79, 24))

    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', ('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                     'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    outer, inner, padding = 2, 1, 2

    assert column_max_width(table_data, 0, outer, inner, padding) == -11
    assert column_max_width(table_data, 1, outer, inner, padding) == 62

    monkeypatch.setattr('terminaltables.width_and_alignment.terminal_size', lambda: (100, 24))
    assert column_max_width(table_data, 0, outer, inner, padding) == 10
    assert column_max_width(table_data, 1, outer, inner, padding) == 83
