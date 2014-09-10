from textwrap import dedent
from terminaltables import _convert_row


def test_single_line():
    assert '' == _convert_row([], '', '', '')
    assert '' == _convert_row([], '', '|', '')
    assert '|' == _convert_row([], '', '|', '|')
    assert '||' == _convert_row([], '|', '|', '|')

    assert '' == _convert_row([''], '', '', '')
    assert '' == _convert_row([''], '', '|', '')
    assert '|' == _convert_row([''], '', '|', '|')
    assert '||' == _convert_row([''], '|', '|', '|')

    assert 'test' == _convert_row(['test'], '', '', '')
    assert 'test' == _convert_row(['test'], '', '|', '')
    assert '|test' == _convert_row(['test'], '|', '', '')
    assert 'test|' == _convert_row(['test'], '', '', '|')
    assert '|test|' == _convert_row(['test'], '|', '|', '|')

    assert 'testtest2' == _convert_row(['test', 'test2'], '', '', '')
    assert 'test+test2' == _convert_row(['test', 'test2'], '', '+', '')
    assert '|test+test2|' == _convert_row(['test', 'test2'], '|', '+', '|')


def test_multi_line():
    assert '\n' == _convert_row(['\n'], '', '', '')
    assert '\n' == _convert_row(['\n'], '', '|', '')
    assert '|\n|' == _convert_row(['\n'], '', '|', '|')
    assert '||\n||' == _convert_row(['\n'], '|', '|', '|')

    expected = dedent("""\
        > Cars | Jetta <
        >      | Camry <""")
    actual = _convert_row([' Cars \n      ', ' Jetta \n Camry '], '>', '|', '<')
    assert expected == actual
