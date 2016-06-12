.. _settings:

========
Settings
========

All tables (except :ref:`githubtable`) have the same settings to change the way the table is displayed. These attributes
are available after instantiation.

.. py:attribute:: Table.table_data

    The actual table data to render. This must be a list (or tuple) of lists of strings. The outer list holds the rows
    and the inner lists holds the cells (aka columns in that row).

    Example:

    .. code-block:: python

        table.table_data = [
            ['Name', 'Color', 'Type'],
            ['Avocado', 'green', 'nut'],
            ['Tomato', 'red', 'fruit'],
            ['Lettuce', 'green', 'vegetable'],
        ]

.. py:attribute:: Table.title

    Optional title to show within the top border of the table. This is ignored if None or a blank string.

.. py:attribute:: Table.inner_column_border

    Toggles the column dividers. Set to **False** to disable these vertically dividing borders.

.. py:attribute:: Table.inner_footing_row_border

    Show a horizontal dividing border before the last row. If **True** this defines the last row as the table footer.

.. py:attribute:: Table.inner_heading_row_border

    Show a horizontal dividing border after the first row. If **False** this removes the border so the first row is no
    longer considered a header row. It'll look just like any other row.

.. py:attribute:: Table.inner_row_border

    If **True** terminaltables will show dividing borders between every row.

.. py:attribute:: Table.outer_border

    Toggles the four outer borders. If **False** the top, left, right, and bottom borders will not be shown.

.. py:attribute:: Table.justify_columns

    Aligns text in entire columns. The keys in this dict are column integers (0 for the first column) and the values
    are either 'left', 'right', or 'center'. Left is the default.

    Example:

    .. code-block:: pycon

        >>> table.justify_columns[0] = 'right'  # Name column.
        >>> table.justify_columns[1] = 'center'  # Color column.
        >>> print table.table
        +---------+-------+-----------+
        |    Name | Color | Type      |
        +---------+-------+-----------+
        | Avocado | green | nut       |
        |  Tomato |  red  | fruit     |
        | Lettuce | green | vegetable |
        +---------+-------+-----------+

.. py:attribute:: Table.padding_left

    Number of spaces to pad on the left side of every cell. Default is **1**. Padding adds spacing between the cell text
    and the column border.

.. py:attribute:: Table.padding_right

    Number of spaces to pad on the right side of every cell. Default is **1**. Padding adds spacing between the cell
    text and the column border.
