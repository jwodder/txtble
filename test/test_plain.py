from __future__ import annotations
import pytest
from test_data import DATA, HEADERS, TABLE
from txtble import Txtble


def test_one_expression() -> None:
    tbl = Txtble(DATA, headers=HEADERS)
    assert str(tbl) == TABLE


def test_append_each() -> None:
    tbl = Txtble(headers=HEADERS)
    for row in DATA:
        tbl.append(row)
    assert str(tbl) == TABLE


def test_extend_all() -> None:
    tbl = Txtble(headers=HEADERS)
    tbl.extend(DATA)
    assert str(tbl) == TABLE


def test_headers_attr() -> None:
    tbl = Txtble(DATA)
    tbl.headers = HEADERS
    assert str(tbl) == TABLE


def test_no_rstrip() -> None:
    tbl = Txtble(DATA, headers=HEADERS, rstrip=False)
    assert str(tbl) == TABLE


@pytest.mark.parametrize("header_border", [None, True, False])
def test_no_headers(header_border: bool | None) -> None:
    tbl = Txtble(DATA, header_border=header_border)
    assert str(tbl) == (
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
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_empty() -> None:
    tbl = Txtble()
    assert str(tbl) == "++\n++"


def test_empty_no_border() -> None:
    tbl = Txtble(border=False)
    assert str(tbl) == ""


def test_headers_no_rows() -> None:
    tbl = Txtble(headers=("This", "That"))
    assert str(tbl) == "+----+----+\n|This|That|\n+----+----+"


def test_headers_empty_row() -> None:
    tbl = Txtble(headers=("This", "That"), data=[[]])
    assert str(tbl) == "+----+----+\n|This|That|\n+----+----+\n|    |    |\n+----+----+"


def test_headers_blank_row() -> None:
    tbl = Txtble(headers=("This", "That"), data=[["", ""]])
    assert str(tbl) == "+----+----+\n|This|That|\n+----+----+\n|    |    |\n+----+----+"


def test_headers_no_rows_no_border() -> None:
    tbl = Txtble(headers=("This", "That"), border=False)
    assert str(tbl) == "This|That"


def test_tabs() -> None:
    tbl = Txtble(
        headers=["Head\ter"],
        data=[
            ["\t*"],
            ["*\t*"],
            ["*\t\t*"],
        ],
    )
    assert str(tbl) == (
        "+-----------------+\n"
        "|Head    er       |\n"
        "+-----------------+\n"
        "|        *        |\n"
        "|*       *        |\n"
        "|*               *|\n"
        "+-----------------+"
    )


def test_extra_whitespace() -> None:
    tbl = Txtble(
        [
            ["  .leading.", ".trailing.  "],
            ["              ", "inn   er"],
        ]
    )
    assert str(tbl) == (
        "+--------------+------------+\n"
        "|  .leading.   |.trailing.  |\n"
        "|              |inn   er    |\n"
        "+--------------+------------+"
    )


def test_extra_whitespace_no_border() -> None:
    tbl = Txtble(
        [
            ["  .leading.", ".trailing.  "],
            ["              ", "inn   er"],
        ],
        border=False,
    )
    assert str(tbl) == "  .leading.   |.trailing.  \n              |inn   er"


def test_headers_matching_columns() -> None:
    tbl = Txtble(DATA, headers=HEADERS, columns=len(HEADERS))
    assert str(tbl) == TABLE


@pytest.mark.parametrize("columns", [len(HEADERS) - 1, len(HEADERS) + 1])
def test_headers_not_matching_columns(columns: int) -> None:
    tbl = Txtble(DATA, headers=HEADERS, columns=columns)
    with pytest.raises(
        ValueError,
        match=r"len\(headers\) and columns do not match",
    ):
        str(tbl)


@pytest.mark.parametrize("columns", [0, -1])
def test_bad_columns(columns: int) -> None:
    with pytest.raises(ValueError, match="columns must be at least 1"):
        Txtble(DATA, columns=columns)


@pytest.mark.parametrize("columns", [0, -1])
def test_bad_columns_attr(columns: int) -> None:
    tbl = Txtble(DATA)
    tbl.columns = columns
    with pytest.raises(ValueError, match="columns must be at least 1"):
        str(tbl)
