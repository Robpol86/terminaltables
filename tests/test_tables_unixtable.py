"""Test end to end showing Unix-characters table."""

from terminaltables.other_tables import UnixTable


def test_simple():
    """Simple UnixTable test."""
    table_data = [
        ['Name', 'Color', 'Type'],
        ['Avocado', 'green', 'nut'],
        ['Tomato', 'red', 'fruit'],
        ['Lettuce', 'green', 'vegetable'],
    ]
    table = UnixTable(table_data, 'Delicious Foods')

    expected = (
        '\033(0\x6c\033(BDelicious Foods\033(0\x71\x71\x77\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6b\033(B\n'
        '\033(0\x78\033(B Name    \033(0\x78\033(B Color \033(0\x78\033(B Type      \033(0\x78\033(B\n'

        '\033(0\x74\x71\x71\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71\x71\x6e\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x75\033(B\n'

        '\033(0\x78\033(B Avocado \033(0\x78\033(B green \033(0\x78\033(B nut       \033(0\x78\033(B\n'
        '\033(0\x78\033(B Tomato  \033(0\x78\033(B red   \033(0\x78\033(B fruit     \033(0\x78\033(B\n'
        '\033(0\x78\033(B Lettuce \033(0\x78\033(B green \033(0\x78\033(B vegetable \033(0\x78\033(B\n'

        '\033(0\x6d\x71\x71\x71\x71\x71\x71\x71\x71\x71\x76\x71\x71\x71\x71\x71\x71\x71\x76\x71\x71\x71\x71\x71\x71'
        '\x71\x71\x71\x71\x71\x6a\033(B'
    )
    assert table.table == expected
