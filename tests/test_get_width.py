# coding: utf-8
"""Tests for character length calculating."""

from colorclass import Color

from terminaltables import _get_width


def test_get_width():
    """Test characters width."""
    testcases = [
        ('hello, world', 12),
        ('世界你好', 8),
        ('hello 世界', 10),
        (Color(u'{autoblue}蓝色{/autoblue}'), 4),
    ]

    for string, expected_length in testcases:
        assert _get_width(string) == expected_length
