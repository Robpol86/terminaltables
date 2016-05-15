"""Common objects used by tests in directory."""

import py

from terminaltables import terminal_io

HERE = py.path.local(__file__).dirpath()


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
