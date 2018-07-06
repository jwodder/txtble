from test_data import DATA, HEADERS
from txtble import Txtble


def test_align_index():
    tbl = Txtble(DATA, headers=HEADERS)
    tbl.align[1] = "c"
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|Month    |Birthstone|Birth Flower      |\n"
        "+---------+----------+------------------+\n"
        "|January  |  Garnet  |Carnation         |\n"
        "|February | Amethyst |Violet            |\n"
        "|March    |Aquamarine|Jonquil           |\n"
        "|April    | Diamond  |Sweetpea          |\n"
        "|May      | Emerald  |Lily Of The Valley|\n"
        "|June     |  Pearl   |Rose              |\n"
        "|July     |   Ruby   |Larkspur          |\n"
        "|August   | Peridot  |Gladiolus         |\n"
        "|September| Sapphire |Aster             |\n"
        "|October  |   Opal   |Calendula         |\n"
        "|November |  Topaz   |Chrysanthemum     |\n"
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_align_index_align_fill():
    tbl = Txtble(DATA, headers=HEADERS)
    tbl.align[1] = "c"
    tbl.align_fill = "r"
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|    Month|Birthstone|      Birth Flower|\n"
        "+---------+----------+------------------+\n"
        "|  January|  Garnet  |         Carnation|\n"
        "| February| Amethyst |            Violet|\n"
        "|    March|Aquamarine|           Jonquil|\n"
        "|    April| Diamond  |          Sweetpea|\n"
        "|      May| Emerald  |Lily Of The Valley|\n"
        "|     June|  Pearl   |              Rose|\n"
        "|     July|   Ruby   |          Larkspur|\n"
        "|   August| Peridot  |         Gladiolus|\n"
        "|September| Sapphire |             Aster|\n"
        "|  October|   Opal   |         Calendula|\n"
        "| November|  Topaz   |     Chrysanthemum|\n"
        "| December|Turquoise |         Narcissus|\n"
        "+---------+----------+------------------+"
    )


def test_align_all_align_index():
    tbl = Txtble(DATA, headers=HEADERS, align="r")
    tbl.align[1] = "c"
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|    Month|Birthstone|      Birth Flower|\n"
        "+---------+----------+------------------+\n"
        "|  January|  Garnet  |         Carnation|\n"
        "| February| Amethyst |            Violet|\n"
        "|    March|Aquamarine|           Jonquil|\n"
        "|    April| Diamond  |          Sweetpea|\n"
        "|      May| Emerald  |Lily Of The Valley|\n"
        "|     June|  Pearl   |              Rose|\n"
        "|     July|   Ruby   |          Larkspur|\n"
        "|   August| Peridot  |         Gladiolus|\n"
        "|September| Sapphire |             Aster|\n"
        "|  October|   Opal   |         Calendula|\n"
        "| November|  Topaz   |     Chrysanthemum|\n"
        "| December|Turquoise |         Narcissus|\n"
        "+---------+----------+------------------+"
    )


def test_align_index_out_of_bounds():
    tbl = Txtble(DATA, headers=HEADERS, align=["c"])
    tbl.align[2] = "r"
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
