from __future__ import annotations
import pytest
from test_data import DATA, HEADERS
from txtble import IndeterminateWidthError, Txtble

LONG_STRING = "Lorem ipsum dolor sit amet, consectetur adipisicing elit"


def test_wrap() -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], widths=[20, 30])
    assert str(tbl) == (
        "+--------------------+------------------------------+\n"
        "|Lorem ipsum dolor   |Lorem ipsum dolor sit amet,   |\n"
        "|sit amet,           |consectetur adipisicing elit  |\n"
        "|consectetur         |                              |\n"
        "|adipisicing elit    |                              |\n"
        "+--------------------+------------------------------+"
    )


@pytest.mark.parametrize("widths", [[20], [20, None], [20, None, 30]])
def test_wrap_no_wrap(widths: list[int | None]) -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], widths=widths)
    assert str(tbl) == (
        "+--------------------+--------------------------------------------------------+\n"
        "|Lorem ipsum dolor   |Lorem ipsum dolor sit amet, consectetur adipisicing elit|\n"
        "|sit amet,           |                                                        |\n"
        "|consectetur         |                                                        |\n"
        "|adipisicing elit    |                                                        |\n"
        "+--------------------+--------------------------------------------------------+"
    )


def test_no_wrap_wrap() -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], widths=[None, 30])
    assert str(tbl) == (
        "+--------------------------------------------------------+------------------------------+\n"
        "|Lorem ipsum dolor sit amet, consectetur adipisicing elit|Lorem ipsum dolor sit amet,   |\n"
        "|                                                        |consectetur adipisicing elit  |\n"
        "+--------------------------------------------------------+------------------------------+"
    )


def test_wrap_long_word() -> None:
    tbl = Txtble(
        [[LONG_STRING], ["antidisestablishmentarianism"]],
        row_border=True,
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+\n"
        "|antidisestablishment|\n"
        "|arianism            |\n"
        "+--------------------+"
    )


def test_wrap_colored_long_word() -> None:
    tbl = Txtble(
        [[LONG_STRING], ["\033[31mantidisestablishmentarianism\033[m"]],
        row_border=True,
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+\n"
        "|\033[31mantidisestablishment\033[m|\n"
        "|\033[31marianism\033[m            |\n"
        "+--------------------+"
    )


def test_wrap_long_word_no_break_long_words() -> None:
    tbl = Txtble(
        [[LONG_STRING], ["antidisestablishmentarianism"]],
        break_long_words=False,
        row_border=True,
        widths=[20],
    )
    assert str(tbl) == (
        "+----------------------------+\n"
        "|Lorem ipsum dolor           |\n"
        "|sit amet,                   |\n"
        "|consectetur                 |\n"
        "|adipisicing elit            |\n"
        "+----------------------------+\n"
        "|antidisestablishmentarianism|\n"
        "+----------------------------+"
    )


@pytest.mark.parametrize("break_long", [True, False])
def test_wrap_long_hyphenated_word(break_long: bool) -> None:
    tbl = Txtble(
        [[LONG_STRING], ["anti-dis-establish-ment-ari-an-ism"]],
        break_long_words=break_long,
        row_border=True,
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+\n"
        "|anti-dis-establish- |\n"
        "|ment-ari-an-ism     |\n"
        "+--------------------+"
    )


@pytest.mark.parametrize("break_long", [True, False])
def test_wrap_long_multi_hyphenated_word(break_long: bool) -> None:
    ### XXX: textwrap.wrap would insert a break before the '---'; should txtble
    ### do likewise?
    tbl = Txtble(
        [[LONG_STRING], ["anti-dis-establish---ment-ari-an-ism"]],
        break_long_words=break_long,
        row_border=True,
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+\n"
        "|anti-dis-establish--|\n"
        "|-ment-ari-an-ism    |\n"
        "+--------------------+"
    )


