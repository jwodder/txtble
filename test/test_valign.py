from __future__ import annotations
import pytest
from txtble import Txtble

LONG_STRING = "Lorem ipsum dolor sit amet, consectetur adipisicing elit"


def test_valign() -> None:
    tbl = Txtble(
        headers=["Line 1", "Line 2", "Line 3", "5 Syllables\n7 Syllables\n5 Syllables"],
        data=[
            [
                "Haikus are easy,",
                "But sometimes they don't make sense.",
                "Refrigerator.",
                "-- - --\n- -- - - - -\n-----",
            ]
        ],
        valign=["t", "m", "b"],
    )
    assert str(tbl) == (
        "+----------------+------------------------------------+-------------+------------+\n"
        "|Line 1          |                                    |             |5 Syllables |\n"
        "|                |Line 2                              |             |7 Syllables |\n"
        "|                |                                    |Line 3       |5 Syllables |\n"
        "+----------------+------------------------------------+-------------+------------+\n"
        "|Haikus are easy,|                                    |             |-- - --     |\n"
        "|                |But sometimes they don't make sense.|             |- -- - - - -|\n"
        "|                |                                    |Refrigerator.|-----       |\n"
        "+----------------+------------------------------------+-------------+------------+"
    )


@pytest.mark.parametrize("v", ["t", "m", "b"])
def test_valign_wrap_t(v: str) -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], valign=[v, "t"], widths=[20, 30])
    assert str(tbl) == (
        "+--------------------+------------------------------+\n"
        "|Lorem ipsum dolor   |Lorem ipsum dolor sit amet,   |\n"
        "|sit amet,           |consectetur adipisicing elit  |\n"
        "|consectetur         |                              |\n"
        "|adipisicing elit    |                              |\n"
        "+--------------------+------------------------------+"
    )


@pytest.mark.parametrize("v", ["t", "m", "b"])
def test_valign_wrap_m(v: str) -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], valign=[v, "m"], widths=[20, 30])
    assert str(tbl) == (
        "+--------------------+------------------------------+\n"
        "|Lorem ipsum dolor   |                              |\n"
        "|sit amet,           |Lorem ipsum dolor sit amet,   |\n"
        "|consectetur         |consectetur adipisicing elit  |\n"
        "|adipisicing elit    |                              |\n"
        "+--------------------+------------------------------+"
    )


@pytest.mark.parametrize("v", ["t", "m", "b"])
def test_valign_wrap_b(v: str) -> None:
    tbl = Txtble([[LONG_STRING, LONG_STRING]], valign=[v, "b"], widths=[20, 30])
    assert str(tbl) == (
        "+--------------------+------------------------------+\n"
        "|Lorem ipsum dolor   |                              |\n"
        "|sit amet,           |                              |\n"
        "|consectetur         |Lorem ipsum dolor sit amet,   |\n"
        "|adipisicing elit    |consectetur adipisicing elit  |\n"
        "+--------------------+------------------------------+"
    )


@pytest.mark.parametrize("v", ["t", "m", "b"])
def test_mid_valign_odd_within_even(v: str) -> None:
    tbl = Txtble(
        [["Line", "Line 1\nLine 2\nLine 3\nLine 4"]],
        valign=["m", v],
    )
    assert str(tbl) == (
        "+----+------+\n"
        "|    |Line 1|\n"
        "|Line|Line 2|\n"
        "|    |Line 3|\n"
        "|    |Line 4|\n"
        "+----+------+"
    )


@pytest.mark.parametrize("v", ["t", "m", "b"])
def test_mid_valign_even_within_odd(v: str) -> None:
    tbl = Txtble(
        [["Line 1\nLine 2", "Line 1\nLine 2\nLine 3\nLine 4\nLine 5"]],
        valign=["m", v],
    )
    assert str(tbl) == (
        "+------+------+\n"
        "|      |Line 1|\n"
        "|Line 1|Line 2|\n"
        "|Line 2|Line 3|\n"
        "|      |Line 4|\n"
        "|      |Line 5|\n"
        "+------+------+"
    )


