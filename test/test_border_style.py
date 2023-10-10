from __future__ import annotations
import pytest
from test_data import DATA, HEADERS, TABLE
from txtble import (
    ASCII_BORDERS,
    ASCII_EQ_BORDERS,
    DOT_BORDERS,
    DOUBLE_BORDERS,
    HEAVY_BORDERS,
    LIGHT_BORDERS,
    Txtble,
)


def test_ascii_border_style() -> None:
    tbl = Txtble(DATA, headers=HEADERS, border_style=ASCII_BORDERS)
    assert str(tbl) == TABLE


def test_ascii_eq_border_style() -> None:
    tbl = Txtble(DATA, headers=HEADERS, border_style=ASCII_EQ_BORDERS)
    assert str(tbl) == (
        "+=========+==========+==================+\n"
        "|Month    |Birthstone|Birth Flower      |\n"
        "+=========+==========+==================+\n"
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
        "|December |Turquoise |Narcissus         |\n"
        "+=========+==========+==================+"
    )


def test_light_border_style() -> None:
    tbl = Txtble(DATA, headers=HEADERS, border_style=LIGHT_BORDERS)
    assert str(tbl) == (
        "┌─────────┬──────────┬──────────────────┐\n"
        "│Month    │Birthstone│Birth Flower      │\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "│January  │Garnet    │Carnation         │\n"
        "│February │Amethyst  │Violet            │\n"
        "│March    │Aquamarine│Jonquil           │\n"
        "│April    │Diamond   │Sweetpea          │\n"
        "│May      │Emerald   │Lily Of The Valley│\n"
        "│June     │Pearl     │Rose              │\n"
        "│July     │Ruby      │Larkspur          │\n"
        "│August   │Peridot   │Gladiolus         │\n"
        "│September│Sapphire  │Aster             │\n"
        "│October  │Opal      │Calendula         │\n"
        "│November │Topaz     │Chrysanthemum     │\n"
        "│December │Turquoise │Narcissus         │\n"
        "└─────────┴──────────┴──────────────────┘"
    )


def test_heavy_border_style() -> None:
    tbl = Txtble(DATA, headers=HEADERS, border_style=HEAVY_BORDERS)
    assert str(tbl) == (
        "┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n"
        "┃Month    ┃Birthstone┃Birth Flower      ┃\n"
        "┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n"
        "┃January  ┃Garnet    ┃Carnation         ┃\n"
        "┃February ┃Amethyst  ┃Violet            ┃\n"
        "┃March    ┃Aquamarine┃Jonquil           ┃\n"
        "┃April    ┃Diamond   ┃Sweetpea          ┃\n"
        "┃May      ┃Emerald   ┃Lily Of The Valley┃\n"
        "┃June     ┃Pearl     ┃Rose              ┃\n"
        "┃July     ┃Ruby      ┃Larkspur          ┃\n"
        "┃August   ┃Peridot   ┃Gladiolus         ┃\n"
        "┃September┃Sapphire  ┃Aster             ┃\n"
        "┃October  ┃Opal      ┃Calendula         ┃\n"
        "┃November ┃Topaz     ┃Chrysanthemum     ┃\n"
        "┃December ┃Turquoise ┃Narcissus         ┃\n"
        "┗━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛"
    )


def test_double_border_style() -> None:
    tbl = Txtble(DATA, headers=HEADERS, border_style=DOUBLE_BORDERS)
    assert str(tbl) == (
        "╔═════════╦══════════╦══════════════════╗\n"
        "║Month    ║Birthstone║Birth Flower      ║\n"
        "╠═════════╬══════════╬══════════════════╣\n"
        "║January  ║Garnet    ║Carnation         ║\n"
        "║February ║Amethyst  ║Violet            ║\n"
        "║March    ║Aquamarine║Jonquil           ║\n"
        "║April    ║Diamond   ║Sweetpea          ║\n"
        "║May      ║Emerald   ║Lily Of The Valley║\n"
        "║June     ║Pearl     ║Rose              ║\n"
        "║July     ║Ruby      ║Larkspur          ║\n"
        "║August   ║Peridot   ║Gladiolus         ║\n"
        "║September║Sapphire  ║Aster             ║\n"
        "║October  ║Opal      ║Calendula         ║\n"
        "║November ║Topaz     ║Chrysanthemum     ║\n"
        "║December ║Turquoise ║Narcissus         ║\n"
        "╚═════════╩══════════╩══════════════════╝"
    )


