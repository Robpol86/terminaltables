# coding: utf-8
"""Test function in module."""

import pytest

from terminaltables.terminal_io import DEFAULT_HEIGHT, DEFAULT_WIDTH, INVALID_HANDLE_VALUE, IS_WINDOWS, terminal_size

from tests.test_terminal_io import MockKernel32


@pytest.mark.parametrize('stderr', [1, INVALID_HANDLE_VALUE])
@pytest.mark.parametrize('stdout', [2, INVALID_HANDLE_VALUE])
def test_windows(monkeypatch, stderr, stdout):
    """Test function with IS_WINDOWS=True.

    :param monkeypatch: pytest fixture.
    :param int stderr: Mock handle value.
    :param int stdout: Mock handle value.
    """
    monkeypatch.setattr('terminaltables.terminal_io.IS_WINDOWS', True)

    kernel32 = MockKernel32(stderr=stderr, stdout=stdout)
    width, height = terminal_size(kernel32)

    if stderr == INVALID_HANDLE_VALUE and stdout == INVALID_HANDLE_VALUE:
        assert width == DEFAULT_WIDTH
        assert height == DEFAULT_HEIGHT
    elif stdout == INVALID_HANDLE_VALUE:
        assert width == 119
        assert height == 29
    elif stderr == INVALID_HANDLE_VALUE:
        assert width == 75
        assert height == 28
    else:
        assert width == 119
        assert height == 29


@pytest.mark.skipif(str(IS_WINDOWS))
def test_nix(monkeypatch):
    """Test function with IS_WINDOWS=False.

    :param monkeypatch: pytest fixture.
    """
    # Test exception (no terminal within pytest).
    width, height = terminal_size()
    assert width == DEFAULT_WIDTH
    assert height == DEFAULT_HEIGHT

    # Test mocked.
    monkeypatch.setattr('fcntl.ioctl', lambda *_: b'\x1d\x00w\x00\xca\x02\x96\x01')
    width, height = terminal_size()
    assert width == 119
    assert height == 29
