# coding: utf-8
"""Test function in module."""

import pytest
from colorama import Fore
from colorclass import Color
from termcolor import colored

from terminaltables.width_and_alignment import visible_width, SEPARATOR


@pytest.mark.parametrize('string,expected', [
    # str
    ('hello, world', 12),
    ('世界你好', 8),
    ('蓝色', 4),
    ('שלום', 4),
    ('معرب', 4),
    ('hello 世界', 10),

    # separator
    (SEPARATOR, 0),

    # str+ansi
    ('\x1b[34mhello, world\x1b[39m', 12),
    ('\x1b[34m世界你好\x1b[39m', 8),
    ('\x1b[34m蓝色\x1b[39m', 4),
    ('\x1b[34mשלום\x1b[39m', 4),
    ('\x1b[34mمعرب\x1b[39m', 4),
    ('\x1b[34mhello 世界\x1b[39m', 10),

    # colorclass
    (Color(u'{blue}hello, world{/blue}'), 12),
    (Color(u'{blue}世界你好{/blue}'), 8),
    (Color(u'{blue}蓝色{/blue}'), 4),
    (Color(u'{blue}שלום{/blue}'), 4),
    (Color(u'{blue}معرب{/blue}'), 4),
    (Color(u'{blue}hello 世界{/blue}'), 10),

    # colorama
    (Fore.BLUE + 'hello, world' + Fore.RESET, 12),
    (Fore.BLUE + '世界你好' + Fore.RESET, 8),
    (Fore.BLUE + '蓝色' + Fore.RESET, 4),
    (Fore.BLUE + 'שלום' + Fore.RESET, 4),
    (Fore.BLUE + 'معرب' + Fore.RESET, 4),
    (Fore.BLUE + 'hello 世界' + Fore.RESET, 10),

    # termcolor
    (colored('hello, world', 'blue'), 12),
    (colored('世界你好', 'blue'), 8),
    (colored('蓝色', 'blue'), 4),
    (colored('שלום', 'blue'), 4),
    (colored('معرب', 'blue'), 4),
    (colored('hello 世界', 'blue'), 10),
])
def test(string, expected):
    """Test function with different color libraries.

    :param str string: Input string to measure.
    :param int expected: Expected visible width of string (some characters are len() == 1 but take up 2 spaces).
    """
    assert visible_width(string) == expected
