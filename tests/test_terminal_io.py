"""Test functions in terminaltables.terminal_io."""

import ctypes

from terminaltables.terminal_io import set_terminal_title, terminal_size


def fake_csbi(_, string_buffer):
    """Mock GetConsoleScreenBufferInfo for Windows testing."""
    string_buffer.raw = b'x\x00)#\x00\x00\x87\x05\x07\x00\x00\x00j\x05w\x00\x87\x05x\x00J\x00'


def test_terminal_size(monkeypatch):
    """Test terminal_size(). In CIs the default height/width is returned since there is no terminal."""
    width, height = terminal_size()
    assert width > 0
    assert height > 0

    if hasattr(ctypes, 'windll'):
        monkeypatch.setattr('ctypes.windll.kernel32.GetConsoleScreenBufferInfo', fake_csbi)
    else:
        monkeypatch.setattr('fcntl.ioctl', lambda *_: b'\x1d\x00w\x00\xca\x02\x96\x01')
    width, height = terminal_size()
    assert width == 119
    assert height == 29


def test_set_terminal_title():
    """Run the function looking for exceptions. Can't get title on Linux/OSX so can't fully test."""
    set_terminal_title('Testing terminaltables.')
