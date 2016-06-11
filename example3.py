#!/usr/bin/env python
"""Simple example usage of terminaltables and column_max_width().

Just prints sample text and exits.
"""

from __future__ import print_function

from textwrap import wrap

from terminaltables import SingleTable

LONG_STRING = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore '
               'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut '
               'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum '
               'dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui '
               'officia deserunt mollit anim id est laborum.')


def main():
    """Main function."""
    table_data = [
        ['Long String', ''],  # One row. Two columns. Long string will replace this empty string.
    ]
    table = SingleTable(table_data)

    # Calculate newlines.
    max_width = table.column_max_width(1)
    wrapped_string = '\n'.join(wrap(LONG_STRING, max_width))
    table.table_data[0][1] = wrapped_string

    print(table.table)


if __name__ == '__main__':
    main()
