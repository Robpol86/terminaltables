"""Generate simple tables in terminals from a nested list of strings.

Use SingleTable or DoubleTable instead of AsciiTable for box-drawing characters.

https://github.com/Robpol86/terminaltables
https://pypi.python.org/pypi/terminaltables
"""

from terminaltables.tables import AsciiTable  # noqa
from terminaltables.tables import DoubleTable  # noqa
from terminaltables.tables import GithubFlavoredMarkdownTable  # noqa
from terminaltables.tables import SingleTable  # noqa

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '2.1.0'
