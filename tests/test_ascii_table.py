"""Test AsciiTable class."""

import pytest

from terminaltables.other_tables import AsciiTable

SINGLE_LINE = (
    ('Name', 'Color', 'Type'),
    ('Avocado', 'green', 'nut'),
    ('Tomato', 'red', 'fruit'),
    ('Lettuce', 'green', 'vegetable'),
)

MULTI_LINE = (
    ('Show', 'Characters'),
    ('Rugrats', 'Tommy Pickles, Chuckie Finster, Phillip DeVille, Lillian DeVille, Angelica Pickles,\nDil Pickles'),
    ('South Park', 'Stan Marsh, Kyle Broflovski, Eric Cartman, Kenny McCormick'),
)


@pytest.fixture(autouse=True)
def patch(monkeypatch):
    """Monkeypatch before every test function in this module.

    :param monkeypatch: pytest fixture.
    """
    monkeypatch.setattr('terminaltables.ascii_table.terminal_size', lambda: (79, 24))
    monkeypatch.setattr('terminaltables.width_and_alignment.terminal_size', lambda: (79, 24))


@pytest.mark.parametrize('table_data,column_number,expected', [
    ([], 0, IndexError),
    ([[]], 0, IndexError),
    ([['']], 1, IndexError),
    (SINGLE_LINE, 0, 55),
    (SINGLE_LINE, 1, 53),
    (SINGLE_LINE, 2, 57),
    (MULTI_LINE, 0, -11),
    (MULTI_LINE, 1, 62),
])
def test_column_max_width(table_data, column_number, expected):
    """Test method in class.

    :param iter table_data: Passed to AsciiTable.__init__().
    :param int column_number: Passed to AsciiTable.column_max_width().
    :param int expected: Expected return value of AsciiTable.column_max_width().
    """
    table = AsciiTable(table_data)

    if expected == IndexError:
        with pytest.raises(IndexError):
            table.column_max_width(column_number)
        return

    actual = table.column_max_width(column_number)
    assert actual == expected


def test_column_widths():
    """Test method in class."""
    assert AsciiTable([]).column_widths == list()

    table = AsciiTable(SINGLE_LINE)
    actual = table.column_widths
    assert actual == [7, 5, 9]


@pytest.mark.parametrize('table_data,terminal_width,expected', [
    ([], None, True),
    ([[]], None, True),
    ([['']], None, True),
    (SINGLE_LINE, None, True),
    (SINGLE_LINE, 30, False),
    (MULTI_LINE, None, False),
    (MULTI_LINE, 100, True),
])
def test_ok(monkeypatch, table_data, terminal_width, expected):
    """Test method in class.

    :param monkeypatch: pytest fixture.
    :param iter table_data: Passed to AsciiTable.__init__().
    :param int terminal_width: Monkeypatch width of terminal_size() if not None.
    :param bool expected: Expected return value.
    """
    if terminal_width is not None:
        monkeypatch.setattr('terminaltables.ascii_table.terminal_size', lambda: (terminal_width, 24))
    table = AsciiTable(table_data)
    actual = table.ok
    assert actual is expected


@pytest.mark.parametrize('table_data,expected', [
    ([], 2),
    ([[]], 2),
    ([['']], 4),
    ([[' ']], 5),
    (SINGLE_LINE, 31),
    (MULTI_LINE, 100),
])
def test_table_width(table_data, expected):
    """Test method in class.

    :param iter table_data: Passed to AsciiTable.__init__().
    :param int expected: Expected return value.
    """
    table = AsciiTable(table_data)
    actual = table.table_width
    assert actual == expected
