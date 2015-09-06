# coding: utf-8
"""Tests for character length calculating."""

import pytest
from colorclass import Color

from terminaltables.width_and_alignment import align_and_pad_cell, string_width


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


def test_align():
    """Test alignment/justifications."""
    assert 'test' == align_and_pad_cell('test', '', 1, 1, 0, 0)
    assert 'test' == align_and_pad_cell('test', 'left', 1, 1, 0, 0)
    assert '    ' == align_and_pad_cell('', 'left', 4, 1, 0, 0)
    assert '' == align_and_pad_cell('', 'left', 0, 1, 0, 0)
    assert '  ' == align_and_pad_cell('', 'left', 0, 1, 1, 1)
    assert '   ' == align_and_pad_cell('', 'left', 1, 1, 1, 1)
    assert '      ' == align_and_pad_cell('', 'left', 4, 1, 1, 1)

    assert 'test' == align_and_pad_cell('test', 'left', 4, 1, 0, 0)
    assert 'test ' == align_and_pad_cell('test', 'left', 5, 1, 0, 0)
    assert 'test  ' == align_and_pad_cell('test', 'left', 6, 1, 0, 0)
    assert 'test   ' == align_and_pad_cell('test', 'left', 7, 1, 0, 0)
    assert ' test  ' == align_and_pad_cell(' test', 'left', 7, 1, 0, 0)

    assert 'test' == align_and_pad_cell('test', 'right', 1, 1, 0, 0)
    assert 'test' == align_and_pad_cell('test', 'right', 4, 1, 0, 0)
    assert ' test' == align_and_pad_cell('test', 'right', 5, 1, 0, 0)
    assert '  test' == align_and_pad_cell('test', 'right', 6, 1, 0, 0)
    assert '   test' == align_and_pad_cell('test', 'right', 7, 1, 0, 0)

    assert 'test' == align_and_pad_cell('test', 'center', 1, 1, 0, 0)
    assert 'test' == align_and_pad_cell('test', 'center', 4, 1, 0, 0)
    assert ' test' == align_and_pad_cell('test', 'center', 5, 1, 0, 0)
    assert ' test ' == align_and_pad_cell('test', 'center', 6, 1, 0, 0)
    assert '  test ' == align_and_pad_cell('test', 'center', 7, 1, 0, 0)


def test_padding():
    """Test padding."""
    assert ' test' == align_and_pad_cell('test', 'left', 4, 1, 1, 0)
    assert 'test ' == align_and_pad_cell('test', 'left', 4, 1, 0, 1)
    assert ' test ' == align_and_pad_cell('test', 'left', 4, 1, 1, 1)


def test_multi_line():
    """Test multi-line support."""
    assert ' test     \n          ' == align_and_pad_cell('test\n', 'left', 8, 2, 1, 1)
    assert '          \n test     ' == align_and_pad_cell('\ntest', 'left', 8, 2, 1, 1)
    assert '          \n test     \n          ' == align_and_pad_cell('\ntest\n', 'left', 8, 3, 1, 1)


def test_multi_line_align_padding():
    """Test alignment and padding on multi-line cells."""
    assert 'test\ntest' == align_and_pad_cell('test\ntest', 'left', 4, 2, 0, 0)
    assert 'test \ntest ' == align_and_pad_cell('test\ntest', 'left', 5, 2, 0, 0)
    assert 'test  \ntest  ' == align_and_pad_cell('test\ntest', 'left', 6, 2, 0, 0)
    assert 'test   \ntest   ' == align_and_pad_cell('test\ntest', 'left', 7, 2, 0, 0)
    assert ' test  \ntest   ' == align_and_pad_cell(' test\ntest', 'left', 7, 2, 0, 0)
    assert ' test  \n test  ' == align_and_pad_cell(' test\n test', 'left', 7, 2, 0, 0)

    assert 'test\ntest' == align_and_pad_cell('test\ntest', 'right', 4, 2, 0, 0)
    assert ' test\n test' == align_and_pad_cell('test\ntest', 'right', 5, 2, 0, 0)
    assert '  test\n  test' == align_and_pad_cell('test\ntest', 'right', 6, 2, 0, 0)
    assert '   test\n   test' == align_and_pad_cell('test\ntest', 'right', 7, 2, 0, 0)

    assert 'test\ntest' == align_and_pad_cell('test\ntest', 'center', 4, 2, 0, 0)
    assert ' test\n test' == align_and_pad_cell('test\ntest', 'center', 5, 2, 0, 0)
    assert ' test \n test ' == align_and_pad_cell('test\ntest', 'center', 6, 2, 0, 0)
    assert '  test \n  test ' == align_and_pad_cell('test\ntest', 'center', 7, 2, 0, 0)

    assert ' test\n test' == align_and_pad_cell('test\ntest', 'left', 4, 2, 1, 0)
    assert 'test \ntest ' == align_and_pad_cell('test\ntest', 'left', 4, 2, 0, 1)
    assert ' test \n test ' == align_and_pad_cell('test\ntest', 'left', 4, 2, 1, 1)


def test_height():
    """Test height of multi-line cells."""
    assert 'test\n    ' == align_and_pad_cell('test', 'left', 4, 2, 0, 0)

    assert 'test\n    ' == align_and_pad_cell('test\n', 'left', 4, 1, 0, 0)
    assert 'test\n    ' == align_and_pad_cell('test\n', 'left', 4, 2, 0, 0)
    assert 'test\n    \n    ' == align_and_pad_cell('test\n', 'left', 4, 3, 0, 0)

    assert ' test \n      \n      ' == align_and_pad_cell('test\n', 'left', 4, 3, 1, 1)
