"""Test function in module."""

import pytest

from terminaltables.build import combine


@pytest.mark.parametrize('generator', [False, True])
def test_borders(generator):
    """Test with borders.

    :param bool generator: Test with generator instead of list.
    """
    line = ['One', 'Two', 'Three']
    actual = list(combine(iter(line) if generator else line, '>', '|', '<'))
    assert actual == ['>', 'One', '|', 'Two', '|', 'Three', '<']


@pytest.mark.parametrize('generator', [False, True])
def test_no_border(generator):
    """Test without borders.

    :param bool generator: Test with generator instead of list.
    """
    line = ['One', 'Two', 'Three']
    actual = list(combine(iter(line) if generator else line, '', '', ''))
    assert actual == ['One', 'Two', 'Three']


@pytest.mark.parametrize('generator', [False, True])
def test_no_items(generator):
    """Test with empty list.

    :param bool generator: Test with generator instead of list.
    """
    actual = list(combine(iter([]) if generator else [], '>', '|', '<'))
    assert actual == ['>', '<']
