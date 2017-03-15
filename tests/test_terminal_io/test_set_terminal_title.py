# coding: utf-8
"""Test function in module."""

import sys
from textwrap import dedent

import py
import pytest

from terminaltables.terminal_io import IS_WINDOWS, set_terminal_title

from tests import PROJECT_ROOT
from tests.screenshot import RunNewConsole, screenshot_until_match
from tests.test_terminal_io import MockKernel32

HERE = py.path.local(__file__).dirpath()


@pytest.mark.parametrize('is_windows', [False, True])
@pytest.mark.parametrize('mode', ['ascii', 'unicode', 'bytes'])
def test(monkeypatch, is_windows, mode):
    """Test function.

    :param monkeypatch: pytest fixture.
    :param bool is_windows: Monkeypatch terminal_io.IS_WINDOWS
    :param str mode: Scenario to test for.
    """
    monkeypatch.setattr('terminaltables.terminal_io.IS_WINDOWS', is_windows)
    kernel32 = MockKernel32()

    # Title.
    if mode == 'ascii':
        title = 'Testing terminaltables.'
    elif mode == 'unicode':
        title = u'Testing terminaltables with unicode: 世界你好蓝色'
    else:
        title = b'Testing terminaltables with bytes.'

    # Run.
    assert set_terminal_title(title, kernel32)
    if not is_windows:
        return

    # Verify.
    if mode == 'ascii':
        assert kernel32.setConsoleTitleA_called
        assert not kernel32.setConsoleTitleW_called
    elif mode == 'unicode':
        assert not kernel32.setConsoleTitleA_called
        assert kernel32.setConsoleTitleW_called
    else:
        assert kernel32.setConsoleTitleA_called
        assert not kernel32.setConsoleTitleW_called


@pytest.mark.skipif(str(not IS_WINDOWS))
@pytest.mark.parametrize('mode', ['ascii', 'unicode', 'bytes'])
@pytest.mark.skip  # https://github.com/Robpol86/terminaltables/issues/44
def test_windows_screenshot(tmpdir, mode):
    """Test function on Windows in a new console window. Take a screenshot to verify it works.

    :param tmpdir: pytest fixture.
    :param str mode: Scenario to test for.
    """
    script = tmpdir.join('script.py')
    command = [sys.executable, str(script)]
    change_title = tmpdir.join('change_title')
    screenshot = PROJECT_ROOT.join('test_terminal_io_{0}.png'.format(mode))
    if screenshot.check():
        screenshot.remove()

    # Determine title.
    if mode == 'ascii':
        title = "'test ASCII test'"
    elif mode == 'unicode':
        title = u"u'test 世界你好蓝色 test'"
    else:
        title = "b'test ASCII test'"

    # Generate script.
    script_template = dedent(u"""\
    # coding: utf-8
    from __future__ import print_function
    import os, time
    from terminaltables.terminal_io import set_terminal_title
    stop_after = time.time() + 20

    print('Waiting for FindWindowA() in RunNewConsole.__enter__()...')
    while not os.path.exists(r'{change_title}') and time.time() < stop_after:
        time.sleep(0.5)
    assert set_terminal_title({title}) is True

    print('Waiting for screenshot_until_match()...')
    while not os.path.exists(r'{screenshot}') and time.time() < stop_after:
        time.sleep(0.5)
    """)
    script_contents = script_template.format(change_title=str(change_title), title=title, screenshot=str(screenshot))
    script.write(script_contents.encode('utf-8'), mode='wb')

    # Setup expected.
    if mode == 'unicode':
        sub_images = [str(p) for p in HERE.listdir('sub_title_cjk_*.bmp')]
    else:
        sub_images = [str(p) for p in HERE.listdir('sub_title_ascii_*.bmp')]
    assert sub_images

    # Run.
    with RunNewConsole(command) as gen:
        change_title.ensure(file=True)  # Touch file.
        screenshot_until_match(str(screenshot), 15, sub_images, 1, gen)
