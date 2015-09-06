"""Test converting list of strings into single string representing a table row with borders."""

from textwrap import dedent

from terminaltables.base_table import join_row


def test_single_line():
    """Test on single lines."""
    assert '' == join_row([], '', '', '')
    assert '' == join_row([], '', '|', '')
    assert '|' == join_row([], '', '|', '|')
    assert '||' == join_row([], '|', '|', '|')

    assert '' == join_row([''], '', '', '')
    assert '' == join_row([''], '', '|', '')
    assert '|' == join_row([''], '', '|', '|')
    assert '||' == join_row([''], '|', '|', '|')

    assert 'test' == join_row(['test'], '', '', '')
    assert 'test' == join_row(['test'], '', '|', '')
    assert '|test' == join_row(['test'], '|', '', '')
    assert 'test|' == join_row(['test'], '', '', '|')
    assert '|test|' == join_row(['test'], '|', '|', '|')

    assert 'testtest2' == join_row(['test', 'test2'], '', '', '')
    assert 'test+test2' == join_row(['test', 'test2'], '', '+', '')
    assert '|test+test2|' == join_row(['test', 'test2'], '|', '+', '|')


def test_multi_line():
    """Test on multi-lines."""
    assert '\n' == join_row(['\n'], '', '', '')
    assert '\n' == join_row(['\n'], '', '|', '')
    assert '|\n|' == join_row(['\n'], '', '|', '|')
    assert '||\n||' == join_row(['\n'], '|', '|', '|')

    expected = dedent("""\
        > Cars | Jetta <
        >      | Camry <""")
    actual = join_row([' Cars \n      ', ' Jetta \n Camry '], '>', '|', '<')
    assert expected == actual
