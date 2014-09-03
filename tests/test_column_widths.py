from textwrap import dedent

from terminaltables import AsciiTable


def test_empty():
    table = AsciiTable([])
    assert [] == table.column_widths

    table = AsciiTable([[]])
    assert [] == table.column_widths

    table = AsciiTable([['']])
    assert [0] == table.column_widths

    table = AsciiTable([[' ']])
    assert [1] == table.column_widths


def test_simple():
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = AsciiTable(table_data)

    assert [7, 5, 9] == table.column_widths

    table_data.append(['Watermelon', 'green', 'fruit'])
    assert [10, 5, 9] == table.column_widths


def test_multi_line():
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', dedent('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                           'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = AsciiTable(table_data)
    assert [10, 83] == table.column_widths
