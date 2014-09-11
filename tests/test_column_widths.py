from textwrap import dedent

import pytest

from terminaltables import AsciiTable, UnixTable


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_empty(cls):
    table = cls([])
    assert [] == table.column_widths

    table = cls([[]])
    assert [] == table.column_widths

    table = cls([['']])
    assert [0] == table.column_widths

    table = cls([[' ']])
    assert [1] == table.column_widths


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_simple(cls):
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = cls(table_data)

    assert [7, 5, 9] == table.column_widths

    table_data.append(['Watermelon', 'green', 'fruit'])
    assert [10, 5, 9] == table.column_widths


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_multi_line(cls):
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', dedent('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                           'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = cls(table_data)
    assert [10, 83] == table.column_widths