@pytest.mark.parametrize("v", ["t", "m", "b"])
def test_bot_valign_trailing_newlines(v: str) -> None:
    tbl = Txtble(
        [["Line\n\n", "Line 1\nLine 2\nLine 3\nLine 4"]],
        valign=["b", v],
    )
    assert str(tbl) == (
        "+----+------+\n"
        "|    |Line 1|\n"
        "|Line|Line 2|\n"
        "|    |Line 3|\n"
        "|    |Line 4|\n"
        "+----+------+"
    )


def test_valign_extra_columns() -> None:
    tbl = Txtble(
        [["Line", "Line 1\nLine 2\nLine 3\nLine 4", "Extra 1\nExtra 2"]],
        valign=["m", "m"],
    )
    assert str(tbl) == (
        "+----+------+-------+\n"
        "|    |Line 1|Extra 1|\n"
        "|Line|Line 2|Extra 2|\n"
        "|    |Line 3|       |\n"
        "|    |Line 4|       |\n"
        "+----+------+-------+"
    )


def test_valign_extra_columns_valign_fill() -> None:
    tbl = Txtble(
        [["Line", "Line 1\nLine 2\nLine 3\nLine 4", "Extra 1\nExtra 2"]],
        valign=["m", "m"],
        valign_fill="b",
    )
    assert str(tbl) == (
        "+----+------+-------+\n"
        "|    |Line 1|       |\n"
        "|Line|Line 2|       |\n"
        "|    |Line 3|Extra 1|\n"
        "|    |Line 4|Extra 2|\n"
        "+----+------+-------+"
    )


def test_valign_extra_aligns() -> None:
    tbl = Txtble(
        [["Line", "Line 1\nLine 2\nLine 3\nLine 4", "Extra 1\nExtra 2"]],
        valign=["m", "m", "b", "t", "t", "m"],
    )
    assert str(tbl) == (
        "+----+------+-------+\n"
        "|    |Line 1|       |\n"
        "|Line|Line 2|       |\n"
        "|    |Line 3|Extra 1|\n"
        "|    |Line 4|Extra 2|\n"
        "+----+------+-------+"
    )


@pytest.mark.parametrize("valign", ["q", "T", "top", "<"])
def test_bad_valign(valign: str) -> None:
    tbl = Txtble(
        [["Line", "Line 1\nLine 2\nLine 3\nLine 4", "Extra 1\nExtra 2"]],
        valign=["m", "m", valign],
    )
    with pytest.raises(ValueError, match="invalid vertical alignment specifier"):
        str(tbl)


@pytest.mark.parametrize("valign", ["q", "T", "top", "<"])
def test_bad_valign_fill(valign: str) -> None:
    tbl = Txtble(
        [["Line", "Line 1\nLine 2\nLine 3\nLine 4", "Extra 1\nExtra 2"]],
        valign=["m", "m"],
        valign_fill=valign,
    )
    with pytest.raises(ValueError, match="invalid vertical alignment specifier"):
        str(tbl)


def test_valign_all_m() -> None:
    tbl = Txtble(
        [["Line", "Line 1\nLine 2\nLine 3\nLine 4", "Extra 1\nExtra 2"]],
        valign="m",
    )
    assert str(tbl) == (
        "+----+------+-------+\n"
        "|    |Line 1|       |\n"
        "|Line|Line 2|Extra 1|\n"
        "|    |Line 3|Extra 2|\n"
        "|    |Line 4|       |\n"
        "+----+------+-------+"
    )


def test_valign_fill_m() -> None:
    tbl = Txtble(
        [["Line", "Line 1\nLine 2\nLine 3\nLine 4", "Extra 1\nExtra 2"]],
        valign_fill="m",
    )
    assert str(tbl) == (
        "+----+------+-------+\n"
        "|    |Line 1|       |\n"
        "|Line|Line 2|Extra 1|\n"
        "|    |Line 3|Extra 2|\n"
        "|    |Line 4|       |\n"
        "+----+------+-------+"
    )


# vim:set nowrap:
