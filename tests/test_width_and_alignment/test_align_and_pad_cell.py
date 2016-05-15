# coding: utf-8
"""Test function in module."""

import pytest
from colorama import Fore
from colorclass import Color
from termcolor import colored

from terminaltables.width_and_alignment import align_and_pad_cell


@pytest.mark.parametrize('string,align,width,expected', [
    (u'test', '', 4, u'test'),
    (Color(u'{blue}Test{/blue}'), '', 4, u'\x1b[34mTest\x1b[39m'),
    (Fore.BLUE + u'Test' + Fore.RESET, '', 4, u'\x1b[34mTest\x1b[39m'),
    (colored(u'Test', 'blue'), '', 4, u'\x1b[34mTest\x1b[0m'),
    (u'蓝色', '', 4, u'蓝色'),
    (u'שלום', '', 4, u'\u05e9\u05dc\u05d5\u05dd'),
    (u'معرب', '', 4, u'\u0645\u0639\u0631\u0628'),

    (u'test', '', 5, u'test '),
    (Color(u'{blue}Test{/blue}'), '', 5, u'\x1b[34mTest\x1b[39m '),
    (Fore.BLUE + u'Test' + Fore.RESET, '', 5, u'\x1b[34mTest\x1b[39m '),
    (colored(u'Test', 'blue'), '', 5, u'\x1b[34mTest\x1b[0m '),
    (u'蓝色', '', 5, u'蓝色 '),
    (u'שלום', '', 5, u'\u05e9\u05dc\u05d5\u05dd '),
    (u'معرب', '', 5, u'\u0645\u0639\u0631\u0628 '),

    (u'test', 'left', 5, u'test '),
    (Color(u'{blue}Test{/blue}'), 'left', 5, u'\x1b[34mTest\x1b[39m '),
    (Fore.BLUE + u'Test' + Fore.RESET, 'left', 5, u'\x1b[34mTest\x1b[39m '),
    (colored(u'Test', 'blue'), 'left', 5, u'\x1b[34mTest\x1b[0m '),
    (u'蓝色', 'left', 5, u'蓝色 '),
    (u'שלום', 'left', 5, u'\u05e9\u05dc\u05d5\u05dd '),
    (u'معرب', 'left', 5, u'\u0645\u0639\u0631\u0628 '),

    (u'test', 'right', 5, u' test'),
    (Color(u'{blue}Test{/blue}'), 'right', 5, u' \x1b[34mTest\x1b[39m'),
    (Fore.BLUE + u'Test' + Fore.RESET, 'right', 5, u' \x1b[34mTest\x1b[39m'),
    (colored(u'Test', 'blue'), 'right', 5, u' \x1b[34mTest\x1b[0m'),
    (u'蓝色', 'right', 5, u' 蓝色'),
    (u'שלום', 'right', 5, u' \u05e9\u05dc\u05d5\u05dd'),
    (u'معرب', 'right', 5, u' \u0645\u0639\u0631\u0628'),

    (u'test', 'center', 6, u' test '),
    (Color(u'{blue}Test{/blue}'), 'center', 6, u' \x1b[34mTest\x1b[39m '),
    (Fore.BLUE + u'Test' + Fore.RESET, 'center', 6, u' \x1b[34mTest\x1b[39m '),
    (colored(u'Test', 'blue'), 'center', 6, u' \x1b[34mTest\x1b[0m '),
    (u'蓝色', 'center', 6, u' 蓝色 '),
    (u'שלום', 'center', 6, u' \u05e9\u05dc\u05d5\u05dd '),
    (u'معرب', 'center', 6, u' \u0645\u0639\u0631\u0628 '),
])
def test_width(string, align, width, expected):
    """Test width and horizontal alignment.

    :param str string: String to test.
    :param str align: Horizontal alignment.
    :param int width: Expand string to this width without padding.
    :param str expected: Expected output string.
    """
    actual = align_and_pad_cell(string, (align,), (width, 1), (0, 0, 0, 0))
    assert actual == expected


@pytest.mark.parametrize('string,align,height,expected', [
    (u'test', '', 1, u'test'),
    (Color(u'{blue}Test{/blue}'), '', 1, u'\x1b[34mTest\x1b[39m'),
    (Fore.BLUE + u'Test' + Fore.RESET, '', 1, u'\x1b[34mTest\x1b[39m'),
    (colored(u'Test', 'blue'), '', 1, u'\x1b[34mTest\x1b[0m'),
    (u'蓝色', '', 1, u'蓝色'),
    (u'שלום', '', 1, u'\u05e9\u05dc\u05d5\u05dd'),
    (u'معرب', '', 1, u'\u0645\u0639\u0631\u0628'),

    (u'test', '', 2, u'test\n    '),
    (Color(u'{blue}Test{/blue}'), '', 2, u'\x1b[34mTest\x1b[39m\n    '),
    (Fore.BLUE + u'Test' + Fore.RESET, '', 2, u'\x1b[34mTest\x1b[39m\n    '),
    (colored(u'Test', 'blue'), '', 2, u'\x1b[34mTest\x1b[0m\n    '),
    (u'蓝色', '', 2, u'蓝色\n    '),
    (u'שלום', '', 2, u'\u05e9\u05dc\u05d5\u05dd\n    '),
    (u'معرب', '', 2, u'\u0645\u0639\u0631\u0628\n    '),

    (u'test', 'top', 2, u'test\n    '),
    (Color(u'{blue}Test{/blue}'), 'top', 2, u'\x1b[34mTest\x1b[39m\n    '),
    (Fore.BLUE + u'Test' + Fore.RESET, 'top', 2, u'\x1b[34mTest\x1b[39m\n    '),
    (colored(u'Test', 'blue'), 'top', 2, u'\x1b[34mTest\x1b[0m\n    '),
    (u'蓝色', 'top', 2, u'蓝色\n    '),
    (u'שלום', 'top', 2, u'\u05e9\u05dc\u05d5\u05dd\n    '),
    (u'معرب', 'top', 2, u'\u0645\u0639\u0631\u0628\n    '),

    (u'test', 'bottom', 2, u'    \ntest'),
    (Color(u'{blue}Test{/blue}'), 'bottom', 2, u'    \n\x1b[34mTest\x1b[39m'),
    (Fore.BLUE + u'Test' + Fore.RESET, 'bottom', 2, u'    \n\x1b[34mTest\x1b[39m'),
    (colored(u'Test', 'blue'), 'bottom', 2, u'    \n\x1b[34mTest\x1b[0m'),
    (u'蓝色', 'bottom', 2, u'    \n蓝色'),
    (u'שלום', 'bottom', 2, u'    \n\u05e9\u05dc\u05d5\u05dd'),
    (u'معرب', 'bottom', 2, u'    \n\u0645\u0639\u0631\u0628'),

    (u'test', 'middle', 3, u'    \ntest\n    '),
    (Color(u'{blue}Test{/blue}'), 'middle', 3, u'    \n\x1b[34mTest\x1b[39m\n    '),
    (Fore.BLUE + u'Test' + Fore.RESET, 'middle', 3, u'    \n\x1b[34mTest\x1b[39m\n    '),
    (colored(u'Test', 'blue'), 'middle', 3, u'    \n\x1b[34mTest\x1b[0m\n    '),
    (u'蓝色', 'middle', 3, u'    \n蓝色\n    '),
    (u'שלום', 'middle', 3, u'    \n\u05e9\u05dc\u05d5\u05dd\n    '),
    (u'معرب', 'middle', 3, u'    \n\u0645\u0639\u0631\u0628\n    '),
])
def test_height(string, align, height, expected):
    """Test height and vertical alignment.

    :param str string: String to test.
    :param str align: Horizontal alignment.
    :param int height: Expand string to this height without padding.
    :param str expected: Expected output string.
    """
    actual = align_and_pad_cell(string, (align,), (4, height), (0, 0, 0, 0))
    assert actual == expected


@pytest.mark.parametrize('string,align,expected', [
    (u'', '', u'.......\n.......\n.......\n.......\n.......'),
    (u'\n', '', u'.......\n.......\n.......\n.......\n.......'),
    (u'a\nb\nc', '', u'.......\n.a.....\n.b.....\n.c.....\n.......'),
    (u'test', '', u'.......\n.test..\n.......\n.......\n.......'),

    (u'', 'left', u'.......\n.......\n.......\n.......\n.......'),
    (u'\n', 'left', u'.......\n.......\n.......\n.......\n.......'),
    (u'a\nb\nc', 'left', u'.......\n.a.....\n.b.....\n.c.....\n.......'),
    (u'test', 'left', u'.......\n.test..\n.......\n.......\n.......'),

    (u'', 'right', u'.......\n.......\n.......\n.......\n.......'),
    (u'\n', 'right', u'.......\n.......\n.......\n.......\n.......'),
    (u'a\nb\nc', 'right', u'.......\n.....a.\n.....b.\n.....c.\n.......'),
    (u'test', 'right', u'.......\n..test.\n.......\n.......\n.......'),

    (u'', 'center', u'.......\n.......\n.......\n.......\n.......'),
    (u'\n', 'center', u'.......\n.......\n.......\n.......\n.......'),
    (u'a\nb\nc', 'center', u'.......\n...a...\n...b...\n...c...\n.......'),
    (u'test', 'center', u'.......\n..test.\n.......\n.......\n.......'),

    (u'', 'top', u'.......\n.......\n.......\n.......\n.......'),
    (u'\n', 'top', u'.......\n.......\n.......\n.......\n.......'),
    (u'a\nb\nc', 'top', u'.......\n.a.....\n.b.....\n.c.....\n.......'),
    (u'test', 'top', u'.......\n.test..\n.......\n.......\n.......'),

    (u'', 'bottom', u'.......\n.......\n.......\n.......\n.......'),
    (u'\n', 'bottom', u'.......\n.......\n.......\n.......\n.......'),
    (u'a\nb\nc', 'bottom', u'.......\n.a.....\n.b.....\n.c.....\n.......'),
    (u'test', 'bottom', u'.......\n.......\n.......\n.test..\n.......'),

    (u'', 'middle', u'.......\n.......\n.......\n.......\n.......'),
    (u'\n', 'middle', u'.......\n.......\n.......\n.......\n.......'),
    (u'a\nb\nc', 'middle', u'.......\n.a.....\n.b.....\n.c.....\n.......'),
    (u'test', 'middle', u'.......\n.......\n.test..\n.......\n.......'),

    (u'蓝色\nשלום\nمعرب', '', u'.......\n.蓝色..\n.\u05e9\u05dc\u05d5\u05dd..\n.\u0645\u0639\u0631\u0628..\n.......'),

    ('\n'.join((Color(u'{blue}Test{/blue}'), Fore.BLUE + u'Test' + Fore.RESET, colored(u'Test', 'blue'))), '',
     u'.......\n.\x1b[34mTest\x1b[39m..\n.\x1b[34mTest\x1b[39m..\n.\x1b[34mTest\x1b[0m..\n.......'),

    # (Color(u'{blue}A\nB{/blue}'), '', u'.......\n.\x1b[34mA\x1b[39m.....\n.\x1b[34mB\x1b[39m.....\n.......\n.......'),

])
def test_odd_width_height_pad_space(string, align, expected):
    """Test odd number width, height, padding, and dots for whitespaces.

    :param str string: String to test.
    :param str align: Alignment in any dimension but one at a time.
    :param str expected: Expected output string.
    """
    actual = align_and_pad_cell(string, (align,), (5, 3), (1, 1, 1, 1), '.')
    assert actual == expected
