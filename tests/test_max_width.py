"""Test max width of table in a terminal without wrapping."""

from textwrap import dedent

import pytest

from terminaltables.tables import AsciiTable, UnixTable
from terminaltables.terminal_io import terminal_size


def test_terminal_width_height():
    """Test terminal width/height functions."""
    assert terminal_size() == (80, 24)


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_empty(cls):
    """Test on empty tables."""
    table = cls([])
    with pytest.raises(IndexError):
        table.column_max_width(0)
    with pytest.raises(IndexError):
        table.column_max_width(1)

    table = cls([[]])
    with pytest.raises(IndexError):
        table.column_max_width(0)
    with pytest.raises(IndexError):
        table.column_max_width(1)

    table = cls([['']])
    assert table.column_max_width(0) == 76
    with pytest.raises(IndexError):
        table.column_max_width(1)

    table = cls([[' ']])
    assert table.column_max_width(0) == 76
    with pytest.raises(IndexError):
        table.column_max_width(1)


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_simple(cls):
    """Test on simple tables."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = cls(table_data)  # '| Lettuce | green | vegetable |'

    assert table.column_max_width(0) == 56
    assert table.column_max_width(1) == 54
    assert table.column_max_width(2) == 58

    table_data.append(['Watermelon', 'green', 'fruit'])
    assert table.column_max_width(0) == 56
    assert table.column_max_width(1) == 51
    assert table.column_max_width(2) == 55


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_attributes(cls):
    """Test different table attributes."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = cls(table_data)  # '| Lettuce | green | vegetable |'

    table.outer_border = False
    assert table.column_max_width(0) == 58
    assert table.column_max_width(1) == 56
    assert table.column_max_width(2) == 60
    table.outer_border = True

    table.inner_column_border = False
    assert table.column_max_width(0) == 58
    assert table.column_max_width(1) == 56
    assert table.column_max_width(2) == 60
    table.outer_border = False
    assert table.column_max_width(0) == 60
    assert table.column_max_width(1) == 58
    assert table.column_max_width(2) == 62
    table.outer_border = True
    table.inner_column_border = True

    table.padding_left = 0
    assert table.column_max_width(0) == 59
    assert table.column_max_width(1) == 57
    assert table.column_max_width(2) == 61
    table.padding_right = 5
    assert table.column_max_width(0) == 47
    assert table.column_max_width(1) == 45
    assert table.column_max_width(2) == 49


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_multi_line(monkeypatch, cls):
    """Test multi-line tables."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', dedent('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                           'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = cls(table_data)

    assert table.column_max_width(0) == -10
    assert table.column_max_width(1) == 63

    monkeypatch.setattr('terminaltables.base_table.terminal_size', lambda: (100, 24))
    assert table.column_max_width(0) == 10
    assert table.column_max_width(1) == 83
