"""Test example scripts."""

from __future__ import print_function

import os
import subprocess
import sys

import pytest

from tests import PROJECT_ROOT


@pytest.mark.parametrize('filename', map('example{0}.py'.format, (1, 2, 3)))
def test(filename):
    """Test with subprocess.

    :param str filename: Example script filename to run.
    """
    command = [sys.executable, str(PROJECT_ROOT.join(filename))]
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    # Run.
    proc = subprocess.Popen(command, env=env, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    output = proc.communicate()[0]

    # Verify.
    try:
        assert proc.poll() == 0
    except AssertionError:
        print(output)
        raise