def test_dot_border_style() -> None:
    tbl = Txtble(DATA, headers=HEADERS, border_style=DOT_BORDERS)
    assert str(tbl) == (
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮Month    ⋮Birthstone⋮Birth Flower      ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮January  ⋮Garnet    ⋮Carnation         ⋮\n"
        "⋮February ⋮Amethyst  ⋮Violet            ⋮\n"
        "⋮March    ⋮Aquamarine⋮Jonquil           ⋮\n"
        "⋮April    ⋮Diamond   ⋮Sweetpea          ⋮\n"
        "⋮May      ⋮Emerald   ⋮Lily Of The Valley⋮\n"
        "⋮June     ⋮Pearl     ⋮Rose              ⋮\n"
        "⋮July     ⋮Ruby      ⋮Larkspur          ⋮\n"
        "⋮August   ⋮Peridot   ⋮Gladiolus         ⋮\n"
        "⋮September⋮Sapphire  ⋮Aster             ⋮\n"
        "⋮October  ⋮Opal      ⋮Calendula         ⋮\n"
        "⋮November ⋮Topaz     ⋮Chrysanthemum     ⋮\n"
        "⋮December ⋮Turquoise ⋮Narcissus         ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·"
    )


def test_ascii_eq_header_border_row_border() -> None:
    tbl = Txtble(
        DATA,
        header_border=ASCII_EQ_BORDERS,
        headers=HEADERS,
        row_border=True,
    )
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|Month    |Birthstone|Birth Flower      |\n"
        "+=========+==========+==================+\n"
        "|January  |Garnet    |Carnation         |\n"
        "+---------+----------+------------------+\n"
        "|February |Amethyst  |Violet            |\n"
        "+---------+----------+------------------+\n"
        "|March    |Aquamarine|Jonquil           |\n"
        "+---------+----------+------------------+\n"
        "|April    |Diamond   |Sweetpea          |\n"
        "+---------+----------+------------------+\n"
        "|May      |Emerald   |Lily Of The Valley|\n"
        "+---------+----------+------------------+\n"
        "|June     |Pearl     |Rose              |\n"
        "+---------+----------+------------------+\n"
        "|July     |Ruby      |Larkspur          |\n"
        "+---------+----------+------------------+\n"
        "|August   |Peridot   |Gladiolus         |\n"
        "+---------+----------+------------------+\n"
        "|September|Sapphire  |Aster             |\n"
        "+---------+----------+------------------+\n"
        "|October  |Opal      |Calendula         |\n"
        "+---------+----------+------------------+\n"
        "|November |Topaz     |Chrysanthemum     |\n"
        "+---------+----------+------------------+\n"
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_every_border_different() -> None:
    tbl = Txtble(
        DATA,
        border=ASCII_BORDERS,
        column_border=HEAVY_BORDERS,
        header_border=DOUBLE_BORDERS,
        headers=HEADERS,
        row_border=LIGHT_BORDERS,
    )
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|Month    ┃Birthstone┃Birth Flower      |\n"
        "╠═════════╬══════════╬══════════════════╣\n"
        "|January  ┃Garnet    ┃Carnation         |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|February ┃Amethyst  ┃Violet            |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|March    ┃Aquamarine┃Jonquil           |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|April    ┃Diamond   ┃Sweetpea          |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|May      ┃Emerald   ┃Lily Of The Valley|\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|June     ┃Pearl     ┃Rose              |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|July     ┃Ruby      ┃Larkspur          |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|August   ┃Peridot   ┃Gladiolus         |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|September┃Sapphire  ┃Aster             |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|October  ┃Opal      ┃Calendula         |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|November ┃Topaz     ┃Chrysanthemum     |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|December ┃Turquoise ┃Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_every_inner_border_different() -> None:
    tbl = Txtble(
        DATA,
        border=False,
        column_border=HEAVY_BORDERS,
        header_border=DOUBLE_BORDERS,
        headers=HEADERS,
        row_border=LIGHT_BORDERS,
    )
    assert str(tbl) == (
        "Month    ┃Birthstone┃Birth Flower\n"
        "═════════╬══════════╬══════════════════\n"
        "January  ┃Garnet    ┃Carnation\n"
        "─────────┼──────────┼──────────────────\n"
        "February ┃Amethyst  ┃Violet\n"
        "─────────┼──────────┼──────────────────\n"
        "March    ┃Aquamarine┃Jonquil\n"
        "─────────┼──────────┼──────────────────\n"
        "April    ┃Diamond   ┃Sweetpea\n"
        "─────────┼──────────┼──────────────────\n"
        "May      ┃Emerald   ┃Lily Of The Valley\n"
        "─────────┼──────────┼──────────────────\n"
        "June     ┃Pearl     ┃Rose\n"
        "─────────┼──────────┼──────────────────\n"
        "July     ┃Ruby      ┃Larkspur\n"
        "─────────┼──────────┼──────────────────\n"
        "August   ┃Peridot   ┃Gladiolus\n"
        "─────────┼──────────┼──────────────────\n"
        "September┃Sapphire  ┃Aster\n"
        "─────────┼──────────┼──────────────────\n"
        "October  ┃Opal      ┃Calendula\n"
        "─────────┼──────────┼──────────────────\n"
        "November ┃Topaz     ┃Chrysanthemum\n"
        "─────────┼──────────┼──────────────────\n"
        "December ┃Turquoise ┃Narcissus"
    )


