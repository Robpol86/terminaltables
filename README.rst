==============
terminaltables
==============

Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.

* Python 2.6, 2.7, PyPy, PyPy3, 3.3, 3.4, and 3.5 supported on Linux and OS X.
* Python 2.7, 3.3, 3.4, and 3.5 supported on Windows (both 32 and 64 bit versions of Python).

📖 Full documentation: https://robpol86.github.io/terminaltables

.. image:: https://img.shields.io/appveyor/ci/Robpol86/terminaltables/master.svg?style=flat-square&label=AppVeyor%20CI
    :target: https://ci.appveyor.com/project/Robpol86/terminaltables
    :alt: Build Status Windows

.. image:: https://img.shields.io/travis/Robpol86/terminaltables/master.svg?style=flat-square&label=Travis%20CI
    :target: https://travis-ci.org/Robpol86/terminaltables
    :alt: Build Status

.. image:: https://img.shields.io/codecov/c/github/Robpol86/terminaltables/master.svg?style=flat-square&label=Codecov
    :target: https://codecov.io/gh/Robpol86/terminaltables
    :alt: Coverage Status

.. image:: https://img.shields.io/pypi/v/terminaltables.svg?style=flat-square&label=Latest
    :target: https://pypi.python.org/pypi/terminaltables
    :alt: Latest Version

Quickstart
==========

Install:

.. code:: bash

    pip install terminaltables

Usage:

.. code::

    from terminaltables import AsciiTable
    table_data = [
        ['Heading1', 'Heading2'],
        ['row1 column1', 'row1 column2'],
        ['row2 column1', 'row2 column2'],
        ['row3 column1', 'row3 column2']
    ]
    table = AsciiTable(table_data)
    print table.table
    +--------------+--------------+
    | Heading1     | Heading2     |
    +--------------+--------------+
    | row1 column1 | row1 column2 |
    | row2 column1 | row2 column2 |
    | row3 column1 | row3 column2 |
    +--------------+--------------+

Example Implementations
=======================

.. image:: docs/examples.png?raw=true
   :alt: Example Scripts Screenshot

Source code for examples: `example1.py <https://github.com/Robpol86/terminaltables/blob/master/example1.py>`_,
`example2.py <https://github.com/Robpol86/terminaltables/blob/master/example2.py>`_, and
`example3.py <https://github.com/Robpol86/terminaltables/blob/master/example3.py>`_

.. changelog-section-start

Changelog
=========

This project adheres to `Semantic Versioning <http://semver.org/>`_.

3.1.0 - 2016-10-16
------------------

Added
    * ``git --porcelain``-like table by liiight: https://github.com/Robpol86/terminaltables/pull/31

3.0.0 - 2016-05-30
------------------

Added
    * Support for https://pypi.python.org/pypi/colorama
    * Support for https://pypi.python.org/pypi/termcolor
    * Support for RTL characters (Arabic and Hebrew).
    * Support for non-string items in ``table_data`` like integers.

Changed
    * Refactored again, but this time entire project including tests.

Removed
    * ``padded_table_data`` property and ``join_row()``. Moving away from repeated string joining/splitting.

Fixed
    * ``set_terminal_title()`` Unicode handling on Windows.
    * https://github.com/Robpol86/terminaltables/issues/18
    * https://github.com/Robpol86/terminaltables/issues/20
    * https://github.com/Robpol86/terminaltables/issues/23
    * https://github.com/Robpol86/terminaltables/issues/26

2.1.0 - 2015-11-02
------------------

Added
    * GitHub Flavored Markdown table by bcho: https://github.com/Robpol86/terminaltables/pull/12
    * Python 3.5 support (Linux/OS X and Windows).

2.0.0 - 2015-10-11
------------------

Changed
    * Refactored code. No new features.
    * Breaking changes: ``UnixTable``/``WindowsTable``/``WindowsTableDouble`` moved. Use ``SingleTable``/``DoubleTable``
      instead.

1.2.1 - 2015-09-03
------------------

Fixed
    * CJK character width fixed by zqqf16 and bcho: https://github.com/Robpol86/terminaltables/pull/9

1.2.0 - 2015-05-31
------------------

Added
    * Bottom row separator.

1.1.1 - 2014-11-03
------------------

Fixed
    * Python 2.7 64-bit terminal width bug on Windows.

1.1.0 - 2014-11-02
------------------

Added
    * Windows support.
    * Double-lined table.

1.0.2 - 2014-09-18
------------------

Added
    * ``table_width`` and ``ok`` properties.

1.0.1 - 2014-09-12
------------------

Added
    * Terminal width/height defaults for testing.
    * ``terminaltables.DEFAULT_TERMINAL_WIDTH``
    * ``terminaltables.DEFAULT_TERMINAL_HEIGHT``

1.0.0 - 2014-09-11
------------------

* Initial release.

.. changelog-section-end
