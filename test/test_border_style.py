# -*- coding: utf-8 -*-
import pytest
from   six       import text_type
from   txtble    import (
    Txtble,
    ASCII_BORDERS, ASCII_EQ_BORDERS,
    LIGHT_BORDERS, HEAVY_BORDERS, DOUBLE_BORDERS,
    DOT_BORDERS,
)
from   test_data import HEADERS, DATA, TABLE

def test_ascii_border_style():
    tbl = Txtble(DATA, headers=HEADERS, border_style=ASCII_BORDERS)
    assert str(tbl) == TABLE

def test_ascii_eq_border_style():
    tbl = Txtble(DATA, headers=HEADERS, border_style=ASCII_EQ_BORDERS)
    assert str(tbl) == (
        '+=========+==========+==================+\n'
        '|Month    |Birthstone|Birth Flower      |\n'
        '+=========+==========+==================+\n'
        '|January  |Garnet    |Carnation         |\n'
        '|February |Amethyst  |Violet            |\n'
        '|March    |Aquamarine|Jonquil           |\n'
        '|April    |Diamond   |Sweetpea          |\n'
        '|May      |Emerald   |Lily Of The Valley|\n'
        '|June     |Pearl     |Rose              |\n'
        '|July     |Ruby      |Larkspur          |\n'
        '|August   |Peridot   |Gladiolus         |\n'
        '|September|Sapphire  |Aster             |\n'
        '|October  |Opal      |Calendula         |\n'
        '|November |Topaz     |Chrysanthemum     |\n'
        '|December |Turquoise |Narcissus         |\n'
        '+=========+==========+==================+'
    )

def test_light_border_style():
    tbl = Txtble(DATA, headers=HEADERS, border_style=LIGHT_BORDERS)
    assert text_type(tbl) == (
        u'┌─────────┬──────────┬──────────────────┐\n'
        u'│Month    │Birthstone│Birth Flower      │\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'│January  │Garnet    │Carnation         │\n'
        u'│February │Amethyst  │Violet            │\n'
        u'│March    │Aquamarine│Jonquil           │\n'
        u'│April    │Diamond   │Sweetpea          │\n'
        u'│May      │Emerald   │Lily Of The Valley│\n'
        u'│June     │Pearl     │Rose              │\n'
        u'│July     │Ruby      │Larkspur          │\n'
        u'│August   │Peridot   │Gladiolus         │\n'
        u'│September│Sapphire  │Aster             │\n'
        u'│October  │Opal      │Calendula         │\n'
        u'│November │Topaz     │Chrysanthemum     │\n'
        u'│December │Turquoise │Narcissus         │\n'
        u'└─────────┴──────────┴──────────────────┘'
    )

def test_heavy_border_style():
    tbl = Txtble(DATA, headers=HEADERS, border_style=HEAVY_BORDERS)
    assert text_type(tbl) == (
        u'┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n'
        u'┃Month    ┃Birthstone┃Birth Flower      ┃\n'
        u'┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n'
        u'┃January  ┃Garnet    ┃Carnation         ┃\n'
        u'┃February ┃Amethyst  ┃Violet            ┃\n'
        u'┃March    ┃Aquamarine┃Jonquil           ┃\n'
        u'┃April    ┃Diamond   ┃Sweetpea          ┃\n'
        u'┃May      ┃Emerald   ┃Lily Of The Valley┃\n'
        u'┃June     ┃Pearl     ┃Rose              ┃\n'
        u'┃July     ┃Ruby      ┃Larkspur          ┃\n'
        u'┃August   ┃Peridot   ┃Gladiolus         ┃\n'
        u'┃September┃Sapphire  ┃Aster             ┃\n'
        u'┃October  ┃Opal      ┃Calendula         ┃\n'
        u'┃November ┃Topaz     ┃Chrysanthemum     ┃\n'
        u'┃December ┃Turquoise ┃Narcissus         ┃\n'
        u'┗━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛'
    )

