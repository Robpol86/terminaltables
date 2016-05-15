# coding: utf-8
"""Test function in module."""

import pytest
from colorama import Fore
from colorclass import Color
from termcolor import colored

from terminaltables.width_and_alignment import align_and_pad_cell


@pytest.mark.parametrize('string,align,width,expected', [
    ('test', '', 4, 'test'),
    (Color('{blue}Test{/blue}'), '', 4, '\x1b[34mTest\x1b[39m'),
    (Fore.BLUE + 'Test' + Fore.RESET, '', 4, '\x1b[34mTest\x1b[39m'),
    (colored('Test', 'blue'), '', 4, '\x1b[34mTest\x1b[0m'),
    ('蓝色', '', 4, '蓝色'),
    (u'שלום', '', 4, u'\u05e9\u05dc\u05d5\u05dd'),
    (u'معرب', '', 4, u'\u0645\u0639\u0631\u0628'),

    ('test', '', 5, 'test '),
    (Color('{blue}Test{/blue}'), '', 5, '\x1b[34mTest\x1b[39m '),
    (Fore.BLUE + 'Test' + Fore.RESET, '', 5, '\x1b[34mTest\x1b[39m '),
    (colored('Test', 'blue'), '', 5, '\x1b[34mTest\x1b[0m '),
    ('蓝色', '', 5, '蓝色 '),
    (u'שלום', '', 5, u'\u05e9\u05dc\u05d5\u05dd '),
    (u'معرب', '', 5, u'\u0645\u0639\u0631\u0628 '),

    ('test', 'left', 5, 'test '),
    (Color('{blue}Test{/blue}'), 'left', 5, '\x1b[34mTest\x1b[39m '),
    (Fore.BLUE + 'Test' + Fore.RESET, 'left', 5, '\x1b[34mTest\x1b[39m '),
    (colored('Test', 'blue'), 'left', 5, '\x1b[34mTest\x1b[0m '),
    ('蓝色', 'left', 5, '蓝色 '),
    (u'שלום', 'left', 5, u'\u05e9\u05dc\u05d5\u05dd '),
    (u'معرب', 'left', 5, u'\u0645\u0639\u0631\u0628 '),

    ('test', 'right', 5, ' test'),
    (Color('{blue}Test{/blue}'), 'right', 5, ' \x1b[34mTest\x1b[39m'),
    (Fore.BLUE + 'Test' + Fore.RESET, 'right', 5, ' \x1b[34mTest\x1b[39m'),
    (colored('Test', 'blue'), 'right', 5, ' \x1b[34mTest\x1b[0m'),
    ('蓝色', 'right', 5, ' 蓝色'),
    (u'שלום', 'right', 5, u' \u05e9\u05dc\u05d5\u05dd'),
    (u'معرب', 'right', 5, u' \u0645\u0639\u0631\u0628'),

    ('test', 'center', 6, ' test '),
    (Color('{blue}Test{/blue}'), 'center', 6, ' \x1b[34mTest\x1b[39m '),
    (Fore.BLUE + 'Test' + Fore.RESET, 'center', 6, ' \x1b[34mTest\x1b[39m '),
    (colored('Test', 'blue'), 'center', 6, ' \x1b[34mTest\x1b[0m '),
    ('蓝色', 'center', 6, ' 蓝色 '),
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
    ('test', '', 1, 'test'),
    (Color('{blue}Test{/blue}'), '', 1, '\x1b[34mTest\x1b[39m'),
    (Fore.BLUE + 'Test' + Fore.RESET, '', 1, '\x1b[34mTest\x1b[39m'),
    (colored('Test', 'blue'), '', 1, '\x1b[34mTest\x1b[0m'),
    ('蓝色', '', 1, '蓝色'),
    (u'שלום', '', 1, u'\u05e9\u05dc\u05d5\u05dd'),
    (u'معرب', '', 1, u'\u0645\u0639\u0631\u0628'),

    ('test', '', 2, 'test\n    '),
    (Color('{blue}Test{/blue}'), '', 2, '\x1b[34mTest\x1b[39m\n    '),
    (Fore.BLUE + 'Test' + Fore.RESET, '', 2, '\x1b[34mTest\x1b[39m\n    '),
    (colored('Test', 'blue'), '', 2, '\x1b[34mTest\x1b[0m\n    '),
    ('蓝色', '', 2, '蓝色\n    '),
    (u'שלום', '', 2, u'\u05e9\u05dc\u05d5\u05dd\n    '),
    (u'معرب', '', 2, u'\u0645\u0639\u0631\u0628\n    '),

    ('test', 'top', 2, 'test\n    '),
    (Color('{blue}Test{/blue}'), 'top', 2, '\x1b[34mTest\x1b[39m\n    '),
    (Fore.BLUE + 'Test' + Fore.RESET, 'top', 2, '\x1b[34mTest\x1b[39m\n    '),
    (colored('Test', 'blue'), 'top', 2, '\x1b[34mTest\x1b[0m\n    '),
    ('蓝色', 'top', 2, '蓝色\n    '),
    (u'שלום', 'top', 2, u'\u05e9\u05dc\u05d5\u05dd\n    '),
    (u'معرب', 'top', 2, u'\u0645\u0639\u0631\u0628\n    '),

    ('test', 'bottom', 2, '    \ntest'),
    (Color('{blue}Test{/blue}'), 'bottom', 2, '    \n\x1b[34mTest\x1b[39m'),
    (Fore.BLUE + 'Test' + Fore.RESET, 'bottom', 2, '    \n\x1b[34mTest\x1b[39m'),
    (colored('Test', 'blue'), 'bottom', 2, '    \n\x1b[34mTest\x1b[0m'),
    ('蓝色', 'bottom', 2, '    \n蓝色'),
    (u'שלום', 'bottom', 2, u'    \n\u05e9\u05dc\u05d5\u05dd'),
    (u'معرب', 'bottom', 2, u'    \n\u0645\u0639\u0631\u0628'),

    ('test', 'middle', 3, '    \ntest\n    '),
    (Color('{blue}Test{/blue}'), 'middle', 3, '    \n\x1b[34mTest\x1b[39m\n    '),
    (Fore.BLUE + 'Test' + Fore.RESET, 'middle', 3, '    \n\x1b[34mTest\x1b[39m\n    '),
    (colored('Test', 'blue'), 'middle', 3, '    \n\x1b[34mTest\x1b[0m\n    '),
    ('蓝色', 'middle', 3, '    \n蓝色\n    '),
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
    ('', '', '.......\n.......\n.......\n.......\n.......'),
    ('\n', '', '.......\n.......\n.......\n.......\n.......'),
    ('a\nb\nc', '', '.......\n.a.....\n.b.....\n.c.....\n.......'),
    ('test', '', '.......\n.test..\n.......\n.......\n.......'),

    ('', 'left', '.......\n.......\n.......\n.......\n.......'),
    ('\n', 'left', '.......\n.......\n.......\n.......\n.......'),
    ('a\nb\nc', 'left', '.......\n.a.....\n.b.....\n.c.....\n.......'),
    ('test', 'left', '.......\n.test..\n.......\n.......\n.......'),

    ('', 'right', '.......\n.......\n.......\n.......\n.......'),
    ('\n', 'right', '.......\n.......\n.......\n.......\n.......'),
    ('a\nb\nc', 'right', '.......\n.....a.\n.....b.\n.....c.\n.......'),
    ('test', 'right', '.......\n..test.\n.......\n.......\n.......'),

    ('', 'center', '.......\n.......\n.......\n.......\n.......'),
    ('\n', 'center', '.......\n.......\n.......\n.......\n.......'),
    ('a\nb\nc', 'center', '.......\n...a...\n...b...\n...c...\n.......'),
    ('test', 'center', '.......\n..test.\n.......\n.......\n.......'),

    ('', 'top', '.......\n.......\n.......\n.......\n.......'),
    ('\n', 'top', '.......\n.......\n.......\n.......\n.......'),
    ('a\nb\nc', 'top', '.......\n.a.....\n.b.....\n.c.....\n.......'),
    ('test', 'top', '.......\n.test..\n.......\n.......\n.......'),

    ('', 'bottom', '.......\n.......\n.......\n.......\n.......'),
    ('\n', 'bottom', '.......\n.......\n.......\n.......\n.......'),
    ('a\nb\nc', 'bottom', '.......\n.a.....\n.b.....\n.c.....\n.......'),
    ('test', 'bottom', '.......\n.......\n.......\n.test..\n.......'),

    ('', 'middle', '.......\n.......\n.......\n.......\n.......'),
    ('\n', 'middle', '.......\n.......\n.......\n.......\n.......'),
    ('a\nb\nc', 'middle', '.......\n.a.....\n.b.....\n.c.....\n.......'),
    ('test', 'middle', '.......\n.......\n.test..\n.......\n.......'),

    (u'蓝色\nשלום\nمعرب', '', u'.......\n.蓝色..\n.\u05e9\u05dc\u05d5\u05dd..\n.\u0645\u0639\u0631\u0628..\n.......'),

    ('\n'.join((Color('{blue}Test{/blue}'), Fore.BLUE + 'Test' + Fore.RESET, colored('Test', 'blue'))), '',
     '.......\n.\x1b[34mTest\x1b[39m..\n.\x1b[34mTest\x1b[39m..\n.\x1b[34mTest\x1b[0m..\n.......'),

    # (Color('{blue}A\nB{/blue}'), '', '.......\n.\x1b[34mA\x1b[39m.....\n.\x1b[34mB\x1b[39m.....\n.......\n.......'),

])
def test_odd_width_height_pad_space(string, align, expected):
    """Test odd number width, height, padding, and dots for whitespaces.

    :param str string: String to test.
    :param str align: Alignment in any dimension but one at a time.
    :param str expected: Expected output string.
    """
    actual = align_and_pad_cell(string, (align,), (5, 3), (1, 1, 1, 1), '.')
    assert actual == expected
