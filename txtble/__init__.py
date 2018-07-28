"""
Yet another plain-text table typesetter

``txtble`` is yet another Python library for creating plain-text tables.  (All
the good names were taken, OK?)  Pass in a list of lists of strings (or other
stringable things) and get out something nice like::

    +---------+----------+------------------+
    |Month    |Birthstone|Birth Flower      |
    +---------+----------+------------------+
    |January  |Garnet    |Carnation         |
    |February |Amethyst  |Violet            |
    |March    |Aquamarine|Jonquil           |
    |April    |Diamond   |Sweetpea          |
    |May      |Emerald   |Lily Of The Valley|
    |June     |Pearl     |Rose              |
    |July     |Ruby      |Larkspur          |
    |August   |Peridot   |Gladiolus         |
    |September|Sapphire  |Aster             |
    |October  |Opal      |Calendula         |
    |November |Topaz     |Chrysanthemum     |
    |December |Turquoise |Narcissus         |
    +---------+----------+------------------+

Visit <https://github.com/jwodder/txtble> for more information.
"""

from .border_style import (
    BorderStyle, ASCII_BORDERS, ASCII_EQ_BORDERS, DOT_BORDERS, DOUBLE_BORDERS,
    HEAVY_BORDERS, LIGHT_BORDERS,
)
from .classes      import Txtble
from .errors       import IndeterminateWidthError, UnterminatedColorError
from .util         import with_color_stripped

__version__      = '0.9.0'
__author__       = 'John Thorvald Wodder II'
__author_email__ = 'txtble@varonathe.org'
__license__      = 'MIT'
__url__          = 'https://github.com/jwodder/txtble'

__all__ = [
    'ASCII_BORDERS',
    'ASCII_EQ_BORDERS',
    'BorderStyle',
    'DOT_BORDERS',
    'DOUBLE_BORDERS',
    'HEAVY_BORDERS',
    'IndeterminateWidthError',
    'LIGHT_BORDERS',
    'Txtble',
    'UnterminatedColorError',
    'with_color_stripped',
]
