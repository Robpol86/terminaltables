# coding: utf-8
"""Test property in BaseTable class."""

from colorama import Fore
from colorclass import Color
from termcolor import colored

from terminaltables.base_table import BaseTable
from terminaltables.width_and_alignment import SEPARATOR


def test_ascii():
    """Test with ASCII characters."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = BaseTable(table_data)
    actual = table.table

    expected = (
        '+---------+-------+-----------+\n'
        '| Name    | Color | Type      |\n'
        '+---------+-------+-----------+\n'
        '| Avocado | green | nut       |\n'
        '| Tomato  | red   | fruit     |\n'
        '| Lettuce | green | vegetable |\n'
        '+---------+-------+-----------+'
    )

    assert actual == expected


def test_separators():
    """Test with SEPARATORs thrown in the mix."""
    table_data = [
        # vegetables
        ['Name', 'Color', 'Type'],
        ['Lettuce', 'green', 'vegetable'],
        ['Potato', 'yellow', 'vegetable'],
        ['Carrot', 'red', 'vegetable'],
        # fruits
        [SEPARATOR],
        ['Tomato', 'red', 'fruit'],
        ['Durian', 'yellow', 'fruit'],
        # nuts
        [SEPARATOR],
        ['Avocado', 'green', 'nut'],
        ['Wallnut', 'brown', 'nut'],
    ]

    table = BaseTable(table_data)
    actual = table.table
    expected = (
        '+---------+--------+-----------+\n'
        '| Name    | Color  | Type      |\n'
        '+---------+--------+-----------+\n'
        '| Lettuce | green  | vegetable |\n'
        '| Potato  | yellow | vegetable |\n'
        '| Carrot  | red    | vegetable |\n'
        '+---------+--------+-----------+\n'
        '| Tomato  | red    | fruit     |\n'
        '| Durian  | yellow | fruit     |\n'
        '+---------+--------+-----------+\n'
        '| Avocado | green  | nut       |\n'
        '| Wallnut | brown  | nut       |\n'
        '+---------+--------+-----------+'
    )

    assert actual == expected


def test_int():
    """Test with integers instead of strings."""
    table_data = [
        [100, 10, 1],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
    ]
    table = BaseTable(table_data, 1234567890)
    actual = table.table

    expected = (
        '+1234567890+---+\n'
        '| 100 | 10 | 1 |\n'
        '+-----+----+---+\n'
        '| 0   | 3  | 6 |\n'
        '| 1   | 4  | 7 |\n'
        '| 2   | 5  | 8 |\n'
        '+-----+----+---+'
    )

    assert actual == expected


def test_float():
    """Test with floats instead of strings."""
    table_data = [
        [1.0, 22.0, 333.0],
        [0.1, 3.1, 6.1],
        [1.1, 4.1, 7.1],
        [2.1, 5.1, 8.1],
    ]
    table = BaseTable(table_data, 0.12345678)
    actual = table.table

    expected = (
        '+0.12345678--+-------+\n'
        '| 1.0 | 22.0 | 333.0 |\n'
        '+-----+------+-------+\n'
        '| 0.1 | 3.1  | 6.1   |\n'
        '| 1.1 | 4.1  | 7.1   |\n'
        '| 2.1 | 5.1  | 8.1   |\n'
        '+-----+------+-------+'
    )

    assert actual == expected


def test_bool_none():
    """Test with NoneType/boolean instead of strings."""
    table_data = [
        [True, False, None],
        [True, False, None],
        [False, None, True],
        [None, True, False],
    ]
    table = BaseTable(table_data, True)
    actual = table.table

    expected = (
        '+True---+-------+-------+\n'
        '| True  | False | None  |\n'
        '+-------+-------+-------+\n'
        '| True  | False | None  |\n'
        '| False | None  | True  |\n'
        '| None  | True  | False |\n'
        '+-------+-------+-------+'
    )

    assert actual == expected


def test_cjk():
    """Test with CJK characters."""
    table_data = [
        ['CJK'],
        ['蓝色'],
        ['世界你好'],
    ]
    table = BaseTable(table_data)
    actual = table.table

    expected = (
        '+----------+\n'
        '| CJK      |\n'
        '+----------+\n'
        '| 蓝色     |\n'
        '| 世界你好 |\n'
        '+----------+'
    )

    assert actual == expected


def test_rtl():
    """Test with RTL characters."""
    table_data = [
        ['RTL'],
        ['שלום'],
        ['معرب'],
    ]
    table = BaseTable(table_data)
    actual = table.table

    expected = (
        '+------+\n'
        '| RTL  |\n'
        '+------+\n'
        '| שלום |\n'
        '| معرب |\n'
        '+------+'
    )

    assert actual == expected


def test_rtl_large():
    """Test large table of RTL characters."""
    table_data = [
        ['اكتب', 'اللون', 'اسم'],
        ['البندق', 'أخضر', 'أفوكادو'],
        ['ثمرة', 'أحمر', 'بندورة'],
        ['الخضروات', 'أخضر', 'الخس'],
    ]
    table = BaseTable(table_data, 'جوجل المترجم')
    actual = table.table

    expected = (
        '+جوجل المترجم------+---------+\n'
        '| اكتب     | اللون | اسم     |\n'
        '+----------+-------+---------+\n'
        '| البندق   | أخضر  | أفوكادو |\n'
        '| ثمرة     | أحمر  | بندورة  |\n'
        '| الخضروات | أخضر  | الخس    |\n'
        '+----------+-------+---------+'
    )

    assert actual == expected


def test_color():
    """Test with color characters."""
    table_data = [
        ['ansi', '\033[31mRed\033[39m', '\033[32mGreen\033[39m', '\033[34mBlue\033[39m'],
        ['colorclass', Color('{red}Red{/red}'), Color('{green}Green{/green}'), Color('{blue}Blue{/blue}')],
        ['colorama', Fore.RED + 'Red' + Fore.RESET, Fore.GREEN + 'Green' + Fore.RESET, Fore.BLUE + 'Blue' + Fore.RESET],
        ['termcolor', colored('Red', 'red'), colored('Green', 'green'), colored('Blue', 'blue')],
    ]
    table = BaseTable(table_data)
    table.inner_heading_row_border = False
    actual = table.table

    expected = (
        u'+------------+-----+-------+------+\n'
        u'| ansi       | \033[31mRed\033[39m | \033[32mGreen\033[39m | \033[34mBlue\033[39m |\n'
        u'| colorclass | \033[31mRed\033[39m | \033[32mGreen\033[39m | \033[34mBlue\033[39m |\n'
        u'| colorama   | \033[31mRed\033[39m | \033[32mGreen\033[39m | \033[34mBlue\033[39m |\n'
        u'| termcolor  | \033[31mRed\033[0m | \033[32mGreen\033[0m | \033[34mBlue\033[0m |\n'
        u'+------------+-----+-------+------+'
    )

    assert actual == expected
