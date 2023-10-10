from __future__ import annotations
import pytest
from txtble import IndeterminateWidthError, Txtble

BAD_STRING = "\x01"
ERRMSG = f"{BAD_STRING!r}: string has indeterminate width"


@pytest.mark.parametrize(
    "s",
    [
        "\x0E",
        "\x0F",  # altcharset on/off
        "\033[17;23H",  # move cursor
        "\a",  # bell
        "\b",  # backspace
        "!\b!",
        "_\bx",  # overstruck printing
        "\x7F",  # delete
        "\033[H\033[J",  # clear screen
        "\033[?1049h",  # altscreen on
        "\033[?1049l",  # altscreen off
    ],
)
def test_indeterminate_cell(s: str) -> None:
    tbl = Txtble(
        headers=["Header", "Header"],
        data=[["A", "B"], [s, "D"]],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == s
    assert str(excinfo.value) == repr(s) + ": string has indeterminate width"


def test_indeterminate_header() -> None:
    tbl = Txtble(
        headers=["Header", BAD_STRING],
        data=[["A", "B"], ["C", "D"]],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG


def test_indeterminate_header_fill() -> None:
    tbl = Txtble(
        headers=["Header"],
        header_fill=BAD_STRING,
        data=[["A", "B"], ["C", "D"]],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG


def test_indeterminate_row_fill() -> None:
    tbl = Txtble(
        headers=["Header", "Header"],
        data=[["A", "B"], ["C"]],
        row_fill=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG


def test_indeterminate_none_str() -> None:
    tbl = Txtble(
        headers=["Header", "Header"],
        data=[["A", "B"], ["C", None]],
        none_str=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG


def test_indeterminate_padding() -> None:
    tbl = Txtble(
        headers=["Header", "Header"],
        data=[["A", "B"], ["C", "D"]],
        padding=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG
