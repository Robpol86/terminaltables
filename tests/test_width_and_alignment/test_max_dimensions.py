# coding: utf-8
"""Test function in module."""

import pytest
from colorama import Fore
from colorclass import Color
from termcolor import colored

from terminaltables.width_and_alignment import max_dimensions, SEPARATOR


@pytest.mark.parametrize('table_data,expected_w,expected_h', [
    ([[]], [], [0]),
    ([['']], [0], [0]),
    ([['', '']], [0, 0], [0]),

    ([[], []], [], [0, 0]),
    ([[''], ['']], [0], [0, 0]),
    ([['', ''], ['', '']], [0, 0], [0, 0]),
])
def test_zero_length(table_data, expected_w, expected_h):
    """Test zero-length or empty tables.

    :param list table_data: Input table data to test.
    :param list expected_w: Expected widths.
    :param list expected_h: Expected heights.
    """
    actual = max_dimensions(table_data)
    assert actual == (expected_w, expected_h, expected_w, expected_h)


def test_single_line():
    """Test widths."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    assert max_dimensions(table_data, 1, 1) == ([7, 5, 9], [1, 1, 1, 1], [9, 7, 11], [1, 1, 1, 1])

    table_data.append(['Watermelon', 'green', 'fruit'])
    assert max_dimensions(table_data, 2, 2) == ([10, 5, 9], [1, 1, 1, 1, 1], [14, 9, 13], [1, 1, 1, 1, 1])


def test_separator():
    """Test separator inside table"""
    table_data = [
        ['Name', 'Color', 'Type'],
        [SEPARATOR],
        ['Avocado', 'green', 'nut'],
    ]

    assert max_dimensions(table_data, 1, 1) == ([7, 5, 4], [1, 1, 1], [9, 7, 6], [1, 1, 1])


def test_multi_line():
    """Test heights."""
    table_data = [
        ['One\nTwo', 'Buckle\nMy\nShoe'],
    ]
    assert max_dimensions(table_data, 0, 0, 1, 1) == ([3, 6], [3], [3, 6], [5])

    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', ('Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\n'
                     'Susie Carmichael, Dil Pickles, Kimi Finster, Spike')],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    assert max_dimensions(table_data, 0, 0, 2, 2) == ([10, 83], [1, 2, 1], [10, 83], [5, 6, 5])


def test_trailing_newline():
    r"""Test with trailing \n."""
    table_data = [
        ['Row One\n<blank>'],
        ['<blank>\nRow Two'],
        ['Row Three\n'],
        ['\nRow Four'],
    ]
    assert max_dimensions(table_data) == ([9], [2, 2, 2, 2], [9], [2, 2, 2, 2])


def test_colors_cjk_rtl():
    """Test color text, CJK characters, and RTL characters."""
    table_data = [
        [Color('{blue}Test{/blue}')],
        [Fore.BLUE + 'Test' + Fore.RESET],
        [colored('Test', 'blue')],
    ]
    assert max_dimensions(table_data) == ([4], [1, 1, 1], [4], [1, 1, 1])

    table_data = [
        ['蓝色'],
        ['世界你好'],
    ]
    assert max_dimensions(table_data) == ([8], [1, 1], [8], [1, 1])

    table_data = [
        ['שלום'],
        ['معرب'],
    ]
    assert max_dimensions(table_data) == ([4], [1, 1], [4], [1, 1])


def test_non_string():
    """Test with non-string values."""
    table_data = [
        [123, 0.9, None, True, False],
    ]
    assert max_dimensions(table_data) == ([3, 3, 4, 4, 5], [1], [3, 3, 4, 4, 5], [1])