def test_double_border_style():
    tbl = Txtble(DATA, headers=HEADERS, border_style=DOUBLE_BORDERS)
    assert text_type(tbl) == (
        u'╔═════════╦══════════╦══════════════════╗\n'
        u'║Month    ║Birthstone║Birth Flower      ║\n'
        u'╠═════════╬══════════╬══════════════════╣\n'
        u'║January  ║Garnet    ║Carnation         ║\n'
        u'║February ║Amethyst  ║Violet            ║\n'
        u'║March    ║Aquamarine║Jonquil           ║\n'
        u'║April    ║Diamond   ║Sweetpea          ║\n'
        u'║May      ║Emerald   ║Lily Of The Valley║\n'
        u'║June     ║Pearl     ║Rose              ║\n'
        u'║July     ║Ruby      ║Larkspur          ║\n'
        u'║August   ║Peridot   ║Gladiolus         ║\n'
        u'║September║Sapphire  ║Aster             ║\n'
        u'║October  ║Opal      ║Calendula         ║\n'
        u'║November ║Topaz     ║Chrysanthemum     ║\n'
        u'║December ║Turquoise ║Narcissus         ║\n'
        u'╚═════════╩══════════╩══════════════════╝'
    )

def test_dot_border_style():
    tbl = Txtble(DATA, headers=HEADERS, border_style=DOT_BORDERS)
    assert text_type(tbl) == (
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮Month    ⋮Birthstone⋮Birth Flower      ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮January  ⋮Garnet    ⋮Carnation         ⋮\n'
        u'⋮February ⋮Amethyst  ⋮Violet            ⋮\n'
        u'⋮March    ⋮Aquamarine⋮Jonquil           ⋮\n'
        u'⋮April    ⋮Diamond   ⋮Sweetpea          ⋮\n'
        u'⋮May      ⋮Emerald   ⋮Lily Of The Valley⋮\n'
        u'⋮June     ⋮Pearl     ⋮Rose              ⋮\n'
        u'⋮July     ⋮Ruby      ⋮Larkspur          ⋮\n'
        u'⋮August   ⋮Peridot   ⋮Gladiolus         ⋮\n'
        u'⋮September⋮Sapphire  ⋮Aster             ⋮\n'
        u'⋮October  ⋮Opal      ⋮Calendula         ⋮\n'
        u'⋮November ⋮Topaz     ⋮Chrysanthemum     ⋮\n'
        u'⋮December ⋮Turquoise ⋮Narcissus         ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·'
    )

def test_ascii_eq_header_border_row_border():
    tbl = Txtble(
        DATA,
        header_border = ASCII_EQ_BORDERS,
        headers       = HEADERS,
        row_border    = True,
    )
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|Month    |Birthstone|Birth Flower      |\n'
        '+=========+==========+==================+\n'
        '|January  |Garnet    |Carnation         |\n'
        '+---------+----------+------------------+\n'
        '|February |Amethyst  |Violet            |\n'
        '+---------+----------+------------------+\n'
        '|March    |Aquamarine|Jonquil           |\n'
        '+---------+----------+------------------+\n'
        '|April    |Diamond   |Sweetpea          |\n'
        '+---------+----------+------------------+\n'
        '|May      |Emerald   |Lily Of The Valley|\n'
        '+---------+----------+------------------+\n'
        '|June     |Pearl     |Rose              |\n'
        '+---------+----------+------------------+\n'
        '|July     |Ruby      |Larkspur          |\n'
        '+---------+----------+------------------+\n'
        '|August   |Peridot   |Gladiolus         |\n'
        '+---------+----------+------------------+\n'
        '|September|Sapphire  |Aster             |\n'
        '+---------+----------+------------------+\n'
        '|October  |Opal      |Calendula         |\n'
        '+---------+----------+------------------+\n'
        '|November |Topaz     |Chrysanthemum     |\n'
        '+---------+----------+------------------+\n'
        '|December |Turquoise |Narcissus         |\n'
        '+---------+----------+------------------+'
    )

def test_every_border_different():
    tbl = Txtble(
        DATA,
        border        = ASCII_BORDERS,
        column_border = HEAVY_BORDERS,
        header_border = DOUBLE_BORDERS,
        headers       = HEADERS,
        row_border    = LIGHT_BORDERS,
    )
    assert text_type(tbl) == (
        u'+---------+----------+------------------+\n'
        u'|Month    ┃Birthstone┃Birth Flower      |\n'
        u'╠═════════╬══════════╬══════════════════╣\n'
        u'|January  ┃Garnet    ┃Carnation         |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|February ┃Amethyst  ┃Violet            |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|March    ┃Aquamarine┃Jonquil           |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|April    ┃Diamond   ┃Sweetpea          |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|May      ┃Emerald   ┃Lily Of The Valley|\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|June     ┃Pearl     ┃Rose              |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|July     ┃Ruby      ┃Larkspur          |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|August   ┃Peridot   ┃Gladiolus         |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|September┃Sapphire  ┃Aster             |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|October  ┃Opal      ┃Calendula         |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|November ┃Topaz     ┃Chrysanthemum     |\n'
        u'├─────────┼──────────┼──────────────────┤\n'
        u'|December ┃Turquoise ┃Narcissus         |\n'
        u'+---------+----------+------------------+'
    )

