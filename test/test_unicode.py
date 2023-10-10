from __future__ import annotations
from test_data import DATA, HEADERS
from txtble import Txtble


def test_unicode() -> None:
    tbl = Txtble(
        headers=("English", "Latin"),
        data=[
            ["to love", "amāre"],
            ["to teach", "docēre"],
            ["to put", "pōnere"],
            ["to take", "capere"],
            ["to fortify", "mūnīre"],
        ],
    )
    assert str(tbl) == (
        "+----------+------+\n"
        "|English   |Latin |\n"
        "+----------+------+\n"
        "|to love   |amāre |\n"
        "|to teach  |docēre|\n"
        "|to put    |pōnere|\n"
        "|to take   |capere|\n"
        "|to fortify|mūnīre|\n"
        "+----------+------+"
    )


def test_unicode_nfd() -> None:
    tbl = Txtble(
        headers=["NFC", "NFD"],
        data=[
            ["Pok\u00E9mon", "Poke\u0301mon"],
        ],
    )
    assert str(tbl) == (
        "+-------+-------+\n"
        "|NFC    |NFD    |\n"
        "+-------+-------+\n"
        "|Pok\u00E9mon|Poke\u0301mon|\n"
        "+-------+-------+"
    )


def test_fullwidth() -> None:
    tbl = Txtble(
        headers=["Halfwidth", "Fullwidth"],
        data=[
            ["Test text", "Ｔｅｓｔ\u3000ｔｅｘｔ"],
        ],
    )
    assert str(tbl) == (
        "+---------+------------------+\n"
        "|Halfwidth|Fullwidth         |\n"
        "+---------+------------------+\n"
        "|Test text|Ｔｅｓｔ\u3000ｔｅｘｔ|\n"
        "+---------+------------------+"
    )


def test_fullwidth_padding() -> None:
    tbl = Txtble(DATA, headers=HEADERS, padding="\uFF0D")
    assert str(tbl) == (
        "+-------------+--------------+----------------------+\n"
        "|－Month    －|－Birthstone－|－Birth Flower      －|\n"
        "+-------------+--------------+----------------------+\n"
        "|－January  －|－Garnet    －|－Carnation         －|\n"
        "|－February －|－Amethyst  －|－Violet            －|\n"
        "|－March    －|－Aquamarine－|－Jonquil           －|\n"
        "|－April    －|－Diamond   －|－Sweetpea          －|\n"
        "|－May      －|－Emerald   －|－Lily Of The Valley－|\n"
        "|－June     －|－Pearl     －|－Rose              －|\n"
        "|－July     －|－Ruby      －|－Larkspur          －|\n"
        "|－August   －|－Peridot   －|－Gladiolus         －|\n"
        "|－September－|－Sapphire  －|－Aster             －|\n"
        "|－October  －|－Opal      －|－Calendula         －|\n"
        "|－November －|－Topaz     －|－Chrysanthemum     －|\n"
        "|－December －|－Turquoise －|－Narcissus         －|\n"
        "+-------------+--------------+----------------------+"
    )


def test_leading_combining() -> None:
    tbl = Txtble(
        headers=["Category", "Name", "Glyph"],
        data=[
            ["Mn", "COMBINING ACUTE ACCENT", "\u0301"],
            ["Mc", "DEVANAGARI SIGN VISARGA", "\u0903"],
            ["Me", "COMBINING CYRILLIC HUNDRED THOUSANDS SIGN", "\u0488"],
        ],
    )
    assert str(tbl) == (
        "+--------+-----------------------------------------+-----+\n"
        "|Category|Name                                     |Glyph|\n"
        "+--------+-----------------------------------------+-----+\n"
        "|Mn      |COMBINING ACUTE ACCENT                   | \u0301    |\n"
        "|Mc      |DEVANAGARI SIGN VISARGA                  | \u0903   |\n"
        "|Me      |COMBINING CYRILLIC HUNDRED THOUSANDS SIGN| \u0488    |\n"
        "+--------+-----------------------------------------+-----+"
    )


def test_leading_combining_padding() -> None:
    tbl = Txtble(DATA, headers=HEADERS, padding="\u0301")
    assert str(tbl) == (
        "+-----------+------------+--------------------+\n"
        "| \u0301Month     \u0301| \u0301Birthstone \u0301| \u0301Birth Flower       \u0301|\n"
        "+-----------+------------+--------------------+\n"
        "| \u0301January   \u0301| \u0301Garnet     \u0301| \u0301Carnation          \u0301|\n"
        "| \u0301February  \u0301| \u0301Amethyst   \u0301| \u0301Violet             \u0301|\n"
        "| \u0301March     \u0301| \u0301Aquamarine \u0301| \u0301Jonquil            \u0301|\n"
        "| \u0301April     \u0301| \u0301Diamond    \u0301| \u0301Sweetpea           \u0301|\n"
        "| \u0301May       \u0301| \u0301Emerald    \u0301| \u0301Lily Of The Valley \u0301|\n"
        "| \u0301June      \u0301| \u0301Pearl      \u0301| \u0301Rose               \u0301|\n"
        "| \u0301July      \u0301| \u0301Ruby       \u0301| \u0301Larkspur           \u0301|\n"
        "| \u0301August    \u0301| \u0301Peridot    \u0301| \u0301Gladiolus          \u0301|\n"
        "| \u0301September \u0301| \u0301Sapphire   \u0301| \u0301Aster              \u0301|\n"
        "| \u0301October   \u0301| \u0301Opal       \u0301| \u0301Calendula          \u0301|\n"
        "| \u0301November  \u0301| \u0301Topaz      \u0301| \u0301Chrysanthemum      \u0301|\n"
        "| \u0301December  \u0301| \u0301Turquoise  \u0301| \u0301Narcissus          \u0301|\n"
        "+-----------+------------+--------------------+"
    )


def test_leading_combining_none_str() -> None:
    tbl = Txtble(
        headers=("repr", "value"),
        data=[
            ("''", ""),
            ("None", None),
            ("'None'", "None"),
        ],
        none_str="\u0301",
    )
    assert str(tbl) == (
        "+------+-----+\n"
        "|repr  |value|\n"
        "+------+-----+\n"
        "|''    |     |\n"
        "|None  | \u0301    |\n"
        "|'None'|None |\n"
        "+------+-----+"
    )


def test_leading_combining_header_fill() -> None:
    tbl = Txtble(
        headers=["Header"],
        header_fill="\u0301",
        data=[["A"], ["B", "C"]],
    )
    assert str(tbl) == (
        "+------+-+\n"
        "|Header| \u0301|\n"
        "+------+-+\n"
        "|A     | |\n"
        "|B     |C|\n"
        "+------+-+"
    )


def test_leading_combining_row_fill() -> None:
    tbl = Txtble(
        headers=["Header", "Header"],
        row_fill="\u0301",
        data=[["A"], ["B", "C"]],
    )
    assert str(tbl) == (
        "+------+------+\n"
        "|Header|Header|\n"
        "+------+------+\n"
        "|A     | \u0301     |\n"
        "|B     |C     |\n"
        "+------+------+"
    )


# vim:set nowrap:
