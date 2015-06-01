#!/usr/bin/env python
"""Setup script for the project."""

import codecs
import os
import re

import setuptools

_PACKAGES = lambda: [os.path.join(r, s) for r, d, _ in os.walk(NAME_FILE) for s in d if s != '__pycache__']
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
REQUIRES_INSTALL = ['colorclass']
REQUIRES_TEST = ['pytest-cov']
REQUIRES_ALL = REQUIRES_INSTALL + REQUIRES_TEST
VERSION_FILE = os.path.join(NAME_FILE, '__init__.py') if PACKAGE else '{0}.py'.format(NAME_FILE)


def _safe_read(path, length):
    """Read file contents."""
    if not os.path.exists(os.path.join(HERE, path)):
        return ''
    file_handle = codecs.open(os.path.join(HERE, path), encoding='utf-8')
    contents = file_handle.read(length)
    file_handle.close()
    return contents


ALL_DATA = dict(
    author_email='robpol86@gmail.com',
    classifiers=CLASSIFIERS,
    description=DESCRIPTION,
    install_requires=REQUIRES_INSTALL,
    keywords=KEYWORDS,
    long_description=_safe_read('README.rst', 15000),
    name=NAME,
    requires=REQUIRES_INSTALL,
    tests_require=REQUIRES_TEST,
    url='https://github.com/Robpol86/{0}'.format(NAME),
    zip_safe=True,
)


# noinspection PyTypeChecker
ALL_DATA.update(dict(_VERSION_RE.findall(_safe_read(VERSION_FILE, 1500).replace('\r\n', '\n'))))
ALL_DATA.update(dict(py_modules=[NAME_FILE]) if not PACKAGE else dict(packages=[NAME_FILE] + _PACKAGES()))


if __name__ == '__main__':
    if not all((ALL_DATA['author'], ALL_DATA['license'], ALL_DATA['version'])):
        raise ValueError('Failed to obtain metadata from package/module.')
    setuptools.setup(**ALL_DATA)
