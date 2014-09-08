from textwrap import dedent

import pytest

from terminaltables import (
    AsciiTable, DosDoubleTable, DosSingleTable, UnicodeDoubleTable, UnicodeSingleTable, UnixTable
)


def test_empty():
    return
    table = AsciiTable([])
    with pytest.raises(IndexError):
        str(table.table)

    table = AsciiTable([[]])
    with pytest.raises(IndexError):
        str(table.table)

    expected = dedent("""\
        +--+
        |  |
        +--+\
    """)
    table = AsciiTable([['']])
    assert expected == table.table

    expected = dedent("""\
        +---+
        |   |
        +---+\
    """)
    table = AsciiTable([[' ']])
    assert expected == table.table


def test_simple():
    return
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = AsciiTable(table_data)

    expected = dedent("""\
        +---------+-------+-----------+
        | Name    | Color | Type      |
        +---------+-------+-----------+
        | Avocado | green | nut       |
        | Tomato  | red   | fruit     |
        | Lettuce | green | vegetable |
        +---------+-------+-----------+\
    """)
    assert expected == table.table

    table_data.append(['Watermelon', 'green'])
    table_data.append([])
    expected = dedent("""\
        +------------+-------+-----------+
        | Name       | Color | Type      |
        +------------+-------+-----------+
        | Avocado    | green | nut       |
        | Tomato     | red   | fruit     |
        | Lettuce    | green | vegetable |
        | Watermelon | green |           |
        |            |       |           |
        +------------+-------+-----------+\
    """)
    assert expected == table.table


def test_attributes():
    return
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green']
    ]
    table = AsciiTable(table_data)

    table.justify_columns[0] = 'right'
    expected = dedent("""\
        +------------+-------+-----------+
        |       Name | Color | Type      |
        +------------+-------+-----------+
        |    Avocado | green | nut       |
        |     Tomato | red   | fruit     |
        |    Lettuce | green | vegetable |
        | Watermelon | green |           |
        +------------+-------+-----------+\
    """)
    assert expected == table.table

    table.justify_columns[2] = 'center'
    expected = dedent("""\
        +------------+-------+-----------+
        |       Name | Color |    Type   |
        +------------+-------+-----------+
        |    Avocado | green |    nut    |
        |     Tomato | red   |   fruit   |
        |    Lettuce | green | vegetable |
        | Watermelon | green |           |
        +------------+-------+-----------+\
    """)
    assert expected == table.table

    table.inner_heading_row_border = False
    expected = dedent("""\
        +------------+-------+-----------+
        |       Name | Color |    Type   |
        |    Avocado | green |    nut    |
        |     Tomato | red   |   fruit   |
        |    Lettuce | green | vegetable |
        | Watermelon | green |           |
        +------------+-------+-----------+\
    """)
    assert expected == table.table

    table.title = 'Foods'
    table.inner_column_border = False
    expected = dedent("""\
        +-Foods------------------------+
        |       Name  Color     Type   |
        |    Avocado  green     nut    |
        |     Tomato  red      fruit   |
        |    Lettuce  green  vegetable |
        | Watermelon  green            |
        +------------------------------+\
    """)
    assert expected == table.table

    table.outer_border = False
    expected = """\
       Name  Color     Type
    Avocado  green     nut
     Tomato  red      fruit
    Lettuce  green  vegetable
 Watermelon  green            \
    """
    assert expected == table.table

    table.outer_border = True
    table.inner_row_border = True
    expected = dedent("""\
        +-Foods------------------------+
        |       Name  Color     Type   |
        +------------------------------+
        |    Avocado  green     nut    |
        +------------------------------+
        |     Tomato  red      fruit   |
        +------------------------------+
        |    Lettuce  green  vegetable |
        +------------------------------+
        | Watermelon  green            |
        +------------------------------+\
    """)
    assert expected == table.table

    table.title = False
    table.inner_column_border = True
    table.inner_heading_row_border = False  # Ignored due to inner_row_border.
    table.inner_row_border = True
    expected = dedent("""\
        +------------+-------+-----------+
        |       Name | Color |    Type   |
        +------------+-------+-----------+
        |    Avocado | green |    nut    |
        +------------+-------+-----------+
        |     Tomato | red   |   fruit   |
        +------------+-------+-----------+
        |    Lettuce | green | vegetable |
        +------------+-------+-----------+
        | Watermelon | green |           |
        +------------+-------+-----------+\
    """)
    assert expected == table.table

    table.outer_border = False
    expected = """\
       Name | Color |    Type
------------+-------+-----------
    Avocado | green |    nut
------------+-------+-----------
     Tomato | red   |   fruit
------------+-------+-----------
    Lettuce | green | vegetable
------------+-------+-----------
 Watermelon | green |           \
    """
    assert expected == table.table


def test_multi_line():
    return
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', dedent('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                           'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = AsciiTable(table_data)

    expected = dedent("""\
        +------------+-------------------------------------------------------------------------------------+
        | Show       | Characters                                                                          |
        +------------+-------------------------------------------------------------------------------------+
        | Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |
        |            | Susie Carmichael, Dil Pickles, Kimi Finster, Spike                                  |
        | South Park | Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          |
        +------------+-------------------------------------------------------------------------------------+\
    """)
    assert expected == table.table

    table.inner_row_border = True
    expected = dedent("""\
        +------------+-------------------------------------------------------------------------------------+
        | Show       | Characters                                                                          |
        +------------+-------------------------------------------------------------------------------------+
        | Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |
        |            | Susie Carmichael, Dil Pickles, Kimi Finster, Spike                                  |
        +------------+-------------------------------------------------------------------------------------+
        | South Park | Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          |
        +------------+-------------------------------------------------------------------------------------+\
    """)
    assert expected == table.table
