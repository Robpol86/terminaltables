"""Test example scripts."""

import os
import sys

import pytest

try:
    import subprocess32 as subprocess
except ImportError:
    import subprocess


@pytest.mark.parametrize('suffix', range(1, 4))
def test(suffix):
    """Test with subprocess.

    :param int suffix: Numerical suffix of file name to test.
    """
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'example{0}.py'.format(suffix)))
    subprocess.check_output([sys.executable, path], stderr=subprocess.STDOUT)
