"""SingleTable end to end testing on Windows."""

import sys
from textwrap import dedent

import py
import pytest

from terminaltables import SingleTable
from terminaltables.terminal_io import IS_WINDOWS
from tests import PROJECT_ROOT
from tests.screenshot import RunNewConsole, screenshot_until_match

HERE = py.path.local(__file__).dirpath()
pytestmark = pytest.mark.skipif(str(not IS_WINDOWS))


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
    table = SingleTable(table_data, 'Example')
    table.inner_footing_row_border = True
    table.justify_columns[0] = 'left'
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'right'
    actual = table.table

    expected = (
        u'\u250cExample\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n'

        u'\u2502 Name       \u2502 Color \u2502      Type \u2502\n'

        u'\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\n'

        u'\u2502 Avocado    \u2502 green \u2502       nut \u2502\n'

        u'\u2502 Tomato     \u2502  red  \u2502     fruit \u2502\n'

        u'\u2502 Lettuce    \u2502 green \u2502 vegetable \u2502\n'

        u'\u2502 Watermelon \u2502 green \u2502           \u2502\n'

        u'\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\n'

        u'\u2502            \u2502       \u2502           \u2502\n'

        u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'
    )
    assert actual == expected


def test_multi_line():
    """Test multi-lined cells."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', 'Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\nDil Pickles'],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = SingleTable(table_data)

    # Test defaults.
    actual = table.table
    expected = (
        u'\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n'

        u'\u2502 Show       \u2502 Characters                                                                          '
        u'\u2502\n'

        u'\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\n'

        u'\u2502 Rugrats    \u2502 Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, '
        u'\u2502\n'

        u'\u2502            \u2502 Dil Pickles                                                                         '
        u'\u2502\n'

        u'\u2502 South Park \u2502 Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          '
        u'\u2502\n'

        u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'
    )
    assert actual == expected

    # Test inner row border.
    table.inner_row_border = True
    actual = table.table
    expected = (
        u'\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n'

        u'\u2502 Show       \u2502 Characters                                                                          '
        u'\u2502\n'

        u'\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\n'

        u'\u2502 Rugrats    \u2502 Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, '
        u'\u2502\n'

        u'\u2502            \u2502 Dil Pickles                                                                         '
        u'\u2502\n'

        u'\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\n'

        u'\u2502 South Park \u2502 Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          '
        u'\u2502\n'

        u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'
    )
    assert actual == expected

    # Justify right.
    table.justify_columns = {1: 'right'}
    actual = table.table
    expected = (
        u'\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n'

        u'\u2502 Show       \u2502                                                                          Characters '
        u'\u2502\n'

        u'\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\n'

        u'\u2502 Rugrats    \u2502 Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, '
        u'\u2502\n'

        u'\u2502            \u2502                                                                         Dil Pickles '
        u'\u2502\n'

        u'\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\n'

        u'\u2502 South Park \u2502                          Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick '
        u'\u2502\n'

        u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500'
        u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'
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
    screenshot = PROJECT_ROOT.join('test_single_table.png')
    if screenshot.check():
        screenshot.remove()

    # Generate script.
    script_template = dedent(u"""\
    from __future__ import print_function
    import os, time
    from colorclass import Color, Windows
    from terminaltables import SingleTable
    Windows.enable(auto_colors=True)
    stop_after = time.time() + 20

    table_data = [
        [Color('{b}Name{/b}'), Color('{b}Color{/b}'), Color('{b}Misc{/b}')],
        ['Avocado', Color('{autogreen}green{/fg}'), 100],
        ['Tomato', Color('{autored}red{/fg}'), 0.5],
        ['Lettuce', Color('{autogreen}green{/fg}'), None],
    ]
    print(SingleTable(table_data).table)

    print('Waiting for screenshot_until_match()...')
    while not os.path.exists(r'%s') and time.time() < stop_after:
        time.sleep(0.5)
    """)
    script_contents = script_template % str(screenshot)
    script.write(script_contents.encode('utf-8'), mode='wb')

    # Setup expected.
    sub_images = [str(p) for p in HERE.listdir('sub_single_*.bmp')]
    assert sub_images

    # Run.
    with RunNewConsole(command) as gen:
        screenshot_until_match(str(screenshot), 15, sub_images, 1, gen)
