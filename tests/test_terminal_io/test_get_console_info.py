# coding: utf-8
"""Test function in module."""

import ctypes

import pytest

from terminaltables.terminal_io import get_console_info, INVALID_HANDLE_VALUE, IS_WINDOWS

from tests.test_terminal_io import MockKernel32


def test():
    """Test function."""
    # Test live WinError.
    if IS_WINDOWS:
        with pytest.raises(OSError):
            get_console_info(ctypes.windll.kernel32, 0)

    # Test INVALID_HANDLE_VALUE.
    kernel32 = MockKernel32(stderr=1)
    with pytest.raises(OSError):
        get_console_info(kernel32, INVALID_HANDLE_VALUE)

    # Test no error with mock methods.
    width, height = get_console_info(kernel32, 1)
    assert width == 119
    assert height == 29
