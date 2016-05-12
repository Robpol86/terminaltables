# coding: utf-8
"""Test functions in terminaltables.terminal_io."""

import ctypes
import sys
from textwrap import dedent

import pytest

from terminaltables import terminal_io

from tests.screenshot import PROJECT_ROOT, RunNewConsole, screenshot_until_match


class MockKernel32(object):
    """Mock kernel32."""

    def __init__(self, stderr=terminal_io.INVALID_HANDLE_VALUE, stdout=terminal_io.INVALID_HANDLE_VALUE):
        """Constructor."""
        self.stderr = stderr
        self.stdout = stdout
        self.csbi_err = b'x\x00)#\x00\x00\x87\x05\x07\x00\x00\x00j\x05w\x00\x87\x05x\x00J\x00'  # 119 x 29
        self.csbi_out = b'L\x00,\x01\x00\x00*\x01\x07\x00\x00\x00\x0e\x01K\x00*\x01L\x00L\x00'  # 75 x 28
        self.setConsoleTitleA_called = False
        self.setConsoleTitleW_called = False

    def GetConsoleScreenBufferInfo(self, handle, lpcsbi):  # noqa
        """Mock GetConsoleScreenBufferInfo.

        :param handle: Unused handle.
        :param lpcsbi: ctypes.create_string_buffer() return value.
        """
        if handle == self.stderr:
            lpcsbi.raw = self.csbi_err
        else:
            lpcsbi.raw = self.csbi_out
        return 1

    def GetStdHandle(self, handle):  # noqa
        """Mock GetStdHandle.

        :param int handle: STD_ERROR_HANDLE or STD_OUTPUT_HANDLE.
        """
        return self.stderr if handle == terminal_io.STD_ERROR_HANDLE else self.stdout

    def SetConsoleTitleA(self, _):  # noqa
        """Mock SetConsoleTitleA."""
        self.setConsoleTitleA_called = True
        return 1

    def SetConsoleTitleW(self, _):  # noqa
        """Mock SetConsoleTitleW."""
        self.setConsoleTitleW_called = True
        return 1


def test_get_console_info():
    """Test function."""
    # Test live WinError.
    if terminal_io.IS_WINDOWS:
        with pytest.raises(OSError):
            terminal_io.get_console_info(ctypes.windll.kernel32, 0)

    # Test INVALID_HANDLE_VALUE.
    kernel32 = MockKernel32(stderr=1)
    with pytest.raises(OSError):
        terminal_io.get_console_info(kernel32, terminal_io.INVALID_HANDLE_VALUE)

    # Test no error with mock methods.
    width, height = terminal_io.get_console_info(kernel32, 1)
    assert width == 119
    assert height == 29


@pytest.mark.parametrize('stderr', [1, terminal_io.INVALID_HANDLE_VALUE])
@pytest.mark.parametrize('stdout', [2, terminal_io.INVALID_HANDLE_VALUE])
def test_terminal_size_windows(monkeypatch, stderr, stdout):
    """Test function with IS_WINDOWS=True.

    :param monkeypatch: pytest fixture.
    :param int stderr: Mock handle value.
    :param int stdout: Mock handle value.
    """
    monkeypatch.setattr(terminal_io, 'IS_WINDOWS', True)

    kernel32 = MockKernel32(stderr=stderr, stdout=stdout)
    width, height = terminal_io.terminal_size(kernel32)

    if stderr == terminal_io.INVALID_HANDLE_VALUE and stdout == terminal_io.INVALID_HANDLE_VALUE:
        assert width == terminal_io.DEFAULT_WIDTH
        assert height == terminal_io.DEFAULT_HEIGHT
    elif stdout == terminal_io.INVALID_HANDLE_VALUE:
        assert width == 119
        assert height == 29
    elif stderr == terminal_io.INVALID_HANDLE_VALUE:
        assert width == 75
        assert height == 28
    else:
        assert width == 119
        assert height == 29


@pytest.mark.skipif(str(terminal_io.IS_WINDOWS))
def test_terminal_size_nix(monkeypatch):
    """Test function with IS_WINDOWS=False.

    :param monkeypatch: pytest fixture.
    """
    # Test exception (no terminal within pytest).
    width, height = terminal_io.terminal_size()
    assert width == terminal_io.DEFAULT_WIDTH
    assert height == terminal_io.DEFAULT_HEIGHT

    # Test mocked.
    monkeypatch.setattr('fcntl.ioctl', lambda *_: b'\x1d\x00w\x00\xca\x02\x96\x01')
    width, height = terminal_io.terminal_size()
    assert width == 119
    assert height == 29


@pytest.mark.parametrize('is_windows', [False, True])
@pytest.mark.parametrize('mode', ['ascii', 'unicode', 'bytes'])
def test_set_terminal_title(monkeypatch, is_windows, mode):
    """Test function.

    :param monkeypatch: pytest fixture.
    :param bool is_windows: Monkeypatch terminal_io.IS_WINDOWS
    :param str mode: Scenario to test for.
    """
    monkeypatch.setattr(terminal_io, 'IS_WINDOWS', is_windows)
    kernel32 = MockKernel32()

    # Title.
    if mode == 'ascii':
        title = 'Testing terminaltables.'
    elif mode == 'unicode':
        title = u'Testing terminaltables with unicode: 世界你好蓝色'
    else:
        title = b'Testing terminaltables with bytes.'

    # Run.
    assert terminal_io.set_terminal_title(title, kernel32)
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


@pytest.mark.skipif(str(not terminal_io.IS_WINDOWS))
@pytest.mark.parametrize('mode', ['ascii', 'unicode', 'bytes'])
def test_set_terminal_title_screenshot(tmpdir, mode):
    """Test function on Windows in a new console window. Take a screenshot to verify it works.

    :param tmpdir: pytest fixture.
    :param str mode: Scenario to test for.
    """
    script = tmpdir.join('script.py')
    command = [sys.executable, str(script)]
    change_title = tmpdir.join('change_title')
    screenshot = PROJECT_ROOT.join('test_terminal_io.png')
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
        sub_images = [str(p) for p in PROJECT_ROOT.join('tests').listdir('sub_title_cjk_*.bmp')]
    else:
        sub_images = [str(p) for p in PROJECT_ROOT.join('tests').listdir('sub_title_ascii_*.bmp')]
    assert sub_images

    # Run.
    with RunNewConsole(command) as gen:
        change_title.ensure(file=True)  # Touch file.
        screenshot_until_match(str(screenshot), 15, sub_images, 1, gen)
