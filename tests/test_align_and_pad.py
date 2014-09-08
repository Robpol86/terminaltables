from terminaltables import _align_and_pad


def test_align():
    assert 'test' == _align_and_pad('test', '', 1, 0, 0)
    assert 'test' == _align_and_pad('test', 'left', 1, 0, 0)
    assert '    ' == _align_and_pad('', 'left', 4, 0, 0)

    assert 'test' == _align_and_pad('test', 'left', 4, 0, 0)
    assert 'test ' == _align_and_pad('test', 'left', 5, 0, 0)
    assert 'test  ' == _align_and_pad('test', 'left', 6, 0, 0)
    assert 'test   ' == _align_and_pad('test', 'left', 7, 0, 0)
    assert ' test  ' == _align_and_pad(' test', 'left', 7, 0, 0)

    assert 'test' == _align_and_pad('test', 'right', 1, 0, 0)
    assert 'test' == _align_and_pad('test', 'right', 4, 0, 0)
    assert ' test' == _align_and_pad('test', 'right', 5, 0, 0)
    assert '  test' == _align_and_pad('test', 'right', 6, 0, 0)
    assert '   test' == _align_and_pad('test', 'right', 7, 0, 0)

    assert 'test' == _align_and_pad('test', 'center', 1, 0, 0)
    assert 'test' == _align_and_pad('test', 'center', 4, 0, 0)
    assert ' test' == _align_and_pad('test', 'center', 5, 0, 0)
    assert ' test ' == _align_and_pad('test', 'center', 6, 0, 0)
    assert '  test ' == _align_and_pad('test', 'center', 7, 0, 0)


def test_padding():
    assert ' test' == _align_and_pad('test', 'left', 4, 1, 0)
    assert 'test ' == _align_and_pad('test', 'left', 4, 0, 1)
    assert ' test ' == _align_and_pad('test', 'left', 4, 1, 1)


def test_multi_line():
    assert ' test     \n          ' == _align_and_pad('test\n', 'left', 8, 1, 1)
    assert '          \n test     ' == _align_and_pad('\ntest', 'left', 8, 1, 1)
    assert '          \n test     \n          ' == _align_and_pad('\ntest\n', 'left', 8, 1, 1)


def test_multi_line_align_padding():
    assert 'test\ntest' == _align_and_pad('test\ntest', 'left', 4, 0, 0)
    assert 'test \ntest ' == _align_and_pad('test\ntest', 'left', 5, 0, 0)
    assert 'test  \ntest  ' == _align_and_pad('test\ntest', 'left', 6, 0, 0)
    assert 'test   \ntest   ' == _align_and_pad('test\ntest', 'left', 7, 0, 0)
    assert ' test  \ntest   ' == _align_and_pad(' test\ntest', 'left', 7, 0, 0)
    assert ' test  \n test  ' == _align_and_pad(' test\n test', 'left', 7, 0, 0)

    assert 'test\ntest' == _align_and_pad('test\ntest', 'right', 4, 0, 0)
    assert ' test\n test' == _align_and_pad('test\ntest', 'right', 5, 0, 0)
    assert '  test\n  test' == _align_and_pad('test\ntest', 'right', 6, 0, 0)
    assert '   test\n   test' == _align_and_pad('test\ntest', 'right', 7, 0, 0)

    assert 'test\ntest' == _align_and_pad('test\ntest', 'center', 4, 0, 0)
    assert ' test\n test' == _align_and_pad('test\ntest', 'center', 5, 0, 0)
    assert ' test \n test ' == _align_and_pad('test\ntest', 'center', 6, 0, 0)
    assert '  test \n  test ' == _align_and_pad('test\ntest', 'center', 7, 0, 0)

    assert ' test\n test' == _align_and_pad('test\ntest', 'left', 4, 1, 0)
    assert 'test \ntest ' == _align_and_pad('test\ntest', 'left', 4, 0, 1)
    assert ' test \n test ' == _align_and_pad('test\ntest', 'left', 4, 1, 1)