def test_every_inner_border_different():
    tbl = Txtble(
        DATA,
        border        = False,
        column_border = HEAVY_BORDERS,
        header_border = DOUBLE_BORDERS,
        headers       = HEADERS,
        row_border    = LIGHT_BORDERS,
    )
    assert text_type(tbl) == (
        u'Month    ┃Birthstone┃Birth Flower\n'
        u'═════════╬══════════╬══════════════════\n'
        u'January  ┃Garnet    ┃Carnation\n'
        u'─────────┼──────────┼──────────────────\n'
        u'February ┃Amethyst  ┃Violet\n'
        u'─────────┼──────────┼──────────────────\n'
        u'March    ┃Aquamarine┃Jonquil\n'
        u'─────────┼──────────┼──────────────────\n'
        u'April    ┃Diamond   ┃Sweetpea\n'
        u'─────────┼──────────┼──────────────────\n'
        u'May      ┃Emerald   ┃Lily Of The Valley\n'
        u'─────────┼──────────┼──────────────────\n'
        u'June     ┃Pearl     ┃Rose\n'
        u'─────────┼──────────┼──────────────────\n'
        u'July     ┃Ruby      ┃Larkspur\n'
        u'─────────┼──────────┼──────────────────\n'
        u'August   ┃Peridot   ┃Gladiolus\n'
        u'─────────┼──────────┼──────────────────\n'
        u'September┃Sapphire  ┃Aster\n'
        u'─────────┼──────────┼──────────────────\n'
        u'October  ┃Opal      ┃Calendula\n'
        u'─────────┼──────────┼──────────────────\n'
        u'November ┃Topaz     ┃Chrysanthemum\n'
        u'─────────┼──────────┼──────────────────\n'
        u'December ┃Turquoise ┃Narcissus'
    )

def test_border_style_overridden():
    tbl = Txtble(
        DATA,
        border        = LIGHT_BORDERS,
        border_style  = DOT_BORDERS,
        column_border = HEAVY_BORDERS,
        header_border = DOUBLE_BORDERS,
        headers       = HEADERS,
    )
    assert text_type(tbl) == (
        u'┌─────────┬──────────┬──────────────────┐\n'
        u'│Month    ┃Birthstone┃Birth Flower      │\n'
        u'╠═════════╬══════════╬══════════════════╣\n'
        u'│January  ┃Garnet    ┃Carnation         │\n'
        u'│February ┃Amethyst  ┃Violet            │\n'
        u'│March    ┃Aquamarine┃Jonquil           │\n'
        u'│April    ┃Diamond   ┃Sweetpea          │\n'
        u'│May      ┃Emerald   ┃Lily Of The Valley│\n'
        u'│June     ┃Pearl     ┃Rose              │\n'
        u'│July     ┃Ruby      ┃Larkspur          │\n'
        u'│August   ┃Peridot   ┃Gladiolus         │\n'
        u'│September┃Sapphire  ┃Aster             │\n'
        u'│October  ┃Opal      ┃Calendula         │\n'
        u'│November ┃Topaz     ┃Chrysanthemum     │\n'
        u'│December ┃Turquoise ┃Narcissus         │\n'
        u'└─────────┴──────────┴──────────────────┘'
    )

def test_border_style_mixed_overrides():
    tbl = Txtble(
        DATA,
        border_style  = DOT_BORDERS,
        column_border = False,
        header_border = ASCII_EQ_BORDERS,
        headers       = HEADERS,
        row_border    = True,
    )
    assert text_type(tbl) == (
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮Month    BirthstoneBirth Flower      ⋮\n'
        u'+=====================================+\n'
        u'⋮January  Garnet    Carnation         ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮February Amethyst  Violet            ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮March    AquamarineJonquil           ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮April    Diamond   Sweetpea          ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮May      Emerald   Lily Of The Valley⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮June     Pearl     Rose              ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮July     Ruby      Larkspur          ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮August   Peridot   Gladiolus         ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮SeptemberSapphire  Aster             ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮October  Opal      Calendula         ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮November Topaz     Chrysanthemum     ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n'
        u'⋮December Turquoise Narcissus         ⋮\n'
        u'·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·'
    )

