import os
import subprocess
import sys


def test_example1():
    path = os.path.join(os.path.dirname(__file__), '..', 'example1.py')
    env = dict(PYTHONIOENCODING='utf-8')
    if 'SystemRoot' in os.environ:
        env['SystemRoot'] = os.environ['SystemRoot']
    assert 0 == subprocess.call([sys.executable, path], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def test_example2():
    path = os.path.join(os.path.dirname(__file__), '..', 'example2.py')
    env = dict(PYTHONIOENCODING='utf-8')
    if 'SystemRoot' in os.environ:
        env['SystemRoot'] = os.environ['SystemRoot']
    assert 0 == subprocess.call([sys.executable, path], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def test_example3():
    path = os.path.join(os.path.dirname(__file__), '..', 'example3.py')
    env = dict(PYTHONIOENCODING='utf-8')
    if 'SystemRoot' in os.environ:
        env['SystemRoot'] = os.environ['SystemRoot']
    assert 0 == subprocess.call([sys.executable, path], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
