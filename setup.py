#!/usr/bin/env python

import ast
import atexit
from codecs import open
from distutils.spawn import find_executable
import os
import sys
import subprocess

import setuptools
import setuptools.command.sdist
from setuptools.command.test import test

HERE = os.path.abspath(os.path.dirname(__file__))
setuptools.command.sdist.READMES = tuple(list(getattr(setuptools.command.sdist, 'READMES', ())) + ['README.md'])
NAME = 'terminaltables'
NAME_FILE = NAME
PACKAGE = False


def get_metadata(main_file):
    """Get metadata about the package/module.

    Positional arguments:
    main_file -- python file path within `HERE` which has __author__ and the others defined as global variables.

    Returns:
    Dictionary to be passed into setuptools.setup().
    """
    with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

    with open(os.path.join(HERE, main_file), encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.startswith('__')]
    metadata = ast.literal_eval("{'" + ", '".join([l.replace(' = ', "': ") for l in lines]) + '}')
    __author__, __license__, __version__ = [metadata[k] for k in ('__author__', '__license__', '__version__')]

    everything = dict(version=__version__, long_description=long_description, author=__author__, license=__license__)
    if not all(everything.values()):
        raise ValueError('Failed to obtain metadata from package/module.')

    return everything


class PyTest(test):
    TEST_ARGS = ['--cov-report', 'term-missing', '--cov', NAME_FILE, 'tests']

    def finalize_options(self):
        test.finalize_options(self)
        setattr(self, 'test_args', self.TEST_ARGS)
        setattr(self, 'test_suite', True)

    def run_tests(self):
        # Import here, cause outside the eggs aren't loaded.
        pytest = __import__('pytest')
        err_no = pytest.main(self.test_args)
        sys.exit(err_no)


class PyTestPdb(PyTest):
    TEST_ARGS = ['--pdb', 'tests']


class PyTestCovWeb(PyTest):
    TEST_ARGS = ['--cov-report', 'html', '--cov', NAME_FILE, 'tests']

    def run_tests(self):
        if find_executable('open'):
            atexit.register(lambda: subprocess.call(['open', os.path.join(HERE, 'htmlcov', 'index.html')]))
        PyTest.run_tests(self)


class CmdStyle(setuptools.Command):
    user_options = []
    CMD_ARGS = ['flake8', '--max-line-length', '120', '--statistics', NAME_FILE + ('' if PACKAGE else '.py')]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.call(self.CMD_ARGS)


class CmdLint(CmdStyle):
    CMD_ARGS = ['pylint', '--max-line-length', '120', NAME_FILE + ('' if PACKAGE else '.py')]


ALL_DATA = dict(
    name=NAME,
    description='Generate simple tables in terminals from a nested list of strings.',
    url='https://github.com/Robpol86/{0}'.format(NAME),
    author_email='robpol86@gmail.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Terminals',
        'Topic :: Text Processing :: Markup',
    ],

    keywords='Shell Bash ANSI ASCII terminal tables',
    py_modules=[NAME_FILE],
    zip_safe=True,

    tests_require=['pytest', 'pytest-cov'],
    cmdclass=dict(test=PyTest, testpdb=PyTestPdb, testcovweb=PyTestCovWeb, style=CmdStyle, lint=CmdLint),

    # Pass the rest from get_metadata().
    **get_metadata(os.path.join(NAME_FILE + ('/__init__.py' if PACKAGE else '.py')))
)


if __name__ == '__main__':
    setuptools.setup(**ALL_DATA)