def test_border_style_overridden() -> None:
    tbl = Txtble(
        DATA,
        border=LIGHT_BORDERS,
        border_style=DOT_BORDERS,
        column_border=HEAVY_BORDERS,
        header_border=DOUBLE_BORDERS,
        headers=HEADERS,
    )
    assert str(tbl) == (
        "┌─────────┬──────────┬──────────────────┐\n"
        "│Month    ┃Birthstone┃Birth Flower      │\n"
        "╠═════════╬══════════╬══════════════════╣\n"
        "│January  ┃Garnet    ┃Carnation         │\n"
        "│February ┃Amethyst  ┃Violet            │\n"
        "│March    ┃Aquamarine┃Jonquil           │\n"
        "│April    ┃Diamond   ┃Sweetpea          │\n"
        "│May      ┃Emerald   ┃Lily Of The Valley│\n"
        "│June     ┃Pearl     ┃Rose              │\n"
        "│July     ┃Ruby      ┃Larkspur          │\n"
        "│August   ┃Peridot   ┃Gladiolus         │\n"
        "│September┃Sapphire  ┃Aster             │\n"
        "│October  ┃Opal      ┃Calendula         │\n"
        "│November ┃Topaz     ┃Chrysanthemum     │\n"
        "│December ┃Turquoise ┃Narcissus         │\n"
        "└─────────┴──────────┴──────────────────┘"
    )


def test_border_style_mixed_overrides() -> None:
    tbl = Txtble(
        DATA,
        border_style=DOT_BORDERS,
        column_border=False,
        header_border=ASCII_EQ_BORDERS,
        headers=HEADERS,
        row_border=True,
    )
    assert str(tbl) == (
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮Month    BirthstoneBirth Flower      ⋮\n"
        "+=====================================+\n"
        "⋮January  Garnet    Carnation         ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮February Amethyst  Violet            ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮March    AquamarineJonquil           ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮April    Diamond   Sweetpea          ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮May      Emerald   Lily Of The Valley⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮June     Pearl     Rose              ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮July     Ruby      Larkspur          ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮August   Peridot   Gladiolus         ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮SeptemberSapphire  Aster             ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮October  Opal      Calendula         ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮November Topaz     Chrysanthemum     ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·\n"
        "⋮December Turquoise Narcissus         ⋮\n"
        "·⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯·"
    )


@pytest.mark.parametrize(
    "border_style",
    [
        None,
        False,
        True,
        tuple("-|+++++++++"),
    ],
)
def test_bad_border_style(border_style: bool | tuple[str] | None) -> None:
    tbl = Txtble(DATA, border_style=border_style)  # type: ignore[arg-type]
    with pytest.raises(
        TypeError,
        match="border_style must be a BorderStyle instance",
    ):
        str(tbl)


def test_border_vs_header_border_style() -> None:
    tbl = Txtble(DATA, border=HEAVY_BORDERS, header_border=DOUBLE_BORDERS)
    assert str(tbl) == (
        "┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n"
        "┃January  |Garnet    |Carnation         ┃\n"
        "┃February |Amethyst  |Violet            ┃\n"
        "┃March    |Aquamarine|Jonquil           ┃\n"
        "┃April    |Diamond   |Sweetpea          ┃\n"
        "┃May      |Emerald   |Lily Of The Valley┃\n"
        "┃June     |Pearl     |Rose              ┃\n"
        "┃July     |Ruby      |Larkspur          ┃\n"
        "┃August   |Peridot   |Gladiolus         ┃\n"
        "┃September|Sapphire  |Aster             ┃\n"
        "┃October  |Opal      |Calendula         ┃\n"
        "┃November |Topaz     |Chrysanthemum     ┃\n"
        "┃December |Turquoise |Narcissus         ┃\n"
        "┗━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛"
    )


def test_top_border_vs_header_border_style() -> None:
    tbl = Txtble(DATA, top_border=HEAVY_BORDERS, header_border=DOUBLE_BORDERS)
    assert str(tbl) == (
        "┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n"
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
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_no_border_header_border_style() -> None:
    tbl = Txtble(DATA, border=False, header_border=DOUBLE_BORDERS)
    assert str(tbl) == (
        "═════════╦══════════╦══════════════════\n"
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
        "December |Turquoise |Narcissus"
    )


def test_no_top_border_header_border_style() -> None:
    tbl = Txtble(DATA, top_border=False, header_border=DOUBLE_BORDERS)
    assert str(tbl) == (
        "╔═════════╦══════════╦══════════════════╗\n"
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
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )
