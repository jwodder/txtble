from __future__ import annotations
import pytest
from test_data import DATA, HEADERS, TABLE
from txtble import Txtble


def test_align_lll() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["l", "l", "l"])
    assert str(tbl) == TABLE


def test_align_ccc() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["c", "c", "c"])
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|  Month  |Birthstone|   Birth Flower   |\n"
        "+---------+----------+------------------+\n"
        "| January |  Garnet  |    Carnation     |\n"
        "|February | Amethyst |      Violet      |\n"
        "|  March  |Aquamarine|     Jonquil      |\n"
        "|  April  | Diamond  |     Sweetpea     |\n"
        "|   May   | Emerald  |Lily Of The Valley|\n"
        "|  June   |  Pearl   |       Rose       |\n"
        "|  July   |   Ruby   |     Larkspur     |\n"
        "| August  | Peridot  |    Gladiolus     |\n"
        "|September| Sapphire |      Aster       |\n"
        "| October |   Opal   |    Calendula     |\n"
        "|November |  Topaz   |  Chrysanthemum   |\n"
        "|December |Turquoise |    Narcissus     |\n"
        "+---------+----------+------------------+"
    )


def test_align_rrr() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["r", "r", "r"])
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|    Month|Birthstone|      Birth Flower|\n"
        "+---------+----------+------------------+\n"
        "|  January|    Garnet|         Carnation|\n"
        "| February|  Amethyst|            Violet|\n"
        "|    March|Aquamarine|           Jonquil|\n"
        "|    April|   Diamond|          Sweetpea|\n"
        "|      May|   Emerald|Lily Of The Valley|\n"
        "|     June|     Pearl|              Rose|\n"
        "|     July|      Ruby|          Larkspur|\n"
        "|   August|   Peridot|         Gladiolus|\n"
        "|September|  Sapphire|             Aster|\n"
        "|  October|      Opal|         Calendula|\n"
        "| November|     Topaz|     Chrysanthemum|\n"
        "| December| Turquoise|         Narcissus|\n"
        "+---------+----------+------------------+"
    )


def test_align_rcl() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["r", "c", "l"])
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|    Month|Birthstone|Birth Flower      |\n"
        "+---------+----------+------------------+\n"
        "|  January|  Garnet  |Carnation         |\n"
        "| February| Amethyst |Violet            |\n"
        "|    March|Aquamarine|Jonquil           |\n"
        "|    April| Diamond  |Sweetpea          |\n"
        "|      May| Emerald  |Lily Of The Valley|\n"
        "|     June|  Pearl   |Rose              |\n"
        "|     July|   Ruby   |Larkspur          |\n"
        "|   August| Peridot  |Gladiolus         |\n"
        "|September| Sapphire |Aster             |\n"
        "|  October|   Opal   |Calendula         |\n"
        "| November|  Topaz   |Chrysanthemum     |\n"
        "| December|Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_align_ccc_right_padding() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["c", "c", "c"], right_padding=2)
    assert str(tbl) == (
        "+-----------+------------+--------------------+\n"
        "|  Month    |Birthstone  |   Birth Flower     |\n"
        "+-----------+------------+--------------------+\n"
        "| January   |  Garnet    |    Carnation       |\n"
        "|February   | Amethyst   |      Violet        |\n"
        "|  March    |Aquamarine  |     Jonquil        |\n"
        "|  April    | Diamond    |     Sweetpea       |\n"
        "|   May     | Emerald    |Lily Of The Valley  |\n"
        "|  June     |  Pearl     |       Rose         |\n"
        "|  July     |   Ruby     |     Larkspur       |\n"
        "| August    | Peridot    |    Gladiolus       |\n"
        "|September  | Sapphire   |      Aster         |\n"
        "| October   |   Opal     |    Calendula       |\n"
        "|November   |  Topaz     |  Chrysanthemum     |\n"
        "|December   |Turquoise   |    Narcissus       |\n"
        "+-----------+------------+--------------------+"
    )


