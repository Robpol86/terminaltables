from textwrap import dedent

import pytest

from terminaltables import (
    AsciiTable, DosDoubleTable, DosSingleTable, UnicodeDoubleTable, UnicodeSingleTable, UnixTable
)

CLASSES = [AsciiTable, DosDoubleTable, DosSingleTable, UnicodeDoubleTable, UnicodeSingleTable, UnixTable]


@pytest.mark.parametrize('cls', CLASSES)
def test_empty(cls):
    class FakeCls(cls):
        terminal_width = 80

    table = FakeCls([])
    with pytest.raises(IndexError):
        table.column_max_width(0)
    with pytest.raises(IndexError):
        table.column_max_width(1)

    table = FakeCls([[]])
    with pytest.raises(IndexError):
        table.column_max_width(0)
    with pytest.raises(IndexError):
        table.column_max_width(1)

    table = FakeCls([['']])
    assert 76 == table.column_max_width(0)
    with pytest.raises(IndexError):
        table.column_max_width(1)

    table = FakeCls([[' ']])
    assert 76 == table.column_max_width(0)
    with pytest.raises(IndexError):
        table.column_max_width(1)


@pytest.mark.parametrize('cls', CLASSES)
def test_simple(cls):
    class FakeCls(cls):
        terminal_width = 80

    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = FakeCls(table_data)  # '| Lettuce | green | vegetable |'

    assert 56 == table.column_max_width(0)
    assert 54 == table.column_max_width(1)
    assert 58 == table.column_max_width(2)

    table_data.append(['Watermelon', 'green', 'fruit'])
    assert 56 == table.column_max_width(0)
    assert 51 == table.column_max_width(1)
    assert 55 == table.column_max_width(2)


@pytest.mark.parametrize('cls', CLASSES)
def test_multi_line(cls):
    class FakeCls(cls):
        terminal_width = 80

    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', dedent('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                           'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = FakeCls(table_data)

    assert -10 == table.column_max_width(0)
    assert 63 == table.column_max_width(1)

    table.terminal_width = 100
    assert 10 == table.column_max_width(0)
    assert 83 == table.column_max_width(1)
