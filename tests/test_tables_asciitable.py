# coding=utf-8
"""Test end to end showing ASCII table."""

from textwrap import dedent

from terminaltables.other_tables import AsciiTable


def test_empty():
    """Test empty table."""
    expected = dedent("""\
        ++
        ++""")
    table = AsciiTable([])
    assert table.table == expected

    expected = dedent("""\
        ++
        ||
        ++""")
    table = AsciiTable([[]])
    assert table.table == expected

    expected = dedent("""\
        +--+
        |  |
        +--+""")
    table = AsciiTable([['']])
    assert table.table == expected

    expected = dedent("""\
        +---+
        |   |
        +---+""")
    table = AsciiTable([[' ']])
    assert table.table == expected


def test_simple():
    """Test simple table."""
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
        +---------+-------+-----------+""")
    assert table.table == expected

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
        +------------+-------+-----------+""")
    assert table.table == expected


def test_title():
    """Test that table title shows up correctly."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = AsciiTable(table_data, 'Foods')

    expected = dedent("""\
        +Foods----+-------+-----------+
        | Name    | Color | Type      |
        +---------+-------+-----------+
        | Avocado | green | nut       |
        | Tomato  | red   | fruit     |
        | Lettuce | green | vegetable |
        +---------+-------+-----------+""")
    assert table.table == expected

    table.title = 'Foooooooooooooods'
    expected = dedent("""\
        +Foooooooooooooods+-----------+
        | Name    | Color | Type      |
        +---------+-------+-----------+
        | Avocado | green | nut       |
        | Tomato  | red   | fruit     |
        | Lettuce | green | vegetable |
        +---------+-------+-----------+""")
    assert table.table == expected

    table.title = 'Foooooooooooooodsssssssssssss'
    expected = dedent("""\
        +Foooooooooooooodsssssssssssss+
        | Name    | Color | Type      |
        +---------+-------+-----------+
        | Avocado | green | nut       |
        | Tomato  | red   | fruit     |
        | Lettuce | green | vegetable |
        +---------+-------+-----------+""")
    assert table.table == expected

    table.title = 'Foooooooooooooodssssssssssssss'
    expected = dedent("""\
        +---------+-------+-----------+
        | Name    | Color | Type      |
        +---------+-------+-----------+
        | Avocado | green | nut       |
        | Tomato  | red   | fruit     |
        | Lettuce | green | vegetable |
        +---------+-------+-----------+""")
    assert table.table == expected


def test_attributes():
    """Test table attributes."""
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
        +------------+-------+-----------+""")
    assert table.table == expected

    table.justify_columns[2] = 'center'
    expected = dedent("""\
        +------------+-------+-----------+
        |       Name | Color |    Type   |
        +------------+-------+-----------+
        |    Avocado | green |    nut    |
        |     Tomato | red   |   fruit   |
        |    Lettuce | green | vegetable |
        | Watermelon | green |           |
        +------------+-------+-----------+""")
    assert table.table == expected

    table.inner_heading_row_border = False
    expected = dedent("""\
        +------------+-------+-----------+
        |       Name | Color |    Type   |
        |    Avocado | green |    nut    |
        |     Tomato | red   |   fruit   |
        |    Lettuce | green | vegetable |
        | Watermelon | green |           |
        +------------+-------+-----------+""")
    assert table.table == expected

    table.title = 'Foods'
    table.inner_column_border = False
    expected = dedent("""\
        +Foods-------------------------+
        |       Name  Color     Type   |
        |    Avocado  green     nut    |
        |     Tomato  red      fruit   |
        |    Lettuce  green  vegetable |
        | Watermelon  green            |
        +------------------------------+""")
    assert table.table == expected

    table.outer_border = False
    expected = (
        '       Name  Color     Type   \n'
        '    Avocado  green     nut    \n'
        '     Tomato  red      fruit   \n'
        '    Lettuce  green  vegetable \n'
        ' Watermelon  green            '
    )
    assert table.table == expected

    table.outer_border = True
    table.inner_row_border = True
    expected = dedent("""\
        +Foods-------------------------+
        |       Name  Color     Type   |
        +------------------------------+
        |    Avocado  green     nut    |
        +------------------------------+
        |     Tomato  red      fruit   |
        +------------------------------+
        |    Lettuce  green  vegetable |
        +------------------------------+
        | Watermelon  green            |
        +------------------------------+""")
    assert table.table == expected

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
        +------------+-------+-----------+""")
    assert table.table == expected

    table.outer_border = False
    expected = (
        '       Name | Color |    Type   \n'
        '------------+-------+-----------\n'
        '    Avocado | green |    nut    \n'
        '------------+-------+-----------\n'
        '     Tomato | red   |   fruit   \n'
        '------------+-------+-----------\n'
        '    Lettuce | green | vegetable \n'
        '------------+-------+-----------\n'
        ' Watermelon | green |           '
    )
    assert table.table == expected


def test_multi_line():
    """Test multi-line tables."""
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
        +------------+-------------------------------------------------------------------------------------+""")
    assert table.table == expected

    table.inner_row_border = True
    expected = dedent("""\
        +------------+-------------------------------------------------------------------------------------+
        | Show       | Characters                                                                          |
        +------------+-------------------------------------------------------------------------------------+
        | Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |
        |            | Susie Carmichael, Dil Pickles, Kimi Finster, Spike                                  |
        +------------+-------------------------------------------------------------------------------------+
        | South Park | Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          |
        +------------+-------------------------------------------------------------------------------------+""")
    assert table.table == expected

    table.justify_columns = {1: 'right'}
    expected = dedent("""\
        +------------+-------------------------------------------------------------------------------------+
        | Show       |                                                                          Characters |
        +------------+-------------------------------------------------------------------------------------+
        | Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |
        |            |                                  Susie Carmichael, Dil Pickles, Kimi Finster, Spike |
        +------------+-------------------------------------------------------------------------------------+
        | South Park |                          Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick |
        +------------+-------------------------------------------------------------------------------------+""")
    assert table.table == expected


def test_unicode():
    """Test Unicode characters."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        [u'Cupuaçu', 'yellow', 'fruit'],
        [u'äöüß', '', 'neither'],
    ]
    table = AsciiTable(table_data, 'Foods')

    expected = dedent(u"""\
        +Foods----+--------+---------+
        | Name    | Color  | Type    |
        +---------+--------+---------+
        | Avocado | green  | nut     |
        | Cupuaçu | yellow | fruit   |
        | äöüß    |        | neither |
        +---------+--------+---------+""")
    assert table.table == expected
