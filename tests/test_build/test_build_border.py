# coding: utf-8
"""Test function in module."""

import pytest
from colorama import Fore, Style
from colorclass import Color
from termcolor import colored

from terminaltables.build import build_border


@pytest.mark.parametrize('column_widths,horizontal,left,intersect,right,expected', [
    ([5, 6, 7], '-', '<', '+', '>', '<-----+------+------->'),
    ([1, 1, 1], '-', '', '', '', '---'),
    ([1, 1, 1], '', '', '', '', ''),
    ([1], '-', '<', '+', '>', '<->'),
    ([], '-', '<', '+', '>', '<>'),
])
def test_no_title(column_widths, horizontal, left, intersect, right, expected):
    """Test without title.

    :param iter column_widths: List of integers representing column widths.
    :param str horizontal: Character to stretch across each column.
    :param str left: Left border.
    :param str intersect: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    actual = build_border(column_widths, horizontal, left, intersect, right)
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,intersect,expected', [
    ([20], '+', 'Applications--------'),
    ([20], '', 'Applications--------'),

    ([15, 5], '+', 'Applications---+-----'),
    ([15, 5], '', 'Applications--------'),

    ([12], '+', 'Applications'),
    ([12], '', 'Applications'),

    ([12, 1], '+', 'Applications+-'),
    ([12, 1], '', 'Applications-'),

    ([12, 0], '+', 'Applications+'),
    ([12, 0], '', 'Applications'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_first_column_fit(column_widths, left, intersect, right, expected):
    """Test with title that fits in the first column.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str intersect: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, intersect, right, title='Applications')
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,expected', [
    ([20], 'Applications--------'),
    ([10, 10], 'Applications--------'),
    ([5, 5, 5, 5], 'Applications--------'),
    ([3, 2, 3, 2, 3, 2, 3, 2], 'Applications--------'),
    ([1] * 20, 'Applications--------'),
    ([10, 5], 'Applications---'),
    ([9, 5], 'Applications--'),
    ([8, 5], 'Applications-'),
    ([7, 5], 'Applications'),
    ([6, 5], '-----------'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_no_intersect(column_widths, left, right, expected):
    """Test with no column dividers.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, '', right, title='Applications')
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,expected', [
    ([20], 'Applications--------'),
    ([0, 20], 'Applications---------'),
    ([20, 0], 'Applications--------+'),
    ([0, 0, 20], 'Applications----------'),
    ([20, 0, 0], 'Applications--------++'),

    ([10, 10], 'Applications---------'),
    ([11, 9], 'Applications---------'),
    ([12, 8], 'Applications+--------'),
    ([13, 7], 'Applications-+-------'),

    ([5, 5, 5, 5], 'Applications-----+-----'),
    ([4, 4, 6, 6], 'Applications----+------'),
    ([3, 3, 7, 7], 'Applications---+-------'),
    ([2, 2, 7, 9], 'Applications-+---------'),
    ([1, 1, 9, 9], 'Applications-+---------'),

    ([2, 2, 2, 2, 2, 2, 2], 'Applications--+--+--'),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'Applications-+-+-+-'),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Applications++++++++'),

    ([2, 2, 2, 2], '--+--+--+--'),
    ([1, 1, 1, 1, 1], '-+-+-+-+-'),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], '+++++++++'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_intersect(column_widths, left, right, expected):
    """Test with column dividers.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, '+', right, title='Applications')
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,intersect,expected', [
    ([12], '+', u'蓝色--------'),
    ([12], '', u'蓝色--------'),
    ([7, 5], '+', u'蓝色---+-----'),
    ([7, 5], '', u'蓝色--------'),
    ([4], '+', u'蓝色'),
    ([4], '', u'蓝色'),
    ([4, 1], '+', u'蓝色+-'),
    ([4, 1], '', u'蓝色-'),
    ([4, 0], '+', u'蓝色+'),
    ([4, 0], '', u'蓝色'),
    ([12], '', u'蓝色--------'),
    ([6, 6], '', u'蓝色--------'),
    ([3, 3, 3, 3], '', u'蓝色--------'),
    ([2, 1, 2, 1, 2, 1, 2, 1], '', u'蓝色--------'),
    ([1] * 12, '', u'蓝色--------'),
    ([2, 4], '', u'蓝色--'),
    ([1, 4], '', u'蓝色-'),
    ([1, 3], '', u'蓝色'),
    ([1, 2], '', u'---'),
    ([2], '', u'--'),
    ([12], '+', u'蓝色--------'),
    ([0, 12], '+', u'蓝色---------'),
    ([12, 0], '+', u'蓝色--------+'),
    ([0, 0, 12], '+', u'蓝色----------'),
    ([12, 0, 0], '+', u'蓝色--------++'),
    ([3, 3], '+', u'蓝色---'),
    ([4, 2], '+', u'蓝色+--'),
    ([5, 1], '+', u'蓝色-+-'),
    ([3, 3, 3, 3], '+', u'蓝色---+---+---'),
    ([2, 2, 4, 4], '+', u'蓝色-+----+----'),
    ([1, 1, 5, 5], '+', u'蓝色-----+-----'),
    ([2, 2, 2, 2], '+', u'蓝色-+--+--'),
    ([1, 1, 1, 1, 1], '+', u'蓝色-+-+-'),
    ([0, 0, 0, 0, 0, 0, 0], '+', u'蓝色++'),
    ([1, 1], '+', u'-+-'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_cjk(column_widths, left, intersect, right, expected):
    """Test with CJK characters in title.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str intersect: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, intersect, right, title=u'蓝色')
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,intersect,expected', [
    ([12], '+', u'معرب--------'),
    ([12], '', u'معرب--------'),
    ([7, 5], '+', u'معرب---+-----'),
    ([7, 5], '', u'معرب--------'),
    ([4], '+', u'معرب'),
    ([4], '', u'معرب'),
    ([4, 1], '+', u'معرب+-'),
    ([4, 1], '', u'معرب-'),
    ([4, 0], '+', u'معرب+'),
    ([4, 0], '', u'معرب'),
    ([12], '', u'معرب--------'),
    ([6, 6], '', u'معرب--------'),
    ([3, 3, 3, 3], '', u'معرب--------'),
    ([2, 1, 2, 1, 2, 1, 2, 1], '', u'معرب--------'),
    ([1] * 12, '', u'معرب--------'),
    ([2, 4], '', u'معرب--'),
    ([1, 4], '', u'معرب-'),
    ([1, 3], '', u'معرب'),
    ([1, 2], '', u'---'),
    ([2], '', u'--'),
    ([12], '+', u'معرب--------'),
    ([0, 12], '+', u'معرب---------'),
    ([12, 0], '+', u'معرب--------+'),
    ([0, 0, 12], '+', u'معرب----------'),
    ([12, 0, 0], '+', u'معرب--------++'),
    ([3, 3], '+', u'معرب---'),
    ([4, 2], '+', u'معرب+--'),
    ([5, 1], '+', u'معرب-+-'),
    ([3, 3, 3, 3], '+', u'معرب---+---+---'),
    ([2, 2, 4, 4], '+', u'معرب-+----+----'),
    ([1, 1, 5, 5], '+', u'معرب-----+-----'),
    ([2, 2, 2, 2], '+', u'معرب-+--+--'),
    ([1, 1, 1, 1, 1], '+', u'معرب-+-+-'),
    ([0, 0, 0, 0, 0, 0, 0], '+', u'معرب++'),
    ([1, 1], '+', u'-+-'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_rtl(column_widths, left, intersect, right, expected):
    """Test with RTL characters in title.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str intersect: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, intersect, right, title=u'معرب')
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,intersect,expected', [
    ([12], '+', '\x1b[34mTEST\x1b[0m--------'),
    ([12], '', '\x1b[34mTEST\x1b[0m--------'),
    ([7, 5], '+', '\x1b[34mTEST\x1b[0m---+-----'),
    ([7, 5], '', '\x1b[34mTEST\x1b[0m--------'),
    ([4], '+', '\x1b[34mTEST\x1b[0m'),
    ([4], '', '\x1b[34mTEST\x1b[0m'),
    ([4, 1], '+', '\x1b[34mTEST\x1b[0m+-'),
    ([4, 1], '', '\x1b[34mTEST\x1b[0m-'),
    ([4, 0], '+', '\x1b[34mTEST\x1b[0m+'),
    ([4, 0], '', '\x1b[34mTEST\x1b[0m'),
    ([12], '', '\x1b[34mTEST\x1b[0m--------'),
    ([6, 6], '', '\x1b[34mTEST\x1b[0m--------'),
    ([3, 3, 3, 3], '', '\x1b[34mTEST\x1b[0m--------'),
    ([2, 1, 2, 1, 2, 1, 2, 1], '', '\x1b[34mTEST\x1b[0m--------'),
    ([1] * 12, '', '\x1b[34mTEST\x1b[0m--------'),
    ([2, 4], '', '\x1b[34mTEST\x1b[0m--'),
    ([1, 4], '', '\x1b[34mTEST\x1b[0m-'),
    ([1, 3], '', '\x1b[34mTEST\x1b[0m'),
    ([1, 2], '', '---'),
    ([12], '+', '\x1b[34mTEST\x1b[0m--------'),
    ([0, 12], '+', '\x1b[34mTEST\x1b[0m---------'),
    ([12, 0], '+', '\x1b[34mTEST\x1b[0m--------+'),
    ([0, 0, 12], '+', '\x1b[34mTEST\x1b[0m----------'),
    ([12, 0, 0], '+', '\x1b[34mTEST\x1b[0m--------++'),
    ([3, 3], '+', '\x1b[34mTEST\x1b[0m---'),
    ([4, 2], '+', '\x1b[34mTEST\x1b[0m+--'),
    ([5, 1], '+', '\x1b[34mTEST\x1b[0m-+-'),
    ([3, 3, 3, 3], '+', '\x1b[34mTEST\x1b[0m---+---+---'),
    ([2, 2, 4, 4], '+', '\x1b[34mTEST\x1b[0m-+----+----'),
    ([1, 1, 5, 5], '+', '\x1b[34mTEST\x1b[0m-----+-----'),
    ([2, 2, 2, 2], '+', '\x1b[34mTEST\x1b[0m-+--+--'),
    ([1, 1, 1, 1, 1], '+', '\x1b[34mTEST\x1b[0m-+-+-'),
    ([0, 0, 0, 0, 0, 0, 0], '+', '\x1b[34mTEST\x1b[0m++'),
    ([1, 1], '+', '-+-'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
@pytest.mark.parametrize('title', [
    '\x1b[34mTEST\x1b[0m',
    Color('{blue}TEST{/all}'),
    Fore.BLUE + 'TEST' + Style.RESET_ALL,
    colored('TEST', 'blue'),
])
def test_colors(column_widths, left, intersect, right, title, expected):
    """Test with color title characters.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str intersect: Column separator.
    :param str right: Right border.
    :param title: Title in border with color codes.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, intersect, right, title=title)
    assert ''.join(actual) == expected
