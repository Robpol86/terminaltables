# coding: utf-8
"""Tests for character length calculating."""

import pytest
from colorclass import Color

from terminaltables.width_and_alignment import string_width


@pytest.mark.parametrize('string,expected_length', [
    ('hello, world', 12),
    ('世界你好', 8),
    ('蓝色', 4),
    ('hello 世界', 10),
    (Color(u'{autoblue}hello, world{/autoblue}'), 12),
    (Color(u'{autoblue}世界你好{/autoblue}'), 8),
    (Color(u'{autoblue}蓝色{/autoblue}'), 4),
    (Color(u'{autoblue}hello 世界{/autoblue}'), 10),
])
def test_string_width(string, expected_length):
    """Test characters width."""
    assert string_width(string) == expected_length
