"""Tests for in-cell text alignment and padding."""

from terminaltables import _align_and_pad


def test_align():
    """Test alignment/justifications."""
    assert 'test' == _align_and_pad('test', '', 1, 1, 0, 0)
    assert 'test' == _align_and_pad('test', 'left', 1, 1, 0, 0)
    assert '    ' == _align_and_pad('', 'left', 4, 1, 0, 0)
    assert '' == _align_and_pad('', 'left', 0, 1, 0, 0)
    assert '  ' == _align_and_pad('', 'left', 0, 1, 1, 1)
    assert '   ' == _align_and_pad('', 'left', 1, 1, 1, 1)
    assert '      ' == _align_and_pad('', 'left', 4, 1, 1, 1)

    assert 'test' == _align_and_pad('test', 'left', 4, 1, 0, 0)
    assert 'test ' == _align_and_pad('test', 'left', 5, 1, 0, 0)
    assert 'test  ' == _align_and_pad('test', 'left', 6, 1, 0, 0)
    assert 'test   ' == _align_and_pad('test', 'left', 7, 1, 0, 0)
    assert ' test  ' == _align_and_pad(' test', 'left', 7, 1, 0, 0)

    assert 'test' == _align_and_pad('test', 'right', 1, 1, 0, 0)
    assert 'test' == _align_and_pad('test', 'right', 4, 1, 0, 0)
    assert ' test' == _align_and_pad('test', 'right', 5, 1, 0, 0)
    assert '  test' == _align_and_pad('test', 'right', 6, 1, 0, 0)
    assert '   test' == _align_and_pad('test', 'right', 7, 1, 0, 0)

    assert 'test' == _align_and_pad('test', 'center', 1, 1, 0, 0)
    assert 'test' == _align_and_pad('test', 'center', 4, 1, 0, 0)
    assert ' test' == _align_and_pad('test', 'center', 5, 1, 0, 0)
    assert ' test ' == _align_and_pad('test', 'center', 6, 1, 0, 0)
    assert '  test ' == _align_and_pad('test', 'center', 7, 1, 0, 0)


def test_padding():
    """Test padding."""
    assert ' test' == _align_and_pad('test', 'left', 4, 1, 1, 0)
    assert 'test ' == _align_and_pad('test', 'left', 4, 1, 0, 1)
    assert ' test ' == _align_and_pad('test', 'left', 4, 1, 1, 1)


def test_multi_line():
    """Test multi-line support."""
    assert ' test     \n          ' == _align_and_pad('test\n', 'left', 8, 2, 1, 1)
    assert '          \n test     ' == _align_and_pad('\ntest', 'left', 8, 2, 1, 1)
    assert '          \n test     \n          ' == _align_and_pad('\ntest\n', 'left', 8, 3, 1, 1)


def test_multi_line_align_padding():
    """Test alignment and padding on multi-line cells."""
    assert 'test\ntest' == _align_and_pad('test\ntest', 'left', 4, 2, 0, 0)
    assert 'test \ntest ' == _align_and_pad('test\ntest', 'left', 5, 2, 0, 0)
    assert 'test  \ntest  ' == _align_and_pad('test\ntest', 'left', 6, 2, 0, 0)
    assert 'test   \ntest   ' == _align_and_pad('test\ntest', 'left', 7, 2, 0, 0)
    assert ' test  \ntest   ' == _align_and_pad(' test\ntest', 'left', 7, 2, 0, 0)
    assert ' test  \n test  ' == _align_and_pad(' test\n test', 'left', 7, 2, 0, 0)

    assert 'test\ntest' == _align_and_pad('test\ntest', 'right', 4, 2, 0, 0)
    assert ' test\n test' == _align_and_pad('test\ntest', 'right', 5, 2, 0, 0)
    assert '  test\n  test' == _align_and_pad('test\ntest', 'right', 6, 2, 0, 0)
    assert '   test\n   test' == _align_and_pad('test\ntest', 'right', 7, 2, 0, 0)

    assert 'test\ntest' == _align_and_pad('test\ntest', 'center', 4, 2, 0, 0)
    assert ' test\n test' == _align_and_pad('test\ntest', 'center', 5, 2, 0, 0)
    assert ' test \n test ' == _align_and_pad('test\ntest', 'center', 6, 2, 0, 0)
    assert '  test \n  test ' == _align_and_pad('test\ntest', 'center', 7, 2, 0, 0)

    assert ' test\n test' == _align_and_pad('test\ntest', 'left', 4, 2, 1, 0)
    assert 'test \ntest ' == _align_and_pad('test\ntest', 'left', 4, 2, 0, 1)
    assert ' test \n test ' == _align_and_pad('test\ntest', 'left', 4, 2, 1, 1)


def test_height():
    """Test height of multi-line cells."""
    assert 'test\n    ' == _align_and_pad('test', 'left', 4, 2, 0, 0)

    assert 'test\n    ' == _align_and_pad('test\n', 'left', 4, 1, 0, 0)
    assert 'test\n    ' == _align_and_pad('test\n', 'left', 4, 2, 0, 0)
    assert 'test\n    \n    ' == _align_and_pad('test\n', 'left', 4, 3, 0, 0)

    assert ' test \n      \n      ' == _align_and_pad('test\n', 'left', 4, 3, 1, 1)
