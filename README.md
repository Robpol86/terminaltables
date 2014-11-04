# terminaltables

Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.

* Python 2.6, 2.7, 3.3, and 3.4 supported on Linux, OS X, and Cygwin.
* Python 2.7, 3.3, and 3.4 supported on Windows (both 32 and 64 bit versions of Python).

Tested on Windows XP and Windows 10 technical preview.

[![Build Status Windows](https://ci.appveyor.com/api/projects/status/krq10akm1qxyd9d6/branch/master?svg=true)]
(https://ci.appveyor.com/project/Robpol86/terminaltables)
[![Build Status](https://travis-ci.org/Robpol86/terminaltables.svg?branch=master)]
(https://travis-ci.org/Robpol86/terminaltables)
[![Coverage Status](https://img.shields.io/coveralls/Robpol86/terminaltables.svg)]
(https://coveralls.io/r/Robpol86/terminaltables)
[![Latest Version](https://pypip.in/version/terminaltables/badge.png)]
(https://pypi.python.org/pypi/terminaltables/)
[![Downloads](https://pypip.in/download/terminaltables/badge.png)]
(https://pypi.python.org/pypi/terminaltables/)
[![Download format](https://pypip.in/format/terminaltables/badge.png)]
(https://pypi.python.org/pypi/terminaltables/)
[![License](https://pypip.in/license/terminaltables/badge.png)]
(https://pypi.python.org/pypi/terminaltables/)

## Quickstart

Install:
```bash
pip install terminaltables
```

## Example Implementations

![Example Scripts Screenshot](/example.png?raw=true "Example Scripts Screenshot")

Source code for examples: [example1.py](example1.py), [example2.py](example2.py), and [example3.py](example3.py)

## Usage

The below usage information is for `AsciiTable` which uses simple ASCII characters for the table (e.g. -+|). Use
`SingleTable` for [box drawing characters](http://en.wikipedia.org/wiki/Box-drawing_character) instead. You may also use
`DoubleTable` for double-lined box characters. All three tables have the same methods and properties and work on all
platforms.

### Simple Usage

```python
from terminaltables import AsciiTable
table_data = [
	['Heading1', 'Heading2'],
	['row1 column1', 'row1 column2'],
	['row2 column1', 'row2 column2']
]
table = AsciiTable(table_data)
print table.table
+--------------+--------------+
| Heading1     | Heading2     |
+--------------+--------------+
| row1 column1 | row1 column2 |
| row2 column1 | row2 column2 |
+--------------+--------------+
```

`table_data` is a list of lists of strings. The outer list represents the whole table, while the inner lists represents
rows. Each row-list holds strings which are the cells of that row.

The first row can be though of the heading, but it doesn't have to be. You can turn off the heading separator (the only
thing that makes the first row a "heading" row) by setting `table.inner_heading_row_border = False`.

```python
table.inner_heading_row_border = False
print table.table
+--------------+--------------+
| Heading1     | Heading2     |
| row1 column1 | row1 column2 |
| row2 column1 | row2 column2 |
+--------------+--------------+
```

If you want to add colors or bold the heading row, you'll have to do that yourself. Keep in mind that `terminaltables`
relies on `len()` and other methods for calculating table borders. I suggest looking at
[colorclass](https://github.com/Robpol86/colorclass) for supporting colors in `terminaltables` since it handles color
string lengths correctly.

### Class Attributes

You can instantiate with `AsciiTable(table_data)` or `AsciiTable(table_data, 'Table Title')`. These are available after
instantiating any table class.

Name | Description/Notes
:--- | :----------------
`table_data` | List of list of strings. Same object passed to `__init__()`.
`title` | Table title string. Default is None for no title.
`inner_column_border` | Default is `True`. Separates columns.
`inner_heading_row_border` | Default is `True`. This is what makes the first row a "header row".
`inner_row_border` | Default is `False`. This adds lines between rows.
`justify_columns` | Dictionary. Keys are column numbers (0 base), values are 'left', 'right', or 'center'.
`outer_border` | Default is `True`. Toggles the top, bottom, left, and right table borders.
`padding_left` | Default is 1. Number of spaces to add to the left of the cell.
`padding_right` | Default is 1. Number of spaces to add to the right of the cell.

### Class Methods

These are regular methods available in either class.

Name | Description/Notes
:--- | :----------------
`column_max_width` | Takes one argument, column number (0 base). Returns The maximum size it will fit in the terminal without breaking the table. Takes other columns into account.

### Class Properties

These are read-only properties after you instantiate either class. They are "real-time". You do not have to
re-instantiate if you change any of the class attributes, including `table_data`.

Name | Description/Notes
:--- | :----------------
`column_widths` | Returns a list with the current column widths (one int per column) without padding.
`ok` | Returns True if the table fits within the terminal width, False if the table breaks.
`padded_table_data` | Returns the padding table data. With spaces and newlines. Does not include borders.
`table` | Returns a large string, the whole table. This may be printed to the terminal.
`table_width` | Returns the width of the table including padding and borders.

## Changelog

#### 1.1.1

* Fixed Python 2.7 64-bit terminal width bug on Windows.

#### 1.1.0

* Added Windows support.
* Added double-lined table.

#### 1.0.2

* Added `table_width` and `ok` properties.

#### 1.0.1

* Added terminal width/height defaults for testing:
    * `terminaltables.DEFAULT_TERMINAL_WIDTH`
    * `terminaltables.DEFAULT_TERMINAL_HEIGHT`

#### 1.0.0

* Initial release.
