from __future__ import annotations
from pytest_mock import MockerFixture
from test_data import DATA, HEADERS, TABLE
from txtble import Txtble, with_color_stripped


def test_custom_len_func_old_not_called(mocker: MockerFixture) -> None:
    strwidth = mocker.patch("txtble.classes.strwidth")
    tbl = Txtble(DATA, headers=HEADERS, len_func=len)
    assert str(tbl) == TABLE
    assert not strwidth.called


def test_null_defaulting_len_func(mocker: MockerFixture) -> None:
    import txtble.classes

    spy = mocker.spy(txtble.classes, "strwidth")
    tbl = Txtble(DATA, headers=HEADERS, len_func=None)
    assert str(tbl) == TABLE
    spy.assert_has_calls(
        [mocker.call(s) for s in HEADERS + sum(DATA, [])],
        any_order=True,
    )


def test_constant_len_func() -> None:
    tbl = Txtble(DATA, headers=HEADERS, len_func=lambda s: 5 if s else 0)
    # The `if s` check prevents the left & right padding from adding to the
    # hrule width, which would just make for a confusing test.
    assert str(tbl) == (
        "+-----+-----+-----+\n"
        "|Month|Birthstone|Birth Flower|\n"
        "+-----+-----+-----+\n"
        "|January|Garnet|Carnation|\n"
        "|February|Amethyst|Violet|\n"
        "|March|Aquamarine|Jonquil|\n"
        "|April|Diamond|Sweetpea|\n"
        "|May|Emerald|Lily Of The Valley|\n"
        "|June|Pearl|Rose|\n"
        "|July|Ruby|Larkspur|\n"
        "|August|Peridot|Gladiolus|\n"
        "|September|Sapphire|Aster|\n"
        "|October|Opal|Calendula|\n"
        "|November|Topaz|Chrysanthemum|\n"
        "|December|Turquoise|Narcissus|\n"
        "+-----+-----+-----+"
    )


def test_builtin_len_func_ansi() -> None:
    tbl = Txtble([["\033[31mRed\033[0m"], ["Red"]], len_func=len)
    assert (
        str(tbl)
        == "+------------+\n|\033[31mRed\033[0m|\n|Red         |\n+------------+"
    )


def test_color_aware_len_func_ansi() -> None:
    tbl = Txtble(
        [["\033[31mRed\033[0m"], ["Red"]],
        len_func=with_color_stripped(len),
    )
    assert str(tbl) == "+---+\n|\033[31mRed\033[0m|\n|Red|\n+---+"


def test_fullwidth_builtin_len_func() -> None:
    tbl = Txtble(
        [
            ["Ｌｏｒｅｍ ｉｐｓｕｍ ｄｏｌｏｒ ｓｉｔ ａｍｅｔ"],
            ["Lorem ipsum dolor sit amet"],
        ],
        len_func=len,
    )
    assert str(tbl) == (
        "+--------------------------+\n"
        "|Ｌｏｒｅｍ ｉｐｓｕｍ ｄｏｌｏｒ ｓｉｔ ａｍｅｔ|\n"
        "|Lorem ipsum dolor sit amet|\n"
        "+--------------------------+"
    )


def test_combining_builtin_len_func() -> None:
    s = (
        "L\u0301o\u0301r\u0301e\u0301m\u0301"
        " i\u0301p\u0301s\u0301u\u0301m\u0301"
        " d\u0301o\u0301l\u0301o\u0301r\u0301"
        " s\u0301i\u0301t\u0301"
        " a\u0301m\u0301e\u0301t\u0301"
    )
    s2 = "Lorem ipsum dolor sit amet"
    tbl = Txtble([[s], [s2]], len_func=len)
    w = len(s)
    assert str(tbl) == (
        "+"
        + "-" * w
        + "+\n"
        + "|"
        + s
        + "|\n"
        + "|"
        + s2
        + " " * s.count("\u0301")
        + "|\n"
        + "+"
        + "-" * w
        + "+"
    )
