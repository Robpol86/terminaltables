"""Test example scripts."""

from __future__ import print_function

import os
import subprocess
import sys

import pytest

from tests import PROJECT_ROOT


@pytest.mark.parametrize('suffix', range(1, 4))
def test(suffix):
    """Test with subprocess.

    :param int suffix: Numerical suffix of file name to test.
    """
    command = [sys.executable, str(PROJECT_ROOT.join('example{0}.py'.format(suffix)))]
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
