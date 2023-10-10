from __future__ import annotations
import pytest
from test_data import DATA, HEADERS
from txtble import (
    ASCII_EQ_BORDERS,
    DOT_BORDERS,
    DOUBLE_BORDERS,
    HEAVY_BORDERS,
    LIGHT_BORDERS,
    BorderStyle,
    Txtble,
)


def test_vborders_off() -> None:
    tbl = Txtble(DATA, headers=HEADERS, left_border=False, right_border=False)
    assert str(tbl) == (
        "---------+----------+------------------\n"
        "Month    |Birthstone|Birth Flower\n"
        "---------+----------+------------------\n"
        "January  |Garnet    |Carnation\n"
        "February |Amethyst  |Violet\n"
        "March    |Aquamarine|Jonquil\n"
        "April    |Diamond   |Sweetpea\n"
        "May      |Emerald   |Lily Of The Valley\n"
        "June     |Pearl     |Rose\n"
        "July     |Ruby      |Larkspur\n"
        "August   |Peridot   |Gladiolus\n"
        "September|Sapphire  |Aster\n"
        "October  |Opal      |Calendula\n"
        "November |Topaz     |Chrysanthemum\n"
        "December |Turquoise |Narcissus\n"
        "---------+----------+------------------"
    )


def test_vborders_off_styled() -> None:
    tbl = Txtble(
        DATA,
        headers=HEADERS,
        border=ASCII_EQ_BORDERS,
        left_border=False,
        right_border=False,
    )
    assert str(tbl) == (
        "=========+==========+==================\n"
        "Month    |Birthstone|Birth Flower\n"
        "---------+----------+------------------\n"
        "January  |Garnet    |Carnation\n"
        "February |Amethyst  |Violet\n"
        "March    |Aquamarine|Jonquil\n"
        "April    |Diamond   |Sweetpea\n"
        "May      |Emerald   |Lily Of The Valley\n"
        "June     |Pearl     |Rose\n"
        "July     |Ruby      |Larkspur\n"
        "August   |Peridot   |Gladiolus\n"
        "September|Sapphire  |Aster\n"
        "October  |Opal      |Calendula\n"
        "November |Topaz     |Chrysanthemum\n"
        "December |Turquoise |Narcissus\n"
        "=========+==========+=================="
    )


def test_hborders_on() -> None:
    tbl = Txtble(
        DATA,
        headers=HEADERS,
        border=False,
        top_border=True,
        bottom_border=True,
    )
    assert str(tbl) == (
        "---------+----------+------------------\n"
        "Month    |Birthstone|Birth Flower\n"
        "---------+----------+------------------\n"
        "January  |Garnet    |Carnation\n"
        "February |Amethyst  |Violet\n"
        "March    |Aquamarine|Jonquil\n"
        "April    |Diamond   |Sweetpea\n"
        "May      |Emerald   |Lily Of The Valley\n"
        "June     |Pearl     |Rose\n"
        "July     |Ruby      |Larkspur\n"
        "August   |Peridot   |Gladiolus\n"
        "September|Sapphire  |Aster\n"
        "October  |Opal      |Calendula\n"
        "November |Topaz     |Chrysanthemum\n"
        "December |Turquoise |Narcissus\n"
        "---------+----------+------------------"
    )


def test_hborders_on_styled() -> None:
    tbl = Txtble(
        DATA,
        headers=HEADERS,
        border=False,
        border_style=ASCII_EQ_BORDERS,
        top_border=True,
        bottom_border=True,
    )
    assert str(tbl) == (
        "=========+==========+==================\n"
        "Month    |Birthstone|Birth Flower\n"
        "=========+==========+==================\n"
        "January  |Garnet    |Carnation\n"
        "February |Amethyst  |Violet\n"
        "March    |Aquamarine|Jonquil\n"
        "April    |Diamond   |Sweetpea\n"
        "May      |Emerald   |Lily Of The Valley\n"
        "June     |Pearl     |Rose\n"
        "July     |Ruby      |Larkspur\n"
        "August   |Peridot   |Gladiolus\n"
        "September|Sapphire  |Aster\n"
        "October  |Opal      |Calendula\n"
        "November |Topaz     |Chrysanthemum\n"
        "December |Turquoise |Narcissus\n"
        "=========+==========+=================="
    )


def test_hborders_off() -> None:
    tbl = Txtble(DATA, headers=HEADERS, top_border=False, bottom_border=False)
    assert str(tbl) == (
        "|Month    |Birthstone|Birth Flower      |\n"
        "+---------+----------+------------------+\n"
        "|January  |Garnet    |Carnation         |\n"
        "|February |Amethyst  |Violet            |\n"
        "|March    |Aquamarine|Jonquil           |\n"
        "|April    |Diamond   |Sweetpea          |\n"
        "|May      |Emerald   |Lily Of The Valley|\n"
        "|June     |Pearl     |Rose              |\n"
        "|July     |Ruby      |Larkspur          |\n"
        "|August   |Peridot   |Gladiolus         |\n"
        "|September|Sapphire  |Aster             |\n"
        "|October  |Opal      |Calendula         |\n"
        "|November |Topaz     |Chrysanthemum     |\n"
        "|December |Turquoise |Narcissus         |"
    )


