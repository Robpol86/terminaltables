"""Test end to end showing Github flavored markdown table."""

from terminaltables import GithubFlavoredMarkdownTable


def test_simple():
    """Simple GithubFlavoredMarkdownTable test."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = GithubFlavoredMarkdownTable(table_data)

    expected = (
        '| Name    | Color | Type      |\n'
        '|---------|-------|-----------|\n'
        '| Avocado | green | nut       |\n'
        '| Tomato  | red   | fruit     |\n'
        '| Lettuce | green | vegetable |'
    )
    assert expected == table.table

    table.justify_columns[0] = 'center'
    expected = (
        '|   Name  | Color | Type      |\n'
        '|:-------:|-------|-----------|\n'
        '| Avocado | green | nut       |\n'
        '|  Tomato | red   | fruit     |\n'
        '| Lettuce | green | vegetable |'
    )
    assert expected == table.table

    table.justify_columns[1] = 'left'
    expected = (
        '|   Name  | Color | Type      |\n'
        '|:-------:|:------|-----------|\n'
        '| Avocado | green | nut       |\n'
        '|  Tomato | red   | fruit     |\n'
        '| Lettuce | green | vegetable |'
    )
    assert expected == table.table

    table.justify_columns[2] = 'right'
    expected = (
        '|   Name  | Color |      Type |\n'
        '|:-------:|:------|----------:|\n'
        '| Avocado | green |       nut |\n'
        '|  Tomato | red   |     fruit |\n'
        '| Lettuce | green | vegetable |'
    )
    assert expected == table.table
