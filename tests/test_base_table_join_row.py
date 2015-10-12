"""Test converting list of strings into single string representing a table row with borders."""

from textwrap import dedent

from terminaltables.base_table import join_row


def test_single_line():
    """Test on single lines."""
    assert join_row([], '', '', '') == ''
    assert join_row([], '', '|', '') == ''
    assert join_row([], '', '|', '|') == '|'
    assert join_row([], '|', '|', '|') == '||'

    assert join_row([''], '', '', '') == ''
    assert join_row([''], '', '|', '') == ''
    assert join_row([''], '', '|', '|') == '|'
    assert join_row([''], '|', '|', '|') == '||'

    assert join_row(['test'], '', '', '') == 'test'
    assert join_row(['test'], '', '|', '') == 'test'
    assert join_row(['test'], '|', '', '') == '|test'
    assert join_row(['test'], '', '', '|') == 'test|'
    assert join_row(['test'], '|', '|', '|') == '|test|'

    assert join_row(['test', 'test2'], '', '', '') == 'testtest2'
    assert join_row(['test', 'test2'], '', '+', '') == 'test+test2'
    assert join_row(['test', 'test2'], '|', '+', '|') == '|test+test2|'


def test_multi_line():
    """Test on multi-lines."""
    assert join_row(['\n'], '', '', '') == '\n'
    assert join_row(['\n'], '', '|', '') == '\n'
    assert join_row(['\n'], '', '|', '|') == '|\n|'
    assert join_row(['\n'], '|', '|', '|') == '||\n||'

    expected = dedent("""\
        > Cars | Jetta <
        >      | Camry <""")
    actual = join_row([' Cars \n      ', ' Jetta \n Camry '], '>', '|', '<')
    assert actual == expected