def test_ulborder() -> None:
    tbl = Txtble(DATA, headers=HEADERS, bottom_border=False, right_border=False)
    assert str(tbl) == (
        "+---------+----------+------------------\n"
        "|Month    |Birthstone|Birth Flower\n"
        "+---------+----------+------------------\n"
        "|January  |Garnet    |Carnation\n"
        "|February |Amethyst  |Violet\n"
        "|March    |Aquamarine|Jonquil\n"
        "|April    |Diamond   |Sweetpea\n"
        "|May      |Emerald   |Lily Of The Valley\n"
        "|June     |Pearl     |Rose\n"
        "|July     |Ruby      |Larkspur\n"
        "|August   |Peridot   |Gladiolus\n"
        "|September|Sapphire  |Aster\n"
        "|October  |Opal      |Calendula\n"
        "|November |Topaz     |Chrysanthemum\n"
        "|December |Turquoise |Narcissus"
    )


def test_no_right_border() -> None:
    tbl = Txtble(DATA, headers=HEADERS, right_border=False)
    assert str(tbl) == (
        "+---------+----------+------------------\n"
        "|Month    |Birthstone|Birth Flower\n"
        "+---------+----------+------------------\n"
        "|January  |Garnet    |Carnation\n"
        "|February |Amethyst  |Violet\n"
        "|March    |Aquamarine|Jonquil\n"
        "|April    |Diamond   |Sweetpea\n"
        "|May      |Emerald   |Lily Of The Valley\n"
        "|June     |Pearl     |Rose\n"
        "|July     |Ruby      |Larkspur\n"
        "|August   |Peridot   |Gladiolus\n"
        "|September|Sapphire  |Aster\n"
        "|October  |Opal      |Calendula\n"
        "|November |Topaz     |Chrysanthemum\n"
        "|December |Turquoise |Narcissus\n"
        "+---------+----------+------------------"
    )


def test_no_right_border_no_rstrip() -> None:
    tbl = Txtble(DATA, headers=HEADERS, right_border=False, rstrip=False)
    assert str(tbl) == (
        "+---------+----------+------------------\n"
        "|Month    |Birthstone|Birth Flower      \n"
        "+---------+----------+------------------\n"
        "|January  |Garnet    |Carnation         \n"
        "|February |Amethyst  |Violet            \n"
        "|March    |Aquamarine|Jonquil           \n"
        "|April    |Diamond   |Sweetpea          \n"
        "|May      |Emerald   |Lily Of The Valley\n"
        "|June     |Pearl     |Rose              \n"
        "|July     |Ruby      |Larkspur          \n"
        "|August   |Peridot   |Gladiolus         \n"
        "|September|Sapphire  |Aster             \n"
        "|October  |Opal      |Calendula         \n"
        "|November |Topaz     |Chrysanthemum     \n"
        "|December |Turquoise |Narcissus         \n"
        "+---------+----------+------------------"
    )


def test_bottom_border_only() -> None:
    tbl = Txtble(DATA, headers=HEADERS, border=False, bottom_border=True)
    assert str(tbl) == (
        "Month    |Birthstone|Birth Flower\n"
        "---------+----------+------------------\n"
        "January  |Garnet    |Carnation\n"
        "February |Amethyst  |Violet\n"
        "March    |Aquamarine|Jonquil\n"
        "April    |Diamond   |Sweetpea\n"
        "May      |Emerald   |Lily Of The Valley\n"
        "June     |Pearl     |Rose\n"
        "July     |Ruby      |Larkspur\n"
        "August   |Peridot   |Gladiolus\n"
        "September|Sapphire  |Aster\n"
        "October  |Opal      |Calendula\n"
        "November |Topaz     |Chrysanthemum\n"
        "December |Turquoise |Narcissus\n"
        "---------+----------+------------------"
    )


@pytest.mark.parametrize("border", [True, False, DOT_BORDERS])
def test_every_side_different_style(border: bool | BorderStyle) -> None:
    tbl = Txtble(
        DATA,
        headers=HEADERS,
        border=border,
        top_border=HEAVY_BORDERS,
        bottom_border=ASCII_EQ_BORDERS,
        left_border=LIGHT_BORDERS,
        right_border=DOUBLE_BORDERS,
    )
    assert str(tbl) == (
        "┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n"
        "│Month    |Birthstone|Birth Flower      ║\n"
        "+---------+----------+------------------+\n"
        "│January  |Garnet    |Carnation         ║\n"
        "│February |Amethyst  |Violet            ║\n"
        "│March    |Aquamarine|Jonquil           ║\n"
        "│April    |Diamond   |Sweetpea          ║\n"
        "│May      |Emerald   |Lily Of The Valley║\n"
        "│June     |Pearl     |Rose              ║\n"
        "│July     |Ruby      |Larkspur          ║\n"
        "│August   |Peridot   |Gladiolus         ║\n"
        "│September|Sapphire  |Aster             ║\n"
        "│October  |Opal      |Calendula         ║\n"
        "│November |Topaz     |Chrysanthemum     ║\n"
        "│December |Turquoise |Narcissus         ║\n"
        "+=========+==========+==================+"
    )
