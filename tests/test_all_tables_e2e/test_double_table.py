"""DoubleTable end to end testing."""

import sys
from textwrap import dedent

import py
import pytest

from terminaltables import DoubleTable
from terminaltables.terminal_io import IS_WINDOWS
from tests import PROJECT_ROOT
from tests.screenshot import RunNewConsole, screenshot_until_match

HERE = py.path.local(__file__).dirpath()


def test_single_line():
    """Test single-lined cells."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
        ['Watermelon', 'green'],
        [],
    ]
    table = DoubleTable(table_data, 'Example')
    table.inner_footing_row_border = True
    table.justify_columns[0] = 'left'
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'right'
    actual = table.table

    expected = (
        u'\u2554Example\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\n'

        u'\u2551 Name       \u2551 Color \u2551      Type \u2551\n'

        u'\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563\n'

        u'\u2551 Avocado    \u2551 green \u2551       nut \u2551\n'

        u'\u2551 Tomato     \u2551  red  \u2551     fruit \u2551\n'

        u'\u2551 Lettuce    \u2551 green \u2551 vegetable \u2551\n'

        u'\u2551 Watermelon \u2551 green \u2551           \u2551\n'

        u'\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563\n'

        u'\u2551            \u2551       \u2551           \u2551\n'

        u'\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d'
    )
    assert actual == expected


def test_multi_line():
    """Test multi-lined cells."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', 'Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\nDil Pickles'],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = DoubleTable(table_data)

    # Test defaults.
    actual = table.table
    expected = (
        u'\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\n'

        u'\u2551 Show       \u2551 Characters                                                                          '
        u'\u2551\n'

        u'\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563\n'

        u'\u2551 Rugrats    \u2551 Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, '
        u'\u2551\n'

        u'\u2551            \u2551 Dil Pickles                                                                         '
        u'\u2551\n'

        u'\u2551 South Park \u2551 Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          '
        u'\u2551\n'

        u'\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d'
    )
    assert actual == expected

    # Test inner row border.
    table.inner_row_border = True
    actual = table.table
    expected = (
        u'\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\n'

        u'\u2551 Show       \u2551 Characters                                                                          '
        u'\u2551\n'

        u'\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563\n'

        u'\u2551 Rugrats    \u2551 Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, '
        u'\u2551\n'

        u'\u2551            \u2551 Dil Pickles                                                                         '
        u'\u2551\n'

        u'\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563\n'

        u'\u2551 South Park \u2551 Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          '
        u'\u2551\n'

        u'\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d'
    )
    assert actual == expected

    # Justify right.
    table.justify_columns = {1: 'right'}
    actual = table.table
    expected = (
        u'\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\n'

        u'\u2551 Show       \u2551                                                                          Characters '
        u'\u2551\n'

        u'\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563\n'

        u'\u2551 Rugrats    \u2551 Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, '
        u'\u2551\n'

        u'\u2551            \u2551                                                                         Dil Pickles '
        u'\u2551\n'

        u'\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256c\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563\n'

        u'\u2551 South Park \u2551                          Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick '
        u'\u2551\n'

        u'\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'
        u'\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d'
    )
    assert actual == expected


@pytest.mark.skipif(str(not IS_WINDOWS))
@pytest.mark.skip  # https://github.com/Robpol86/terminaltables/issues/44
def test_windows_screenshot(tmpdir):
    """Test on Windows in a new console window. Take a screenshot to verify it works.

    :param tmpdir: pytest fixture.
    """
    script = tmpdir.join('script.py')
    command = [sys.executable, str(script)]
    screenshot = PROJECT_ROOT.join('test_double_table.png')
    if screenshot.check():
        screenshot.remove()

    # Generate script.
    script_template = dedent(u"""\
    from __future__ import print_function
    import os, time
    from colorclass import Color, Windows
    from terminaltables import DoubleTable
    Windows.enable(auto_colors=True)
    stop_after = time.time() + 20

    table_data = [
        [Color('{b}Name{/b}'), Color('{b}Color{/b}'), Color('{b}Misc{/b}')],
        ['Avocado', Color('{autogreen}green{/fg}'), 100],
        ['Tomato', Color('{autored}red{/fg}'), 0.5],
        ['Lettuce', Color('{autogreen}green{/fg}'), None],
    ]
    print(DoubleTable(table_data).table)

    print('Waiting for screenshot_until_match()...')
    while not os.path.exists(r'%s') and time.time() < stop_after:
        time.sleep(0.5)
    """)
    script_contents = script_template % str(screenshot)
    script.write(script_contents.encode('utf-8'), mode='wb')

    # Setup expected.
    sub_images = [str(p) for p in HERE.listdir('sub_double_*.bmp')]
    assert sub_images

    # Run.
    with RunNewConsole(command) as gen:
        screenshot_until_match(str(screenshot), 15, sub_images, 1, gen)
