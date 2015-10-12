==============
terminaltables
==============

Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.

* Python 2.6, 2.7, PyPy, PyPy3, 3.3, and 3.4 supported on Linux and OS X.
* Python 2.7, 3.3, and 3.4 supported on Windows (both 32 and 64 bit versions of Python).

.. image:: https://img.shields.io/appveyor/ci/Robpol86/terminaltables/master.svg?style=flat-square&label=AppVeyor%20CI
   :target: https://ci.appveyor.com/project/Robpol86/terminaltables
   :alt: Build Status Windows

.. image:: https://img.shields.io/travis/Robpol86/terminaltables/master.svg?style=flat-square&label=Travis%20CI
   :target: https://travis-ci.org/Robpol86/terminaltables
   :alt: Build Status

.. image:: https://img.shields.io/codecov/c/github/Robpol86/terminaltables/master.svg?style=flat-square&label=Codecov
   :target: https://codecov.io/github/Robpol86/terminaltables
   :alt: Coverage Status

.. image:: https://img.shields.io/pypi/v/terminaltables.svg?style=flat-square&label=Latest
   :target: https://pypi.python.org/pypi/terminaltables/
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/terminaltables.svg?style=flat-square&label=PyPI%20Downloads
   :target: https://pypi.python.org/pypi/terminaltables/
   :alt: Downloads

Quickstart
==========

Install:

.. code:: bash

    pip install terminaltables

Example Implementations
=======================

.. image:: https://github.com/Robpol86/terminaltables/raw/master/example.png?raw=true
   :alt: Example Scripts Screenshot

Source code for examples: `example1.py <https://github.com/Robpol86/terminaltables/blob/master/example1.py>`_,
`example2.py <https://github.com/Robpol86/terminaltables/blob/master/example2.py>`_, and
`example3.py <https://github.com/Robpol86/terminaltables/blob/master/example3.py>`_

Usage
=====

The below usage information is for ``AsciiTable`` which uses simple ASCII characters for the table (e.g. ``-`` ``+``
``|``). Use ``SingleTable`` for `box drawing characters <http://en.wikipedia.org/wiki/Box-drawing_character>`_ instead.
You may also use ``DoubleTable`` for double-lined box characters. All three tables have the same methods and properties
and work on all platforms.

Simple Usage
------------

.. code:: python

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

``table_data`` is a list of lists of strings. The outer list represents the whole table, while the inner lists
represents rows. Each row-list holds strings which are the cells of that row.

The first row can be though of the heading, but it doesn't have to be. You can turn off the heading separator (the only
thing that makes the first row a "heading" row) by setting ``table.inner_heading_row_border = False``.

.. code:: python

    table.inner_heading_row_border = False
    print table.table
    +--------------+--------------+
    | Heading1     | Heading2     |
    | row1 column1 | row1 column2 |
    | row2 column1 | row2 column2 |
    | row3 column1 | row3 column2 |
    +--------------+--------------+


Sometimes the last row can be though of a total (summary) row, by default it isn't. You can turn on the las row separator (the only
thing that makes the last row a "total" row) by setting ``table.inner_footing_row_border = True``.

.. code:: python

    table.inner_heading_row_border = True
    table.inner_footing_row_border = True
    print table.table
    +--------------+--------------+
    | Heading1     | Heading2     |
    +--------------+--------------+
    | row1 column1 | row1 column2 |
    | row2 column1 | row2 column2 |
    +--------------+--------------+
    | row3 column1 | row3 column2 |
    +--------------+--------------+

If you want to add colors or bold the heading row, you'll have to do that yourself. Keep in mind that ``terminaltables``
relies on ``len()`` and other methods for calculating table borders. I suggest looking at
`colorclass <https://github.com/Robpol86/colorclass>`_ for supporting colors in ``terminaltables`` since it handles
color string lengths correctly.

Class Attributes
----------------

You can instantiate with ``AsciiTable(table_data)`` or ``AsciiTable(table_data, 'Table Title')``. These are available
after instantiating any table class.

============================ ===============================================================================
Name                         Description/Notes
============================ ===============================================================================
``table_data``               List of list of strings. Same object passed to ``__init__()``.
``title``                    Table title string. Default is None for no title.
``inner_column_border``      Default is ``True``. Separates columns.
``inner_footing_row_border`` Default is ``False``. This is what makes the last row a "footer row".
``inner_heading_row_border`` Default is ``True``. This is what makes the first row a "header row".
``inner_row_border``         Default is ``False``. This adds lines between rows.
``justify_columns``          Dictionary. Keys are column numbers (0 base), values are 'left', 'right', or 'center'.
``outer_border``             Default is ``True``. Toggles the top, bottom, left, and right table borders.
``padding_left``             Default is 1. Number of spaces to add to the left of the cell.
``padding_right``            Default is 1. Number of spaces to add to the right of the cell.
============================ ===============================================================================

Class Methods
-------------

These are regular methods available in either class.

==================== ==============================================================================================================================================================
Name                 Description/Notes
==================== ==============================================================================================================================================================
``column_max_width`` Takes one argument, column number (0 base). Returns The maximum size it will fit in the terminal without breaking the table. Takes other columns into account.
==================== ==============================================================================================================================================================

Class Properties
----------------

These are read-only properties after you instantiate either class. They are "real-time". You do not have to
re-instantiate if you change any of the class attributes, including ``table_data``.

===================== ====================================================================================
Name                  Description/Notes
===================== ====================================================================================
``column_widths``     Returns a list with the current column widths (one int per column) without padding.
``ok``                Returns True if the table fits within the terminal width, False if the table breaks.
``padded_table_data`` Returns the padding table data. With spaces and newlines. Does not include borders.
``table``             Returns a large string, the whole table. This may be printed to the terminal.
``table_width``       Returns the width of the table including padding and borders.
===================== ====================================================================================

Changelog
=========

This project adheres to `Semantic Versioning <http://semver.org/>`_.

2.0.0 - 2015-10-11
------------------

Changed
    * Refactored code. No new features.
    * Breaking changes: `UnixTable`/`WindowsTable`/`WindowsTableDouble` moved. Use `SingleTable`/`DoubleTable` instead.

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
