#!/usr/bin/env python
"""Setup script for the project."""

from __future__ import print_function

import codecs
import os

from setuptools import setup


def readme():
    """Try to read README.rst or return empty string if failed.

    :return: File contents.
    :rtype: str
    """
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'README.rst'))
    handle = None
    try:
        handle = codecs.open(path, encoding='utf-8')
        return handle.read(131072)
    except IOError:
        return ''
    finally:
        getattr(handle, 'close', lambda: None)()


setup(
    author='@Robpol86',
    author_email='robpol86@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Terminals',
        'Topic :: Text Processing :: Markup',
    ],
    description='Generate simple tables in terminals from a nested list of strings.',
    install_requires=[],
    keywords='Shell Bash ANSI ASCII terminal tables',
    license='MIT',
    long_description=readme(),
    name='terminaltables',
    packages=['terminaltables'],
    url='https://github.com/Robpol86/terminaltables',
    version='2.1.0',
    zip_safe=True,
)
