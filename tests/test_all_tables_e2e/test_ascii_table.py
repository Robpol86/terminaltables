# coding=utf-8
"""AsciiTable end to end testing."""

from terminaltables import AsciiTable


def test_single_line():
    """Test single-lined cells."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green'],
        [],
    ]
    table = AsciiTable(table_data, 'Example')
    table.inner_footing_row_border = True
    table.justify_columns[0] = 'left'
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'right'
    actual = table.table

    expected = (
        '+Example-----+-------+-----------+\n'
        '| Name       | Color |      Type |\n'
        '+------------+-------+-----------+\n'
        '| Avocado    | green |       nut |\n'
        '| Tomato     |  red  |     fruit |\n'
        '| Lettuce    | green | vegetable |\n'
        '| Watermelon | green |           |\n'
        '+------------+-------+-----------+\n'
        '|            |       |           |\n'
        '+------------+-------+-----------+'
    )
    assert actual == expected


def test_multi_line():
    """Test multi-lined cells."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', 'Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\nDil Pickles'],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = AsciiTable(table_data)

    # Test defaults.
    actual = table.table
    expected = (
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Show       | Characters                                                                          |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |\n'
        '|            | Dil Pickles                                                                         |\n'
        '| South Park | Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          |\n'
        '+------------+-------------------------------------------------------------------------------------+'
    )
    assert actual == expected

    # Test inner row border.
    table.inner_row_border = True
    actual = table.table
    expected = (
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Show       | Characters                                                                          |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |\n'
        '|            | Dil Pickles                                                                         |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| South Park | Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          |\n'
        '+------------+-------------------------------------------------------------------------------------+'
    )
    assert actual == expected

    # Justify right.
    table.justify_columns = {1: 'right'}
    actual = table.table
    expected = (
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Show       |                                                                          Characters |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |\n'
        '|            |                                                                         Dil Pickles |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| South Park |                          Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick |\n'
        '+------------+-------------------------------------------------------------------------------------+'
    )
    assert actual == expected
