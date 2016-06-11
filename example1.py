#!/usr/bin/env python
"""Simple example usage of terminaltables without any other dependencies.

Just prints sample text and exits.
"""

from __future__ import print_function

from terminaltables import AsciiTable, DoubleTable, SingleTable

TABLE_DATA = (
    ('Platform', 'Years', 'Notes'),
    ('Mk5', '2007-2009', 'The Golf Mk5 Variant was\nintroduced in 2007.'),
    ('MKVI', '2009-2013', 'Might actually be Mk5.'),
)


def main():
    """Main function."""
    title = 'Jetta SportWagen'

    # AsciiTable.
    table_instance = AsciiTable(TABLE_DATA, title)
    table_instance.justify_columns[2] = 'right'
    print(table_instance.table)
    print()

    # SingleTable.
    table_instance = SingleTable(TABLE_DATA, title)
    table_instance.justify_columns[2] = 'right'
    print(table_instance.table)
    print()

    # DoubleTable.
    table_instance = DoubleTable(TABLE_DATA, title)
    table_instance.justify_columns[2] = 'right'
    print(table_instance.table)
    print()


if __name__ == '__main__':
    main()
