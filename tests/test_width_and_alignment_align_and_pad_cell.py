# coding: utf-8
"""Tests for character length calculating."""

from terminaltables.width_and_alignment import align_and_pad_cell


def test_align():
    """Test alignment/justifications."""
    assert align_and_pad_cell('test', '', (1, 1, 0, 0)) == 'test'
    assert align_and_pad_cell('test', 'left', (1, 1, 0, 0)) == 'test'
    assert align_and_pad_cell('', 'left', (4, 1, 0, 0)) == '    '
    assert align_and_pad_cell('', 'left', (0, 1, 0, 0)) == ''
    assert align_and_pad_cell('', 'left', (0, 1, 1, 1)) == '  '
    assert align_and_pad_cell('', 'left', (1, 1, 1, 1)) == '   '
    assert align_and_pad_cell('', 'left', (4, 1, 1, 1)) == '      '

    assert align_and_pad_cell('test', 'left', (4, 1, 0, 0)) == 'test'
    assert align_and_pad_cell('test', 'left', (5, 1, 0, 0)) == 'test '
    assert align_and_pad_cell('test', 'left', (6, 1, 0, 0)) == 'test  '
    assert align_and_pad_cell('test', 'left', (7, 1, 0, 0)) == 'test   '
    assert align_and_pad_cell(' test', 'left', (7, 1, 0, 0)) == ' test  '

    assert align_and_pad_cell('test', 'right', (1, 1, 0, 0)) == 'test'
    assert align_and_pad_cell('test', 'right', (4, 1, 0, 0)) == 'test'
    assert align_and_pad_cell('test', 'right', (5, 1, 0, 0)) == ' test'
    assert align_and_pad_cell('test', 'right', (6, 1, 0, 0)) == '  test'
    assert align_and_pad_cell('test', 'right', (7, 1, 0, 0)) == '   test'

    assert align_and_pad_cell('test', 'center', (1, 1, 0, 0)) == 'test'
    assert align_and_pad_cell('test', 'center', (4, 1, 0, 0)) == 'test'
    assert align_and_pad_cell('test', 'center', (5, 1, 0, 0)) == ' test'
    assert align_and_pad_cell('test', 'center', (6, 1, 0, 0)) == ' test '
    assert align_and_pad_cell('test', 'center', (7, 1, 0, 0)) == '  test '


def test_padding():
    """Test padding."""
    assert align_and_pad_cell('test', 'left', (4, 1, 1, 0)) == ' test'
    assert align_and_pad_cell('test', 'left', (4, 1, 0, 1)) == 'test '
    assert align_and_pad_cell('test', 'left', (4, 1, 1, 1)) == ' test '


def test_multi_line():
    """Test multi-line support."""
    assert align_and_pad_cell('test\n', 'left', (8, 2, 1, 1)) == ' test     \n          '
    assert align_and_pad_cell('\ntest', 'left', (8, 2, 1, 1)) == '          \n test     '
    assert align_and_pad_cell('\ntest\n', 'left', (8, 3, 1, 1)) == '          \n test     \n          '


def test_multi_line_align_padding():
    """Test alignment and padding on multi-line cells."""
    assert align_and_pad_cell('test\ntest', 'left', (4, 2, 0, 0)) == 'test\ntest'
    assert align_and_pad_cell('test\ntest', 'left', (5, 2, 0, 0)) == 'test \ntest '
    assert align_and_pad_cell('test\ntest', 'left', (6, 2, 0, 0)) == 'test  \ntest  '
    assert align_and_pad_cell('test\ntest', 'left', (7, 2, 0, 0)) == 'test   \ntest   '
    assert align_and_pad_cell(' test\ntest', 'left', (7, 2, 0, 0)) == ' test  \ntest   '
    assert align_and_pad_cell(' test\n test', 'left', (7, 2, 0, 0)) == ' test  \n test  '

    assert align_and_pad_cell('test\ntest', 'right', (4, 2, 0, 0)) == 'test\ntest'
    assert align_and_pad_cell('test\ntest', 'right', (5, 2, 0, 0)) == ' test\n test'
    assert align_and_pad_cell('test\ntest', 'right', (6, 2, 0, 0)) == '  test\n  test'
    assert align_and_pad_cell('test\ntest', 'right', (7, 2, 0, 0)) == '   test\n   test'

    assert align_and_pad_cell('test\ntest', 'center', (4, 2, 0, 0)) == 'test\ntest'
    assert align_and_pad_cell('test\ntest', 'center', (5, 2, 0, 0)) == ' test\n test'
    assert align_and_pad_cell('test\ntest', 'center', (6, 2, 0, 0)) == ' test \n test '
    assert align_and_pad_cell('test\ntest', 'center', (7, 2, 0, 0)) == '  test \n  test '

    assert align_and_pad_cell('test\ntest', 'left', (4, 2, 1, 0)) == ' test\n test'
    assert align_and_pad_cell('test\ntest', 'left', (4, 2, 0, 1)) == 'test \ntest '
    assert align_and_pad_cell('test\ntest', 'left', (4, 2, 1, 1)) == ' test \n test '


def test_height():
    """Test height of multi-line cells."""
    assert align_and_pad_cell('test', 'left', (4, 2, 0, 0)) == 'test\n    '

    assert align_and_pad_cell('test\n', 'left', (4, 1, 0, 0)) == 'test\n    '
    assert align_and_pad_cell('test\n', 'left', (4, 2, 0, 0)) == 'test\n    '
    assert align_and_pad_cell('test\n', 'left', (4, 3, 0, 0)) == 'test\n    \n    '

    assert align_and_pad_cell('test\n', 'left', (4, 3, 1, 1)) == ' test \n      \n      '
