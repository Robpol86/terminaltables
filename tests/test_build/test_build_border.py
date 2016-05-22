# coding: utf-8
"""Test function in module."""

import pytest

from terminaltables.build import build_border


@pytest.mark.parametrize('column_widths,horizontal,left,intersect,right,expected', [
    ([5, 6, 7], '-', '<', '+', '>', '<-----+------+------->'),
    ([1, 1, 1], '-', '', '', '', '---'),
    ([1, 1, 1], '', '', '', '', ''),
    ([1], '-', '<', '+', '>', '<->'),
    ([], '-', '<', '+', '>', '<>'),
])
def test(column_widths, horizontal, left, intersect, right, expected):
    """Test function.

    :param iter column_widths: List of integers representing column widths.
    :param str horizontal: Character to stretch across each column.
    :param str left: Left border.
    :param str intersect: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    actual = build_border(column_widths, horizontal, left, intersect, right)
    assert ''.join(actual) == expected
