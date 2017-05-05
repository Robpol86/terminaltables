# coding: utf-8
"""Test function in module."""

import ctypes

import pytest

from terminaltables.terminal_io import get_console_info, INVALID_HANDLE_VALUE

from tests.test_terminal_io import MockKernel32


@pytest.mark.skipif("sys.platform != 'win32'")
def test_live_win_error():
    """Test live WinError."""
    with pytest.raises(OSError):
        get_console_info(ctypes.windll.kernel32, 0)


def test_invalid_handle_value():
    """Test INVALID_HANDLE_VALUE."""
    kernel32 = MockKernel32(stderr=1)
    with pytest.raises(OSError):
        get_console_info(kernel32, INVALID_HANDLE_VALUE)


def test_no_error_with_mock_methods():
    """Test no error with mock methods."""
    kernel32 = MockKernel32(stderr=1)
    width, height = get_console_info(kernel32, 1)
    assert width == 119
    assert height == 29


@pytest.mark.skipif("sys.platform != 'win32'")
def test_no_console_screen_buffer_info():
    """Test no console screen buffer info."""
    kernel32 = MockKernel32(stderr=1, screen_buffer_info=False)
    with pytest.raises(OSError):
        get_console_info(kernel32, 1)
