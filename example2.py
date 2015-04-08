#!/usr/bin/env python
"""Example usage of terminaltables using colorclass.

Just prints sample text and exits.
"""

from __future__ import print_function

from colorclass import Color, Windows

from terminaltables import SingleTable


Windows.enable(auto_colors=True, reset_atexit=True)  # Does nothing if not on Windows.

table_data = [
    [Color('{autogreen}<10ms{/autogreen}'), '192.168.0.100, 192.168.0.101'],
    [Color('{autoyellow}10ms <= 100ms{/autoyellow}'), '192.168.0.102, 192.168.0.103'],
    [Color('{autored}>100ms{/autored}'), '192.168.0.105'],
]
table = SingleTable(table_data)
table.inner_heading_row_border = False
print()
print(table.table)

table.title = '192.168.0.105'
table.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
table.inner_row_border = True
table.table_data = [
    [Color('Low Space'), Color('{autocyan}Nominal Space{/autocyan}'), Color('Excessive Space')],
    [Color('Low Load'), Color('Nominal Load'), Color('{autored}High Load{/autored}')],
    [Color('{autocyan}Low Free RAM{/autocyan}'), Color('Nominal Free RAM'), Color('High Free RAM')],
]
print()
print(table.table)

table.title = None
table.outer_border = False
table.table_data = [['A', 'B'], ['C', 'D']]
print()
print(table.table)

table.outer_border = True
table.inner_row_border = False
table.inner_column_border = False
print()
print(table.table)

table = SingleTable([['Obey Obey Obey Obey']], 'Instructions')
print()
print(table.table)

print()