def test_wrap_long_hyphenated_word_no_break_on_hyphens() -> None:
    tbl = Txtble(
        [[LONG_STRING], ["anti-dis-establish-ment-ari-an-ism"]],
        break_on_hyphens=False,
        row_border=True,
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+\n"
        "|anti-dis-establish-m|\n"
        "|ent-ari-an-ism      |\n"
        "+--------------------+"
    )


@pytest.mark.parametrize("hyph_break", [True, False])
def test_wrap_long_soft_hyphenated_word(hyph_break: bool) -> None:
    # textwrap doesn't break on soft hyphens, so txtble shouldn't either.
    tbl = Txtble(
        [
            [LONG_STRING],
            ["anti\xADdis\xADestablish\xADment\xADari\xADan\xADism"],
        ],
        break_on_hyphens=hyph_break,
        row_border=True,
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+\n"
        "|anti\xADdis\xADestablish\xADment\xAD|\n"
        "|ari\xADan\xADism            |\n"
        "+--------------------+"
    )


def test_wrap_some_cells() -> None:
    tbl = Txtble(
        [[LONG_STRING], ["antidisestablishmentarianism"]],
        row_border=True,
        widths=[30],
    )
    assert str(tbl) == (
        "+------------------------------+\n"
        "|Lorem ipsum dolor sit amet,   |\n"
        "|consectetur adipisicing elit  |\n"
        "+------------------------------+\n"
        "|antidisestablishmentarianism  |\n"
        "+------------------------------+"
    )


def test_wrap_shorter_than_width() -> None:
    tbl = Txtble(DATA, headers=HEADERS, widths=20)
    assert str(tbl) == (
        "+--------------------+--------------------+--------------------+\n"
        "|Month               |Birthstone          |Birth Flower        |\n"
        "+--------------------+--------------------+--------------------+\n"
        "|January             |Garnet              |Carnation           |\n"
        "|February            |Amethyst            |Violet              |\n"
        "|March               |Aquamarine          |Jonquil             |\n"
        "|April               |Diamond             |Sweetpea            |\n"
        "|May                 |Emerald             |Lily Of The Valley  |\n"
        "|June                |Pearl               |Rose                |\n"
        "|July                |Ruby                |Larkspur            |\n"
        "|August              |Peridot             |Gladiolus           |\n"
        "|September           |Sapphire            |Aster               |\n"
        "|October             |Opal                |Calendula           |\n"
        "|November            |Topaz               |Chrysanthemum       |\n"
        "|December            |Turquoise           |Narcissus           |\n"
        "+--------------------+--------------------+--------------------+"
    )


