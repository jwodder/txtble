# -*- coding: utf-8 -*-
import pytest
from   six       import text_type
from   txtble    import (
    Txtble,
    ASCII_EQ_BORDERS, LIGHT_BORDERS, HEAVY_BORDERS, DOUBLE_BORDERS, DOT_BORDERS,
)
from   test_data import HEADERS, DATA

def test_vborders_off():
    tbl = Txtble(DATA, headers=HEADERS, left_border=False, right_border=False)
    assert str(tbl) == (
        '---------+----------+------------------\n'
        'Month    |Birthstone|Birth Flower\n'
        '---------+----------+------------------\n'
        'January  |Garnet    |Carnation\n'
        'February |Amethyst  |Violet\n'
        'March    |Aquamarine|Jonquil\n'
        'April    |Diamond   |Sweetpea\n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose\n'
        'July     |Ruby      |Larkspur\n'
        'August   |Peridot   |Gladiolus\n'
        'September|Sapphire  |Aster\n'
        'October  |Opal      |Calendula\n'
        'November |Topaz     |Chrysanthemum\n'
        'December |Turquoise |Narcissus\n'
        '---------+----------+------------------'
    )

def test_vborders_off_styled():
    tbl = Txtble(
        DATA,
        headers      = HEADERS,
        border       = ASCII_EQ_BORDERS,
        left_border  = False,
        right_border = False,
    )
    assert str(tbl) == (
        '=========+==========+==================\n'
        'Month    |Birthstone|Birth Flower\n'
        '---------+----------+------------------\n'
        'January  |Garnet    |Carnation\n'
        'February |Amethyst  |Violet\n'
        'March    |Aquamarine|Jonquil\n'
        'April    |Diamond   |Sweetpea\n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose\n'
        'July     |Ruby      |Larkspur\n'
        'August   |Peridot   |Gladiolus\n'
        'September|Sapphire  |Aster\n'
        'October  |Opal      |Calendula\n'
        'November |Topaz     |Chrysanthemum\n'
        'December |Turquoise |Narcissus\n'
        '=========+==========+=================='
    )

def test_hborders_on():
    tbl = Txtble(
        DATA,
        headers       = HEADERS,
        border        = False,
        top_border    = True,
        bottom_border = True,
    )
    assert str(tbl) == (
        '---------+----------+------------------\n'
        'Month    |Birthstone|Birth Flower\n'
        '---------+----------+------------------\n'
        'January  |Garnet    |Carnation\n'
        'February |Amethyst  |Violet\n'
        'March    |Aquamarine|Jonquil\n'
        'April    |Diamond   |Sweetpea\n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose\n'
        'July     |Ruby      |Larkspur\n'
        'August   |Peridot   |Gladiolus\n'
        'September|Sapphire  |Aster\n'
        'October  |Opal      |Calendula\n'
        'November |Topaz     |Chrysanthemum\n'
        'December |Turquoise |Narcissus\n'
        '---------+----------+------------------'
    )

def test_hborders_on_styled():
    tbl = Txtble(
        DATA,
        headers       = HEADERS,
        border        = False,
        border_style  = ASCII_EQ_BORDERS,
        top_border    = True,
        bottom_border = True,
    )
    assert str(tbl) == (
        '=========+==========+==================\n'
        'Month    |Birthstone|Birth Flower\n'
        '=========+==========+==================\n'
        'January  |Garnet    |Carnation\n'
        'February |Amethyst  |Violet\n'
        'March    |Aquamarine|Jonquil\n'
        'April    |Diamond   |Sweetpea\n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose\n'
        'July     |Ruby      |Larkspur\n'
        'August   |Peridot   |Gladiolus\n'
        'September|Sapphire  |Aster\n'
        'October  |Opal      |Calendula\n'
        'November |Topaz     |Chrysanthemum\n'
        'December |Turquoise |Narcissus\n'
        '=========+==========+=================='
    )

def test_hborders_off():
    tbl = Txtble(DATA, headers=HEADERS, top_border=False, bottom_border=False)
    assert str(tbl) == (
        '|Month    |Birthstone|Birth Flower      |\n'
        '+---------+----------+------------------+\n'
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
        '|December |Turquoise |Narcissus         |'
    )

