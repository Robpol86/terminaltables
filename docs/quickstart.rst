.. _quickstart:

==========
Quickstart
==========

This section will go over the basics of terminaltables.

Make sure that you've already :ref:`installed <install>` it.

Table with Default Settings
===========================

Let's begin by importing AsciiTable, which just uses ``+``, ``-``, and ``|`` characters.

.. code-block:: pycon

    >>> from terminaltables import AsciiTable

Now let's define the table data in a variable called ``data``. We'll do it the long way by creating an empty list
representing the entire table. Then we'll add rows one by one. Each row is a list representing table cells.

.. code-block:: pycon

    >>> data = []
    >>> data.append(['Row one column one', 'Row one column two'])
    >>> data.append(['Row two column one', 'Row two column two'])
    >>> data.append(['Row three column one', 'Row three column two'])

Next we can use AsciiTable to format the table properly and then we can just print it. ``table.table`` gives you just
one long string with newline characters so you can easily print it.

.. code-block:: pycon

    >>> table = AsciiTable(data)
    >>> print table.table
    +----------------------+----------------------+
    | Row one column one   | Row one column two   |
    +----------------------+----------------------+
    | Row two column one   | Row two column two   |
    | Row three column one | Row three column two |
    +----------------------+----------------------+

By default the first row of the table is considered the heading. This can be turned off.

Changing Table Settings
=======================

There are more options available to change how your tables are formatted. Say your table doesn't really have a heading
row; all rows are just data.

.. code-block:: pycon

    >>> table.inner_heading_row_border = False
    >>> print table.table
    +----------------------+----------------------+
    | Row one column one   | Row one column two   |
    | Row two column one   | Row two column two   |
    | Row three column one | Row three column two |
    +----------------------+----------------------+

Now you want to add a title to the table:

.. code-block:: pycon

    >>> table.title = 'My Table'
    >>> print table.table
    +My Table--------------+----------------------+
    | Row one column one   | Row one column two   |
    | Row two column one   | Row two column two   |
    | Row three column one | Row three column two |
    +----------------------+----------------------+

Maybe you want lines in between all rows:

.. code-block:: pycon

    >>> table.inner_row_border = True
    >>> print table.table
    +My Table--------------+----------------------+
    | Row one column one   | Row one column two   |
    +----------------------+----------------------+
    | Row two column one   | Row two column two   |
    +----------------------+----------------------+
    | Row three column one | Row three column two |
    +----------------------+----------------------+

There are many more settings available. You can find out more by reading the :ref:`settings` section.

Other Table Styles
==================

Terminaltables comes with a few other table styles than just ``AsciiTable``. All table styles more or less have the same
API.

.. code-block:: pycon

    >>> from terminaltables import SingleTable
    >>> table = SingleTable(data)
    >>> print table.table
    ┌──────────────────────┬──────────────────────┐
    │ Row one column one   │ Row one column two   │
    ├──────────────────────┼──────────────────────┤
    │ Row two column one   │ Row two column two   │
    │ Row three column one │ Row three column two │
    └──────────────────────┴──────────────────────┘

You can find documentation for all table styles over at the :ref:`tables` section.