def test_wrap_color() -> None:
    tbl = Txtble(
        [
            [
                "\033[31mLorem\033[m"
                " \033[32mipsum\033[m"
                " \033[33mdolor\033[m"
                " \033[34msit\033[m \033[35mamet\033[m,"
                " \033[36mconsectetur\033[m"
                " \033[41madipisicing\033[m"
                " \033[42melit\033[m"
            ]
        ],
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|\033[31mLorem\033[m \033[32mipsum\033[m \033[33mdolor\033[m   |\n"
        "|\033[34msit\033[m \033[35mamet\033[m,           |\n"
        "|\033[36mconsectetur\033[m         |\n"
        "|\033[41madipisicing\033[m \033[42melit\033[m    |\n"
        "+--------------------+"
    )


def test_wrap_running_color() -> None:
    tbl = Txtble(
        [
            [
                "\033[31mLorem"
                " \033[32mipsum"
                " \033[33mdolor"
                " \033[34msit \033[35mamet,"
                " \033[36mconsectetur"
                " \033[41madipisicing"
                " \033[42melit\033[m"
            ]
        ],
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|\033[31mLorem \033[32mipsum \033[33mdolor\033[m   |\n"
        "|\033[31m\033[32m\033[33m\033[34msit \033[35mamet,\033[m           |\n"
        "|\033[31m\033[32m\033[33m\033[34m\033[35m\033[36mconsectetur\033[m         |\n"
        "|\033[31m\033[32m\033[33m\033[34m\033[35m\033[36m\033[41madipisicing \033[42melit\033[m    |\n"
        "+--------------------+"
    )


def test_wrap_long_color() -> None:
    tbl = Txtble([["\033[31m" + LONG_STRING + "\033[0m"]], widths=[20])
    assert str(tbl) == (
        "+--------------------+\n"
        "|\033[31mLorem ipsum dolor\033[m   |\n"
        "|\033[31msit amet,\033[m           |\n"
        "|\033[31mconsectetur\033[m         |\n"
        "|\033[31madipisicing elit\033[0m    |\n"
        "+--------------------+"
    )


def test_width_fill() -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], widths=[20], width_fill=30)
    assert str(tbl) == (
        "+--------------------+------------------------------+\n"
        "|Lorem ipsum dolor   |Lorem ipsum dolor sit amet,   |\n"
        "|sit amet,           |consectetur adipisicing elit  |\n"
        "|consectetur         |                              |\n"
        "|adipisicing elit    |                              |\n"
        "+--------------------+------------------------------+"
    )


def test_width_fill_all() -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], width_fill=20)
    assert str(tbl) == (
        "+--------------------+--------------------+\n"
        "|Lorem ipsum dolor   |Lorem ipsum dolor   |\n"
        "|sit amet,           |sit amet,           |\n"
        "|consectetur         |consectetur         |\n"
        "|adipisicing elit    |adipisicing elit    |\n"
        "+--------------------+--------------------+"
    )


@pytest.mark.parametrize("width_fill", [None, 30])
def test_widths_all(width_fill: int | None) -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], widths=20, width_fill=width_fill)
    assert str(tbl) == (
        "+--------------------+--------------------+\n"
        "|Lorem ipsum dolor   |Lorem ipsum dolor   |\n"
        "|sit amet,           |sit amet,           |\n"
        "|consectetur         |consectetur         |\n"
        "|adipisicing elit    |adipisicing elit    |\n"
        "+--------------------+--------------------+"
    )


@pytest.mark.parametrize("width_fill", [None, 30])
def test_widths_all_none(width_fill: int | None) -> None:
    tbl = Txtble(
        [[LONG_STRING, LONG_STRING]],
        width_fill=width_fill,
        widths=None,
    )
    assert str(tbl) == (
        "+--------------------------------------------------------"
        "+--------------------------------------------------------+\n"
        "|Lorem ipsum dolor sit amet, consectetur adipisicing elit"
        "|Lorem ipsum dolor sit amet, consectetur adipisicing elit|\n"
        "+--------------------------------------------------------"
        "+--------------------------------------------------------+"
    )


def test_wrap_multiline() -> None:
    tbl = Txtble([["Lorem ipsum\n" + LONG_STRING]], widths=[20])
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum         |\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+"
    )


def test_wrap_fullwidth() -> None:
    tbl = Txtble(
        [["Ｌｏｒｅｍ ｉｐｓｕｍ ｄｏｌｏｒ ｓｉｔ ａｍｅｔ"]],
        widths=[30],
    )
    assert str(tbl) == (
        "+------------------------------+\n"
        "|Ｌｏｒｅｍ ｉｐｓｕｍ         |\n"
        "|ｄｏｌｏｒ ｓｉｔ ａｍｅｔ    |\n"
        "+------------------------------+"
    )


def test_wrap_fullwidth_long_word() -> None:
    tbl = Txtble(
        [["ａｎｔｉｄｉｓｅｓｔａｂｌｉｓｈｍｅｎｔａｒｉａｎｉｓｍ"]],
        widths=[30],
    )
    assert str(tbl) == (
        "+------------------------------+\n"
        "|ａｎｔｉｄｉｓｅｓｔａｂｌｉｓ|\n"
        "|ｈｍｅｎｔａｒｉａｎｉｓｍ    |\n"
        "+------------------------------+"
    )


def test_wrap_combining() -> None:
    tbl = Txtble(
        [
            [
                "L\u0301o\u0301r\u0301e\u0301m\u0301"
                " i\u0301p\u0301s\u0301u\u0301m\u0301"
                " d\u0301o\u0301l\u0301o\u0301r\u0301"
                " s\u0301i\u0301t\u0301"
                " a\u0301m\u0301e\u0301t\u0301"
            ],
        ],
        widths=[30],
    )
    assert str(tbl) == (
        "+------------------------------+\n"
        "|L\u0301o\u0301r\u0301e\u0301m\u0301"
        " i\u0301p\u0301s\u0301u\u0301m\u0301"
        " d\u0301o\u0301l\u0301o\u0301r\u0301"
        " s\u0301i\u0301t\u0301"
        " a\u0301m\u0301e\u0301t\u0301    |\n"
        "+------------------------------+"
    )


def test_wrap_fullwidth_builtin_len() -> None:
    tbl = Txtble(
        [["Ｌｏｒｅｍ ｉｐｓｕｍ ｄｏｌｏｒ ｓｉｔ ａｍｅｔ"]],
        len_func=len,
        widths=[30],
    )
    assert str(tbl) == (
        "+------------------------------+\n"
        "|Ｌｏｒｅｍ ｉｐｓｕｍ ｄｏｌｏｒ ｓｉｔ ａｍｅｔ    |\n"
        "+------------------------------+"
    )


def test_wrap_combining_builtin_len() -> None:
    tbl = Txtble(
        [
            [
                "L\u0301o\u0301r\u0301e\u0301m\u0301"
                " i\u0301p\u0301s\u0301u\u0301m\u0301"
                " d\u0301o\u0301l\u0301o\u0301r\u0301"
                " s\u0301i\u0301t\u0301"
                " a\u0301m\u0301e\u0301t\u0301"
            ],
        ],
        len_func=len,
        widths=[30],
    )
    assert str(tbl) == (
        "+------------------------------+\n"
        "|L\u0301o\u0301r\u0301e\u0301m\u0301 i\u0301p\u0301s\u0301u\u0301m\u0301         |\n"
        "|d\u0301o\u0301l\u0301o\u0301r\u0301 s\u0301i\u0301t\u0301 a\u0301m\u0301e\u0301t\u0301    |\n"
        "+------------------------------+"
    )


def test_wrap_padding() -> None:
    tbl = Txtble([[LONG_STRING]], padding=2, widths=[30])
    assert str(tbl) == (
        "+----------------------------------+\n"
        "|  Lorem ipsum dolor sit amet,     |\n"
        "|  consectetur adipisicing elit    |\n"
        "+----------------------------------+"
    )


@pytest.mark.parametrize("s", [LONG_STRING, ""])
@pytest.mark.parametrize("width", [-42, 0, "", "q"])
def test_invalid_width(s: str, width: int | str) -> None:
    tbl = Txtble([[s]], widths=[width])  # type: ignore[list-item]
    with pytest.raises((TypeError, ValueError)):
        str(tbl)


def test_wrap_header() -> None:
    tbl = Txtble([[LONG_STRING]], headers=[LONG_STRING], widths=[20])
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+"
    )


def test_wrap_none_str() -> None:
    tbl = Txtble([[None]], none_str=LONG_STRING, widths=[20])
    assert str(tbl) == (
        "+--------------------+\n"
        "|Lorem ipsum dolor   |\n"
        "|sit amet,           |\n"
        "|consectetur         |\n"
        "|adipisicing elit    |\n"
        "+--------------------+"
    )


def test_wrap_header_fill_row_fill() -> None:
    tbl = Txtble(
        [["foo"], ["bar", "baz"]],
        header_fill=LONG_STRING,
        headers=["Quux"],
        row_fill=LONG_STRING,
        widths=[None, 20],
    )
    assert str(tbl) == (
        "+----+--------------------+\n"
        "|Quux|Lorem ipsum dolor   |\n"
        "|    |sit amet,           |\n"
        "|    |consectetur         |\n"
        "|    |adipisicing elit    |\n"
        "+----+--------------------+\n"
        "|foo |Lorem ipsum dolor   |\n"
        "|    |sit amet,           |\n"
        "|    |consectetur         |\n"
        "|    |adipisicing elit    |\n"
        "|bar |baz                 |\n"
        "+----+--------------------+"
    )


def test_wrap_empty() -> None:
    tbl = Txtble([[""]], widths=[20])
    assert (
        str(tbl)
        == "+--------------------+\n|                    |\n+--------------------+"
    )


def test_wrap_long_word_short_words() -> None:
    tbl = Txtble(
        [['"Antidisestablishmentarianism" is not that hard to spell.']],
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        '|"Antidisestablishmen|\n'
        '|tarianism" is not   |\n'
        "|that hard to spell. |\n"
        "+--------------------+"
    )


def test_wrap_long_word_short_words_no_break_long_words() -> None:
    tbl = Txtble(
        [['"Antidisestablishmentarianism" is not that hard to spell.']],
        break_long_words=False,
        widths=[20],
    )
    assert str(tbl) == (
        "+------------------------------+\n"
        '|"Antidisestablishmentarianism"|\n'
        "|is not that hard to           |\n"
        "|spell.                        |\n"
        "+------------------------------+"
    )


@pytest.mark.parametrize("hyph_break", [True, False])
def test_wrap_hyphen_after_width(hyph_break: bool) -> None:
    tbl = Txtble(
        [["Antidisestablishmentarianism-length words are hard to wrap."]],
        break_on_hyphens=hyph_break,
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        "|Antidisestablishment|\n"
        "|arianism-length     |\n"
        "|words are hard to   |\n"
        "|wrap.               |\n"
        "+--------------------+"
    )


def test_wrap_hyphen_after_width_no_break_long_words() -> None:
    tbl = Txtble(
        [["Antidisestablishmentarianism-length words are hard to wrap."]],
        break_long_words=False,
        widths=[20],
    )
    assert str(tbl) == (
        "+-----------------------------+\n"
        "|Antidisestablishmentarianism-|\n"
        "|length words are             |\n"
        "|hard to wrap.                |\n"
        "+-----------------------------+"
    )


def test_wrap_even_multiple() -> None:
    tbl = Txtble(
        [['"The time has come," the Walrus said, "To talk of many things"']],
        widths=[20],
    )
    assert str(tbl) == (
        "+--------------------+\n"
        '|"The time has come,"|\n'
        '|the Walrus said, "To|\n'
        '|talk of many things"|\n'
        "+--------------------+"
    )


def test_wrap_before_trailing_space() -> None:
    tbl = Txtble([['"The time has come." ']], widths=[20])
    assert str(tbl) == (
        "+--------------------+\n"
        '|"The time has come."|\n'
        "|                    |\n"
        "+--------------------+"
    )


def test_wrap_bad_len_func() -> None:
    width = 20

    def len_func(s: str) -> int:
        return -1 if 0 < len(s) <= width else len(s)

    tbl = Txtble([[LONG_STRING]], len_func=len_func, widths=[width])
    with pytest.raises(IndeterminateWidthError):
        str(tbl)


def test_wrap_implementation_bsearch_boundary() -> None:
    """
    Test a boundary condition in the implementation of the long-word-splitting
    algorithm
    """
    tbl = Txtble([["antidisestablishme\u0301n\uFF54arianism"]], widths=[20])
    assert str(tbl) == (
        "+--------------------+\n"
        "|antidisestablishme\u0301n |\n"
        "|\uFF54arianism          |\n"
        "+--------------------+"
    )


# vim:set nowrap:
