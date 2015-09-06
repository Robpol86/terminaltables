"""Test max width of table in a terminal without wrapping."""

from textwrap import dedent

import pytest

import terminaltables


def test_terminal_width_height():
    """Test terminal width/height functions."""
    assert (80, 24) == terminaltables.terminal_io.terminal_size()


@pytest.mark.parametrize('cls', [terminaltables.AsciiTable, terminaltables.UnixTable])
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
    assert 76 == table.column_max_width(0)
    with pytest.raises(IndexError):
        table.column_max_width(1)

    table = cls([[' ']])
    assert 76 == table.column_max_width(0)
    with pytest.raises(IndexError):
        table.column_max_width(1)


@pytest.mark.parametrize('cls', [terminaltables.AsciiTable, terminaltables.UnixTable])
def test_simple(cls):
    """Test on simple tables."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = cls(table_data)  # '| Lettuce | green | vegetable |'

    assert 56 == table.column_max_width(0)
    assert 54 == table.column_max_width(1)
    assert 58 == table.column_max_width(2)

    table_data.append(['Watermelon', 'green', 'fruit'])
    assert 56 == table.column_max_width(0)
    assert 51 == table.column_max_width(1)
    assert 55 == table.column_max_width(2)


@pytest.mark.parametrize('cls', [terminaltables.AsciiTable, terminaltables.UnixTable])
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
    assert 58 == table.column_max_width(0)
    assert 56 == table.column_max_width(1)
    assert 60 == table.column_max_width(2)
    table.outer_border = True

    table.inner_column_border = False
    assert 58 == table.column_max_width(0)
    assert 56 == table.column_max_width(1)
    assert 60 == table.column_max_width(2)
    table.outer_border = False
    assert 60 == table.column_max_width(0)
    assert 58 == table.column_max_width(1)
    assert 62 == table.column_max_width(2)
    table.outer_border = True
    table.inner_column_border = True

    table.padding_left = 0
    assert 59 == table.column_max_width(0)
    assert 57 == table.column_max_width(1)
    assert 61 == table.column_max_width(2)
    table.padding_right = 5
    assert 47 == table.column_max_width(0)
    assert 45 == table.column_max_width(1)
    assert 49 == table.column_max_width(2)


@pytest.mark.parametrize('cls', [terminaltables.AsciiTable, terminaltables.UnixTable])
def test_multi_line(monkeypatch, cls):
    """Test multi-line tables."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', dedent('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                           'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = cls(table_data)

    assert -10 == table.column_max_width(0)
    assert 63 == table.column_max_width(1)

    monkeypatch.setattr(terminaltables, 'terminal_size', lambda: (100, 24))
    assert 10 == table.column_max_width(0)
    assert 83 == table.column_max_width(1)
