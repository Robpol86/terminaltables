"""Test padding cells."""

import pytest

from terminaltables.tables import AsciiTable, UnixTable


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_empty(cls):
    """Test on empty tables."""
    table = cls([])
    assert table.padded_table_data == []

    table = cls([[]])
    assert table.padded_table_data == [[]]

    table = cls([['']])
    assert table.padded_table_data == [['  ']]

    table = cls([[' ']])
    assert table.padded_table_data == [['   ']]


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_simple(cls):
    """Test on simple tables."""
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
    assert table.padded_table_data == expected

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
    assert table.padded_table_data == expected


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_attributes(cls):
    """Test padding on different text justifications."""
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
    assert table.padded_table_data == expected

    table.justify_columns[2] = 'center'
    expected = [
        ['       Name ', ' Color ', '    Type   '],
        ['    Avocado ', ' green ', '    nut    '],
        ['     Tomato ', ' red   ', '   fruit   '],
        ['    Lettuce ', ' green ', ' vegetable '],
        [' Watermelon ', ' green ', '           ']
    ]
    assert table.padded_table_data == expected


@pytest.mark.parametrize('cls', [AsciiTable, UnixTable])
def test_multi_line(cls):
    """Test on multi-line tables."""
    table_data = [
        ['A', 'B', 'C'],
        ['aaa', 'b\nbb\nbb', 'cc\nccccc'],
        ['aa', 'bb\nbb', 'c\ncc\nccc'],
    ]
    table = cls(table_data)
    table.justify_columns = {1: 'center', 2: 'right'}

    expected = [
        [' A   ', ' B  ', '     C '],
        [' aaa \n     \n     ', ' b  \n bb \n bb ', '    cc \n ccccc \n       '],
        [' aa  \n     \n     ', ' bb \n bb \n    ', '     c \n    cc \n   ccc '],
    ]
    assert table.padded_table_data == expected
