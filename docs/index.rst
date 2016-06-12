========================
terminaltables |version|
========================

Easily draw tables in terminal/console applications from a list of lists of strings. As easy as:

.. code-block:: pycon

    >>> from terminaltables import AsciiTable
    >>> table_data = [
    ... ['Heading1', 'Heading2'],
    ... ['row1 column1', 'row1 column2'],
    ... ['row2 column1', 'row2 column2'],
    ... ['row3 column1', 'row3 column2'],
    ... ]
    >>> table = AsciiTable(table_data)
    >>> print table.table
    +--------------+--------------+
    | Heading1     | Heading2     |
    +--------------+--------------+
    | row1 column1 | row1 column2 |
    | row2 column1 | row2 column2 |
    | row3 column1 | row3 column2 |
    +--------------+--------------+

.. figure:: examples.png
    :target: _images/examples.png

    Windows 10, Windows XP, and OS X are also supported. View source: :github:`example1.py`, :github:`example2.py`,
    :github:`example3.py`

Features
========

* Multi-line rows: add newlines to table cells and terminatables will handle the rest.
* Table titles: show a title embedded in the top border of the table.
* POSIX: Python 2.6, 2.7, PyPy, PyPy3, 3.3, 3.4, and 3.5 supported on Linux and OS X.
* Windows: Python 2.7, 3.3, 3.4, and 3.5 supported on Windows XP through 10.
* CJK: Wide Chinese/Japanese/Korean characters displayed correctly.
* RTL: Arabic and Hebrew characters aligned correctly.
* Alignment/Justification: Align individual columns left, center, or right.
* Colored text: colorclass_, colorama_, termcolor_, or just plain `ANSI escape codes`_.

Project Links
=============

* Documentation: https://robpol86.github.io/terminaltables
* Source code: https://github.com/Robpol86/terminaltables
* PyPI homepage: https://pypi.python.org/pypi/terminaltables

Contents
========

.. toctree::
    :maxdepth: 2
    :caption: General

    install
    quickstart
    settings

.. toctree::
    :maxdepth: 2
    :caption: Table Styles

    asciitable
    singletable
    doubletable
    githubtable

.. _colorclass: https://github.com/Robpol86/colorclass
.. _colorama: https://github.com/tartley/colorama
.. _termcolor: https://pypi.python.org/pypi/termcolor
.. _ANSI escape codes: http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html
