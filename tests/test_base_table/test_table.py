# coding: utf-8
"""Test property in BaseTable class."""

from colorama import Fore
from colorclass import Color
from termcolor import colored

from terminaltables.base_table import BaseTable


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
