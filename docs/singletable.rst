.. _singletable:

===========
SingleTable
===========

SingleTable uses `box drawing characters`_ for table borders. On POSIX (Linux/OS X) terminaltables uses ``Esc ( 0``
characters while on Windows it uses `code page 437`_ characters.

.. image:: singletable.png
    :target: _images/singletable.png

Gaps on Windows 10
==================

Unfortunately the console on Windows 10 changed the default font face to ``Consolas``. This new font seems to show gaps
between lines. Switching the font back to ``Lucida Console`` eliminates the gaps.

API
===

.. autoclass:: terminaltables.SingleTable
    :members: column_max_width, column_widths, ok, table_width, table

.. _box drawing characters: https://en.wikipedia.org/wiki/Box-drawing_character
.. _code page 437: https://en.wikipedia.org/wiki/Code_page_437
