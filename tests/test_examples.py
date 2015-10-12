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
    """Test with subprocess."""
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'example{0}.py'.format(suffix)))
    env = dict(PYTHONIOENCODING='utf-8')
    if 'SystemRoot' in os.environ:
        env['SystemRoot'] = os.environ['SystemRoot']
    subprocess.check_output([sys.executable, path], env=env, stderr=subprocess.STDOUT)