def test_align_extra_columns() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["c", "c"])
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|  Month  |Birthstone|Birth Flower      |\n"
        "+---------+----------+------------------+\n"
        "| January |  Garnet  |Carnation         |\n"
        "|February | Amethyst |Violet            |\n"
        "|  March  |Aquamarine|Jonquil           |\n"
        "|  April  | Diamond  |Sweetpea          |\n"
        "|   May   | Emerald  |Lily Of The Valley|\n"
        "|  June   |  Pearl   |Rose              |\n"
        "|  July   |   Ruby   |Larkspur          |\n"
        "| August  | Peridot  |Gladiolus         |\n"
        "|September| Sapphire |Aster             |\n"
        "| October |   Opal   |Calendula         |\n"
        "|November |  Topaz   |Chrysanthemum     |\n"
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_align_extra_columns_align_fill() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["c", "c"], align_fill="r")
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|  Month  |Birthstone|      Birth Flower|\n"
        "+---------+----------+------------------+\n"
        "| January |  Garnet  |         Carnation|\n"
        "|February | Amethyst |            Violet|\n"
        "|  March  |Aquamarine|           Jonquil|\n"
        "|  April  | Diamond  |          Sweetpea|\n"
        "|   May   | Emerald  |Lily Of The Valley|\n"
        "|  June   |  Pearl   |              Rose|\n"
        "|  July   |   Ruby   |          Larkspur|\n"
        "| August  | Peridot  |         Gladiolus|\n"
        "|September| Sapphire |             Aster|\n"
        "| October |   Opal   |         Calendula|\n"
        "|November |  Topaz   |     Chrysanthemum|\n"
        "|December |Turquoise |         Narcissus|\n"
        "+---------+----------+------------------+"
    )


def test_align_extra_aligns() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["r", "c", "l", "c", "r"])
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|    Month|Birthstone|Birth Flower      |\n"
        "+---------+----------+------------------+\n"
        "|  January|  Garnet  |Carnation         |\n"
        "| February| Amethyst |Violet            |\n"
        "|    March|Aquamarine|Jonquil           |\n"
        "|    April| Diamond  |Sweetpea          |\n"
        "|      May| Emerald  |Lily Of The Valley|\n"
        "|     June|  Pearl   |Rose              |\n"
        "|     July|   Ruby   |Larkspur          |\n"
        "|   August| Peridot  |Gladiolus         |\n"
        "|September| Sapphire |Aster             |\n"
        "|  October|   Opal   |Calendula         |\n"
        "| November|  Topaz   |Chrysanthemum     |\n"
        "| December|Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


@pytest.mark.parametrize("align", ["q", "L", "left", "<"])
def test_bad_align(align: str) -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["r", "c", align])
    with pytest.raises(ValueError, match="invalid alignment specifier"):
        str(tbl)


@pytest.mark.parametrize("align", ["q", "L", "left", "<"])
def test_bad_align_fill(align: str) -> None:
    tbl = Txtble(DATA, headers=HEADERS, align=["c", "c"], align_fill=align)
    with pytest.raises(ValueError, match="invalid alignment specifier"):
        str(tbl)


def test_align_all_c() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align="c")
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|  Month  |Birthstone|   Birth Flower   |\n"
        "+---------+----------+------------------+\n"
        "| January |  Garnet  |    Carnation     |\n"
        "|February | Amethyst |      Violet      |\n"
        "|  March  |Aquamarine|     Jonquil      |\n"
        "|  April  | Diamond  |     Sweetpea     |\n"
        "|   May   | Emerald  |Lily Of The Valley|\n"
        "|  June   |  Pearl   |       Rose       |\n"
        "|  July   |   Ruby   |     Larkspur     |\n"
        "| August  | Peridot  |    Gladiolus     |\n"
        "|September| Sapphire |      Aster       |\n"
        "| October |   Opal   |    Calendula     |\n"
        "|November |  Topaz   |  Chrysanthemum   |\n"
        "|December |Turquoise |    Narcissus     |\n"
        "+---------+----------+------------------+"
    )


def test_align_fill_c() -> None:
    tbl = Txtble(DATA, headers=HEADERS, align_fill="c")
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|  Month  |Birthstone|   Birth Flower   |\n"
        "+---------+----------+------------------+\n"
        "| January |  Garnet  |    Carnation     |\n"
        "|February | Amethyst |      Violet      |\n"
        "|  March  |Aquamarine|     Jonquil      |\n"
        "|  April  | Diamond  |     Sweetpea     |\n"
        "|   May   | Emerald  |Lily Of The Valley|\n"
        "|  June   |  Pearl   |       Rose       |\n"
        "|  July   |   Ruby   |     Larkspur     |\n"
        "| August  | Peridot  |    Gladiolus     |\n"
        "|September| Sapphire |      Aster       |\n"
        "| October |   Opal   |    Calendula     |\n"
        "|November |  Topaz   |  Chrysanthemum   |\n"
        "|December |Turquoise |    Narcissus     |\n"
        "+---------+----------+------------------+"
    )
