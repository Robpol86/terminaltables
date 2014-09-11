import pytest

import terminaltables


@pytest.fixture(autouse=True, scope='session')
def override_terminal_width():
    terminaltables.terminal_width = lambda: 80
