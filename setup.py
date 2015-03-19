#!/usr/bin/env python

import atexit
from codecs import open
from distutils.spawn import find_executable
import os
import re
import sys
import subprocess

import setuptools.command.sdist
from setuptools.command.test import test

_JOIN = lambda *p: os.path.join(HERE, *p)
_PACKAGES = lambda: [os.path.join(r, s) for r, d, _ in os.walk(NAME_FILE) for s in d if s != '__pycache__']
_REQUIRES = lambda p: [i for i in open(_JOIN(p), encoding='utf-8') if i[0] != '-'] if os.path.exists(_JOIN(p)) else []
_VERSION_RE = re.compile(r"^__(version|author|license)__ = '([\w\.@]+)'$", re.MULTILINE)

CLASSIFIERS = (
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Environment :: MacOS X',
    'Environment :: Win32 (MS Windows)',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries',
    'Topic :: Terminals',
    'Topic :: Text Processing :: Markup',
)
DESCRIPTION = 'Generate simple tables in terminals from a nested list of strings.'
HERE = os.path.abspath(os.path.dirname(__file__))
KEYWORDS = 'Shell Bash ANSI ASCII terminal tables'
NAME = 'terminaltables'
NAME_FILE = NAME
PACKAGE = False
VERSION_FILE = os.path.join(NAME_FILE, '__init__.py') if PACKAGE else '{0}.py'.format(NAME_FILE)


class PyTest(test):
    description = 'Run all tests.'
    user_options = []
    CMD = 'test'
    TEST_ARGS = ['--cov-report', 'term-missing', '--cov', NAME_FILE, 'tests']

    def finalize_options(self):
        overflow_args = sys.argv[sys.argv.index(self.CMD) + 1:]
        test.finalize_options(self)
        setattr(self, 'test_args', self.TEST_ARGS + overflow_args)
        setattr(self, 'test_suite', True)

    def run_tests(self):
        # Import here, cause outside the eggs aren't loaded.
        pytest = __import__('pytest')
        err_no = pytest.main(self.test_args)
        sys.exit(err_no)


class PyTestPdb(PyTest):
    description = 'Run all tests, drops to ipdb upon unhandled exception.'
    CMD = 'testpdb'
    TEST_ARGS = ['--ipdb', 'tests']


class PyTestCovWeb(PyTest):
    description = 'Generates HTML report on test coverage.'
    CMD = 'testcovweb'
    TEST_ARGS = ['--cov-report', 'html', '--cov', NAME_FILE, 'tests']

    def run_tests(self):
        if find_executable('open'):
            atexit.register(lambda: subprocess.call(['open', _JOIN('htmlcov', 'index.html')]))
        PyTest.run_tests(self)


ALL_DATA = dict(
    author_email='robpol86@gmail.com',
    classifiers=CLASSIFIERS,
    cmdclass={PyTest.CMD: PyTest, PyTestPdb.CMD: PyTestPdb, PyTestCovWeb.CMD: PyTestCovWeb},
    description=DESCRIPTION,
    install_requires=_REQUIRES('requirements.txt'),
    keywords=KEYWORDS,
    long_description=open(_JOIN('README.rst'), encoding='utf-8').read(10000),
    name=NAME,
    tests_require=_REQUIRES('requirements-test.txt'),
    url='https://github.com/Robpol86/{0}'.format(NAME),
    zip_safe=True,
)


# noinspection PyTypeChecker
ALL_DATA.update(dict(_VERSION_RE.findall(open(_JOIN(VERSION_FILE), encoding='utf-8').read(1000).replace('\r\n', '\n'))))
ALL_DATA.update(dict(py_modules=[NAME_FILE]) if not PACKAGE else dict(packages=[NAME_FILE] + _PACKAGES()))


if __name__ == '__main__':
    if not all((ALL_DATA['author'], ALL_DATA['license'], ALL_DATA['version'])):
        raise ValueError('Failed to obtain metadata from package/module.')
    setuptools.setup(**ALL_DATA)