@pytest.mark.parametrize('border_style', [
    None,
    False,
    True,
    tuple('-|+++++++++'),
])
def test_bad_border_style(border_style):
    tbl = Txtble(DATA, border_style=border_style)
    with pytest.raises(
        TypeError,
        match='border_style must be a BorderStyle instance',
    ):
        str(tbl)

def test_border_vs_header_border_style():
    tbl = Txtble(DATA, border=HEAVY_BORDERS, header_border=DOUBLE_BORDERS)
    assert text_type(tbl) == (
        u'┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n'
        u'┃January  |Garnet    |Carnation         ┃\n'
        u'┃February |Amethyst  |Violet            ┃\n'
        u'┃March    |Aquamarine|Jonquil           ┃\n'
        u'┃April    |Diamond   |Sweetpea          ┃\n'
        u'┃May      |Emerald   |Lily Of The Valley┃\n'
        u'┃June     |Pearl     |Rose              ┃\n'
        u'┃July     |Ruby      |Larkspur          ┃\n'
        u'┃August   |Peridot   |Gladiolus         ┃\n'
        u'┃September|Sapphire  |Aster             ┃\n'
        u'┃October  |Opal      |Calendula         ┃\n'
        u'┃November |Topaz     |Chrysanthemum     ┃\n'
        u'┃December |Turquoise |Narcissus         ┃\n'
        u'┗━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛'
    )

def test_top_border_vs_header_border_style():
    tbl = Txtble(DATA, top_border=HEAVY_BORDERS, header_border=DOUBLE_BORDERS)
    assert text_type(tbl) == (
        u'┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n'
        u'|January  |Garnet    |Carnation         |\n'
        u'|February |Amethyst  |Violet            |\n'
        u'|March    |Aquamarine|Jonquil           |\n'
        u'|April    |Diamond   |Sweetpea          |\n'
        u'|May      |Emerald   |Lily Of The Valley|\n'
        u'|June     |Pearl     |Rose              |\n'
        u'|July     |Ruby      |Larkspur          |\n'
        u'|August   |Peridot   |Gladiolus         |\n'
        u'|September|Sapphire  |Aster             |\n'
        u'|October  |Opal      |Calendula         |\n'
        u'|November |Topaz     |Chrysanthemum     |\n'
        u'|December |Turquoise |Narcissus         |\n'
        u'+---------+----------+------------------+'
    )

def test_no_border_header_border_style():
    tbl = Txtble(DATA, border=False, header_border=DOUBLE_BORDERS)
    assert text_type(tbl) == (
        u'═════════╦══════════╦══════════════════\n'
        u'January  |Garnet    |Carnation\n'
        u'February |Amethyst  |Violet\n'
        u'March    |Aquamarine|Jonquil\n'
        u'April    |Diamond   |Sweetpea\n'
        u'May      |Emerald   |Lily Of The Valley\n'
        u'June     |Pearl     |Rose\n'
        u'July     |Ruby      |Larkspur\n'
        u'August   |Peridot   |Gladiolus\n'
        u'September|Sapphire  |Aster\n'
        u'October  |Opal      |Calendula\n'
        u'November |Topaz     |Chrysanthemum\n'
        u'December |Turquoise |Narcissus'
    )

def test_no_top_border_header_border_style():
    tbl = Txtble(DATA, top_border=False, header_border=DOUBLE_BORDERS)
    assert text_type(tbl) == (
        u'╔═════════╦══════════╦══════════════════╗\n'
        u'|January  |Garnet    |Carnation         |\n'
        u'|February |Amethyst  |Violet            |\n'
        u'|March    |Aquamarine|Jonquil           |\n'
        u'|April    |Diamond   |Sweetpea          |\n'
        u'|May      |Emerald   |Lily Of The Valley|\n'
        u'|June     |Pearl     |Rose              |\n'
        u'|July     |Ruby      |Larkspur          |\n'
        u'|August   |Peridot   |Gladiolus         |\n'
        u'|September|Sapphire  |Aster             |\n'
        u'|October  |Opal      |Calendula         |\n'
        u'|November |Topaz     |Chrysanthemum     |\n'
        u'|December |Turquoise |Narcissus         |\n'
        u'+---------+----------+------------------+'
    )
