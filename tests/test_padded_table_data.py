from textwrap import dedent

import pytest

from terminaltables import (
    AsciiTable, DosDoubleTable, DosSingleTable, UnicodeDoubleTable, UnicodeSingleTable, UnixTable
)

CLASSES = [AsciiTable, DosDoubleTable, DosSingleTable, UnicodeDoubleTable, UnicodeSingleTable, UnixTable]


@pytest.mark.parametrize('cls', CLASSES)
def test_empty(cls):
    table = cls([])
    assert [] == table.padded_table_data

    table = cls([[]])
    assert [[]] == table.padded_table_data

    table = cls([['']])
    assert [['  ']] == table.padded_table_data

    table = cls([[' ']])
    assert [['   ']] == table.padded_table_data


@pytest.mark.parametrize('cls', CLASSES)
def test_simple(cls):
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = cls(table_data)

    expected = [
        [' Name    ', ' Color ', ' Type      '],
        [' Avocado ', ' green ', ' nut       '],
        [' Tomato  ', ' red   ', ' fruit     '],
        [' Lettuce ', ' green ', ' vegetable '],
    ]
    assert expected == table.padded_table_data

    table_data.append(['Watermelon', 'green'])
    table_data.append([])
    expected = [
        [' Name       ', ' Color ', ' Type      '],
        [' Avocado    ', ' green ', ' nut       '],
        [' Tomato     ', ' red   ', ' fruit     '],
        [' Lettuce    ', ' green ', ' vegetable '],
        [' Watermelon ', ' green ', '           '],
        ['            ', '       ', '           '],
    ]
    assert expected == table.padded_table_data


@pytest.mark.parametrize('cls', CLASSES)
def test_attributes(cls):
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green']
    ]
    table = cls(table_data)

    table.justify_columns[0] = 'right'
    expected = [
        ['       Name ', ' Color ', ' Type      '],
        ['    Avocado ', ' green ', ' nut       '],
        ['     Tomato ', ' red   ', ' fruit     '],
        ['    Lettuce ', ' green ', ' vegetable '],
        [' Watermelon ', ' green ', '           ']
    ]
    assert expected == table.padded_table_data

    table.justify_columns[2] = 'center'
    expected = [
        ['       Name ', ' Color ', '    Type   '],
        ['    Avocado ', ' green ', '    nut    '],
        ['     Tomato ', ' red   ', '   fruit   '],
        ['    Lettuce ', ' green ', ' vegetable '],
        [' Watermelon ', ' green ', '           ']
    ]
    assert expected == table.padded_table_data


@pytest.mark.parametrize('cls', CLASSES)
def test_multi_line(cls):
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', dedent('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                           'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = cls(table_data)

    expected = [
        [' Show       ', ' Characters                                                                          '],
        [' Rugrats    ', dedent(
                         ' Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, \n'
                         ' Susie Carmichael, Dil Pickles, Kimi Finster, Spike                                  '
        )],
        [' South Park ', ' Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          ']
    ]
    assert expected == table.padded_table_data
