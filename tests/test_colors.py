# coding=utf-8

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
    table = AsciiTable(table_data, Color('{autocyan}Foods{/autocyan}'))

    expected = dedent("""\
        +Foods----+-------+-----------+
        | Name    | Color | Type      |
        +---------+-------+-----------+
        | Avocado | green | nut       |
        | Tomato  | red   | fruit     |
        | Lettuce | green | vegetable |
        +---------+-------+-----------+""")
    assert expected == Color(table.table).value_no_colors


def test_unicode():
    table_data = [
        [Color('{b}Name{/b}'), Color('{b}Color{/b}'), Color('{b}Type{/b}')],
        ['Avocado', Color('{autogreen}green{/autogreen}'), 'nut'],
        [Color(u'{u}Cupuaçu{/u}'), Color('{autoyellow}yellow{/autoyellow}'), 'fruit'],
        [Color(u'{u}äöüß{/u}'), '', 'neither'],
    ]
    table = AsciiTable(table_data)

    expected = dedent(u"""\
        +---------+--------+---------+
        | Name    | Color  | Type    |
        +---------+--------+---------+
        | Avocado | green  | nut     |
        | Cupuaçu | yellow | fruit   |
        | äöüß    |        | neither |
        +---------+--------+---------+""")
    assert expected == Color(table.table).value_no_colors
