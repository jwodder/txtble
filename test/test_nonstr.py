from __future__ import annotations
from txtble import Txtble


class Custom:
    def __str__(self) -> str:
        return "str"

    def __bytes__(self) -> bytes:
        return b"bytes"

    def __repr__(self) -> str:
        return "repr"


def test_none() -> None:
    tbl = Txtble(
        headers=("repr", "value"),
        data=[
            ("''", ""),
            ("None", None),
            ("'None'", "None"),
        ],
    )
    assert str(tbl) == (
        "+------+-----+\n"
        "|repr  |value|\n"
        "+------+-----+\n"
        "|''    |     |\n"
        "|None  |     |\n"
        "|'None'|None |\n"
        "+------+-----+"
    )


def test_none_str() -> None:
    tbl = Txtble(
        headers=("repr", "value"),
        data=[
            ("''", ""),
            ("None", None),
            ("'None'", "None"),
        ],
        none_str="None",
    )
    assert str(tbl) == (
        "+------+-----+\n"
        "|repr  |value|\n"
        "+------+-----+\n"
        "|''    |     |\n"
        "|None  |None |\n"
        "|'None'|None |\n"
        "+------+-----+"
    )


def test_tab_none_str() -> None:
    tbl = Txtble(
        headers=("repr", "value"),
        data=[
            ("''", ""),
            ("None", None),
            ("'None'", "None"),
        ],
        none_str="<\t>",
    )
    assert str(tbl) == (
        "+------+---------+\n"
        "|repr  |value    |\n"
        "+------+---------+\n"
        "|''    |         |\n"
        "|None  |<       >|\n"
        "|'None'|None     |\n"
        "+------+---------+"
    )


def test_recursive_none_str() -> None:
    tbl = Txtble(
        headers=("repr", "value"),
        data=[
            ("''", ""),
            ("None", None),
            ("'None'", "None"),
        ],
        none_str=None,
    )
    assert str(tbl) == (
        "+------+-----+\n"
        "|repr  |value|\n"
        "+------+-----+\n"
        "|''    |     |\n"
        "|None  |None |\n"
        "|'None'|None |\n"
        "+------+-----+"
    )


def test_custom_none_str() -> None:
    tbl = Txtble(
        headers=("repr", "value"),
        data=[
            ("''", ""),
            ("None", None),
            ("'None'", "None"),
        ],
        none_str=Custom(),
    )
    assert str(tbl) == (
        "+------+-----+\n"
        "|repr  |value|\n"
        "+------+-----+\n"
        "|''    |     |\n"
        "|None  |str  |\n"
        "|'None'|None |\n"
        "+------+-----+"
    )


def test_multiline_none_str() -> None:
    tbl = Txtble(
        headers=("repr", "value"),
        data=[
            ("''", ""),
            ("None", None),
            ("'None'", "None"),
        ],
        none_str="foo\nbar",
    )
    assert str(tbl) == (
        "+------+-----+\n"
        "|repr  |value|\n"
        "+------+-----+\n"
        "|''    |     |\n"
        "|None  |foo  |\n"
        "|      |bar  |\n"
        "|'None'|None |\n"
        "+------+-----+"
    )


def test_custom() -> None:
    tbl = Txtble(data=[["A", "B"], ["C", Custom()]])
    assert str(tbl) == "+-+---+\n|A|B  |\n|C|str|\n+-+---+"
    assert str(tbl) == "+-+---+\n|A|B  |\n|C|str|\n+-+---+"


def test_custom_plus_unicode() -> None:
    tbl = Txtble(data=[["Å", "B"], ["Č", Custom()]])
    assert str(tbl) == "+-+---+\n|Å|B  |\n|Č|str|\n+-+---+"


def test_custom_header() -> None:
    tbl = Txtble(
        headers=[Custom(), "String"],
        data=[["A", "B"], ["C", "D"]],
    )
    assert str(tbl) == (
        "+---+------+\n"
        "|str|String|\n"
        "+---+------+\n"
        "|A  |B     |\n"
        "|C  |D     |\n"
        "+---+------+"
    )


def test_custom_header_fill() -> None:
    tbl = Txtble(
        headers=["Header"],
        header_fill=Custom(),
        data=[["A"], ["B", "C"]],
    )
    assert str(tbl) == (
        "+------+---+\n"
        "|Header|str|\n"
        "+------+---+\n"
        "|A     |   |\n"
        "|B     |C  |\n"
        "+------+---+"
    )


def test_custom_row_fill() -> None:
    tbl = Txtble(
        headers=["Header", "Header"],
        row_fill=Custom(),
        data=[["A"], ["B", "C"]],
    )
    assert str(tbl) == (
        "+------+------+\n"
        "|Header|Header|\n"
        "+------+------+\n"
        "|A     |str   |\n"
        "|B     |C     |\n"
        "+------+------+"
    )
