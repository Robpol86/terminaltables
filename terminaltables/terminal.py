"""Get info about the current terminal window/screen buffer."""

import ctypes
import struct
import sys

try:
    import fcntl
    import termios
except ImportError:
    fcntl = None
    termios = None

DEFAULT_HEIGHT = 24
DEFAULT_WIDTH = 80


def terminal_size():
    """Get the width and height of the terminal.

    http://code.activestate.com/recipes/440694-determine-size-of-console-window-on-windows/
    http://stackoverflow.com/questions/17993814/why-the-irrelevant-code-made-a-difference

    :return: Width (number of characters) and height (number of lines) of the terminal.
    :rtype: tuple
    """
    if hasattr(ctypes, 'windll'):
        # Only works on Microsoft Windows platforms.
        string_buffer = ctypes.create_string_buffer(22)  # To be written to by GetConsoleScreenBufferInfo.
        ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ctypes.windll.kernel32.GetStdHandle(-11), string_buffer)
        left, top, right, bottom = struct.unpack('hhhhHhhhhhh', string_buffer.raw)[5:-2]
        width, height = right - left, bottom - top
        if width < 1 or height < 1:
            return DEFAULT_WIDTH, DEFAULT_HEIGHT
        return width, height

    try:
        device = fcntl.ioctl(0, termios.TIOCGWINSZ, '\0' * 8)
    except IOError:
        return DEFAULT_WIDTH, DEFAULT_HEIGHT
    height, width = struct.unpack('hhhh', device)[:2]
    return width, height


def set_terminal_title(title):
    """Set the terminal title.

    :param str title: The title to set.
    """
    if hasattr(ctypes, 'windll'):
        if sys.version_info[0] == 3:
            func = ctypes.windll.kernel32.SetConsoleTitleW  # Unicode.
        else:
            func = ctypes.windll.kernel32.SetConsoleTitleA  # Ascii.
        return func(title)
    sys.stdout.write('\033]0;{0}\007'.format(title))
