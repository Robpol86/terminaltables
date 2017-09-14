#!/usr/bin/env python
"""Example usage of terminaltables with colorclass.

Just prints sample text and exits.
"""

from __future__ import print_function

from colorclass import Color, Windows

from terminaltables import SingleTable
from terminaltables import SEPARATOR


def table_server_timings():
    """Return table string to be printed."""
    table_data = [
        [Color('{autogreen}<10ms{/autogreen}'), '192.168.0.100, 192.168.0.101'],
        [Color('{autoyellow}10ms <= 100ms{/autoyellow}'), '192.168.0.102, 192.168.0.103'],
        [Color('{autored}>100ms{/autored}'), '192.168.0.105'],
    ]
    table_instance = SingleTable(table_data)
    table_instance.inner_heading_row_border = False
    return table_instance.table


def table_server_status():
    """Return table string to be printed."""
    table_data = [
        [Color('Low Space'), Color('{autocyan}Nominal Space{/autocyan}'), Color('Excessive Space')],
        [Color('Low Load'), Color('Nominal Load'), Color('{autored}High Load{/autored}')],
        [Color('{autocyan}Low Free RAM{/autocyan}'), Color('Nominal Free RAM'), Color('High Free RAM')],
    ]
    table_instance = SingleTable(table_data, '192.168.0.105')
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True
    table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
    return table_instance.table


def table_abcd():
    """Return table string to be printed. Two tables on one line."""
    table_instance = SingleTable([['A', 'B'], ['C', 'D']])

    # Get first table lines.
    table_instance.outer_border = False
    table_inner_borders = table_instance.table.splitlines()

    # Get second table lines.
    table_instance.outer_border = True
    table_instance.inner_heading_row_border = False
    table_instance.inner_column_border = False
    table_outer_borders = table_instance.table.splitlines()

    # Combine.
    smallest, largest = sorted([table_inner_borders, table_outer_borders], key=len)
    smallest += [''] * (len(largest) - len(smallest))  # Make both same size.
    combined = list()
    for i, row in enumerate(largest):
        combined.append(row.ljust(10) + '          ' + smallest[i])
    return '\n'.join(combined)


def table_separators():
    table_data = [["X", "Y"]]
    for x in range(0, 3):
        for y in range(0, 5):
            table_data.append([Color("{autoyellow}" + str(x) + "{/autoyellow}"), Color(str(y))])
        table_data.append([SEPARATOR])
    table_instance = SingleTable(table_data, "Separators")
    return table_instance.table


def main():
    """Main function."""
    Windows.enable(auto_colors=True, reset_atexit=True)  # Does nothing if not on Windows.

    # Server timings.
    print(table_server_timings())
    print()

    # Server status.
    print(table_server_status())
    print()

    # Two A B C D tables.
    print(table_abcd())
    print()

    # Separators
    print(table_separators())
    print()

    # Instructions.
    table_instance = SingleTable([['Obey Obey Obey Obey']], 'Instructions')
    print(table_instance.table)
    print()


if __name__ == '__main__':
    main()
