# coding=utf-8
"""Tests for colorclass compatibility."""

from textwrap import dedent

from colorclass import Color

from terminaltables.tables import AsciiTable


def test_ascii():
    """Test colors and ASCII characters."""
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
    assert Color(table.table).value_no_colors == expected


def test_unicode():
    """Test colors and Unicode characters."""
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
    assert Color(table.table).value_no_colors == expected
