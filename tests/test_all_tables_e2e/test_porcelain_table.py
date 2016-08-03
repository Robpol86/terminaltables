"""PorcelainTable end to end testing."""

from terminaltables import PorcelainTable


def test_single_line():
    """Test single-lined cells."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green']
    ]
    table = PorcelainTable(table_data)
    table.justify_columns[0] = 'left'
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'right'
    actual = table.table

    expected = (
        ' Name       | Color |      Type \n'
        ' Avocado    | green |       nut \n'
        ' Tomato     |  red  |     fruit \n'
        ' Lettuce    | green | vegetable \n'
        ' Watermelon | green |           '
     )
    assert actual == expected


def test_multi_line():
    """Test multi-lined cells."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', 'Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\nDil Pickles'],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = PorcelainTable(table_data)

    # Test defaults.
    actual = table.table
    expected = (
        ' Show       | Characters                                                                          \n'
        ' Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, \n'
        '            | Dil Pickles                                                                         \n'
        ' South Park | Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          '
    )
    assert actual == expected


    # Justify right.
    table.justify_columns = {1: 'right'}
    actual = table.table
    expected = (
        ' Show       |                                                                          Characters \n'
        ' Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, \n'
        '            |                                                                         Dil Pickles \n'
        ' South Park |                          Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick '
    )
    assert actual == expected
