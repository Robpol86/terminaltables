"""AsciiTable end to end testing."""

import sys
from textwrap import dedent

import py
import pytest

from terminaltables import AsciiTable
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
    table = AsciiTable(table_data, 'Example')
    table.inner_footing_row_border = True
    table.justify_columns[0] = 'left'
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'right'
    actual = table.table

    expected = (
        '+Example-----+-------+-----------+\n'
        '| Name       | Color |      Type |\n'
        '+------------+-------+-----------+\n'
        '| Avocado    | green |       nut |\n'
        '| Tomato     |  red  |     fruit |\n'
        '| Lettuce    | green | vegetable |\n'
        '| Watermelon | green |           |\n'
        '+------------+-------+-----------+\n'
        '|            |       |           |\n'
        '+------------+-------+-----------+'
    )
    assert actual == expected


def test_multi_line():
    """Test multi-lined cells."""
    table_data = [
        ['Show', 'Characters'],
        ['Rugrats', 'Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\nDil Pickles'],
        ['South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick']
    ]
    table = AsciiTable(table_data)

    # Test defaults.
    actual = table.table
    expected = (
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Show       | Characters                                                                          |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |\n'
        '|            | Dil Pickles                                                                         |\n'
        '| South Park | Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          |\n'
        '+------------+-------------------------------------------------------------------------------------+'
    )
    assert actual == expected

    # Test inner row border.
    table.inner_row_border = True
    actual = table.table
    expected = (
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Show       | Characters                                                                          |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |\n'
        '|            | Dil Pickles                                                                         |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| South Park | Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick                          |\n'
        '+------------+-------------------------------------------------------------------------------------+'
    )
    assert actual == expected

    # Justify right.
    table.justify_columns = {1: 'right'}
    actual = table.table
    expected = (
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Show       |                                                                          Characters |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| Rugrats    | Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles, |\n'
        '|            |                                                                         Dil Pickles |\n'
        '+------------+-------------------------------------------------------------------------------------+\n'
        '| South Park |                          Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick |\n'
        '+------------+-------------------------------------------------------------------------------------+'
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
    screenshot = PROJECT_ROOT.join('test_ascii_table.png')
    if screenshot.check():
        screenshot.remove()

    # Generate script.
    script_template = dedent(u"""\
    from __future__ import print_function
    import os, time
    from colorclass import Color, Windows
    from terminaltables import AsciiTable
    Windows.enable(auto_colors=True)
    stop_after = time.time() + 20

    table_data = [
        [Color('{b}Name{/b}'), Color('{b}Color{/b}'), Color('{b}Misc{/b}')],
        ['Avocado', Color('{autogreen}green{/fg}'), 100],
        ['Tomato', Color('{autored}red{/fg}'), 0.5],
        ['Lettuce', Color('{autogreen}green{/fg}'), None],
    ]
    print(AsciiTable(table_data).table)

    print('Waiting for screenshot_until_match()...')
    while not os.path.exists(r'%s') and time.time() < stop_after:
        time.sleep(0.5)
    """)
    script_contents = script_template % str(screenshot)
    script.write(script_contents.encode('utf-8'), mode='wb')

    # Setup expected.
    sub_images = [str(p) for p in HERE.listdir('sub_ascii_*.bmp')]
    assert sub_images

    # Run.
    with RunNewConsole(command) as gen:
        screenshot_until_match(str(screenshot), 15, sub_images, 1, gen)
