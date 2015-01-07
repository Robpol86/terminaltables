from textwrap import dedent

from colorclass import Color
from terminaltables import AsciiTable


def test_ascii():
    table_data = [
        [Color('{b}Name{/b}'), Color('{b}Color{/b}'), Color('{b}Type{/b}')],
        ['Avocado', Color('{autogreen}green{/autogreen}'), 'nut'],
        ['Tomato', Color('{autored}red{/autored}'), 'fruit'],
        ['Lettuce', Color('{autogreen}green{/autogreen}'), 'vegetable'],
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
    assert expected == Color(table.table).value_no_colors