def test_ulborder():
    tbl = Txtble(DATA, headers=HEADERS, bottom_border=False, right_border=False)
    assert str(tbl) == (
        '+---------+----------+------------------\n'
        '|Month    |Birthstone|Birth Flower\n'
        '+---------+----------+------------------\n'
        '|January  |Garnet    |Carnation\n'
        '|February |Amethyst  |Violet\n'
        '|March    |Aquamarine|Jonquil\n'
        '|April    |Diamond   |Sweetpea\n'
        '|May      |Emerald   |Lily Of The Valley\n'
        '|June     |Pearl     |Rose\n'
        '|July     |Ruby      |Larkspur\n'
        '|August   |Peridot   |Gladiolus\n'
        '|September|Sapphire  |Aster\n'
        '|October  |Opal      |Calendula\n'
        '|November |Topaz     |Chrysanthemum\n'
        '|December |Turquoise |Narcissus'
    )

def test_no_right_border():
    tbl = Txtble(DATA, headers=HEADERS, right_border=False)
    assert str(tbl) == (
        '+---------+----------+------------------\n'
        '|Month    |Birthstone|Birth Flower\n'
        '+---------+----------+------------------\n'
        '|January  |Garnet    |Carnation\n'
        '|February |Amethyst  |Violet\n'
        '|March    |Aquamarine|Jonquil\n'
        '|April    |Diamond   |Sweetpea\n'
        '|May      |Emerald   |Lily Of The Valley\n'
        '|June     |Pearl     |Rose\n'
        '|July     |Ruby      |Larkspur\n'
        '|August   |Peridot   |Gladiolus\n'
        '|September|Sapphire  |Aster\n'
        '|October  |Opal      |Calendula\n'
        '|November |Topaz     |Chrysanthemum\n'
        '|December |Turquoise |Narcissus\n'
        '+---------+----------+------------------'
    )

def test_no_right_border_no_rstrip():
    tbl = Txtble(DATA, headers=HEADERS, right_border=False, rstrip=False)
    assert str(tbl) == (
        '+---------+----------+------------------\n'
        '|Month    |Birthstone|Birth Flower      \n'
        '+---------+----------+------------------\n'
        '|January  |Garnet    |Carnation         \n'
        '|February |Amethyst  |Violet            \n'
        '|March    |Aquamarine|Jonquil           \n'
        '|April    |Diamond   |Sweetpea          \n'
        '|May      |Emerald   |Lily Of The Valley\n'
        '|June     |Pearl     |Rose              \n'
        '|July     |Ruby      |Larkspur          \n'
        '|August   |Peridot   |Gladiolus         \n'
        '|September|Sapphire  |Aster             \n'
        '|October  |Opal      |Calendula         \n'
        '|November |Topaz     |Chrysanthemum     \n'
        '|December |Turquoise |Narcissus         \n'
        '+---------+----------+------------------'
    )

def test_bottom_border_only():
    tbl = Txtble(DATA, headers=HEADERS, border=False, bottom_border=True)
    assert str(tbl) == (
        'Month    |Birthstone|Birth Flower\n'
        '---------+----------+------------------\n'
        'January  |Garnet    |Carnation\n'
        'February |Amethyst  |Violet\n'
        'March    |Aquamarine|Jonquil\n'
        'April    |Diamond   |Sweetpea\n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose\n'
        'July     |Ruby      |Larkspur\n'
        'August   |Peridot   |Gladiolus\n'
        'September|Sapphire  |Aster\n'
        'October  |Opal      |Calendula\n'
        'November |Topaz     |Chrysanthemum\n'
        'December |Turquoise |Narcissus\n'
        '---------+----------+------------------'
    )

@pytest.mark.parametrize('border', [True, False, DOT_BORDERS])
def test_every_side_different_style(border):
    tbl = Txtble(
        DATA,
        headers       = HEADERS,
        border        = border,
        top_border    = HEAVY_BORDERS,
        bottom_border = ASCII_EQ_BORDERS,
        left_border   = LIGHT_BORDERS,
        right_border  = DOUBLE_BORDERS,
    )
    assert text_type(tbl) == (
        u'┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n'
        u'│Month    |Birthstone|Birth Flower      ║\n'
        u'+---------+----------+------------------+\n'
        u'│January  |Garnet    |Carnation         ║\n'
        u'│February |Amethyst  |Violet            ║\n'
        u'│March    |Aquamarine|Jonquil           ║\n'
        u'│April    |Diamond   |Sweetpea          ║\n'
        u'│May      |Emerald   |Lily Of The Valley║\n'
        u'│June     |Pearl     |Rose              ║\n'
        u'│July     |Ruby      |Larkspur          ║\n'
        u'│August   |Peridot   |Gladiolus         ║\n'
        u'│September|Sapphire  |Aster             ║\n'
        u'│October  |Opal      |Calendula         ║\n'
        u'│November |Topaz     |Chrysanthemum     ║\n'
        u'│December |Turquoise |Narcissus         ║\n'
        u'+=========+==========+==================+'
    )
