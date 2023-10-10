from __future__ import annotations
import pytest
from txtble import NumericWidthOverflowError, Txtble


@pytest.mark.parametrize("align", ["n", "ln", "nl"])
def test_align_n(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", 1234.5],
            ["Baz", 123.45],
            ["Quux", 12.345],
            ["Glarch", 1.2345],
            ["Gnusto", 0.12345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+-----------+\n"
        "|Thing |Value      |\n"
        "+------+-----------+\n"
        "|Foo   |12345      |\n"
        "|Bar   | 1234.5    |\n"
        "|Baz   |  123.45   |\n"
        "|Quux  |   12.345  |\n"
        "|Glarch|    1.2345 |\n"
        "|Gnusto|    0.12345|\n"
        "+------+-----------+"
    )


@pytest.mark.parametrize("align", ["cn", "nc"])
def test_align_nc(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", 1234.5],
            ["Baz", 123.45],
            ["Quux", 12.345],
            ["Glarch", 1.2345],
            ["Gnusto", 0.12345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+-----------+\n"
        "|Thing |   Value   |\n"
        "+------+-----------+\n"
        "|Foo   |12345      |\n"
        "|Bar   | 1234.5    |\n"
        "|Baz   |  123.45   |\n"
        "|Quux  |   12.345  |\n"
        "|Glarch|    1.2345 |\n"
        "|Gnusto|    0.12345|\n"
        "+------+-----------+"
    )


@pytest.mark.parametrize("align", ["rn", "nr"])
def test_align_nr(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", 1234.5],
            ["Baz", 123.45],
            ["Quux", 12.345],
            ["Glarch", 1.2345],
            ["Gnusto", 0.12345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+-----------+\n"
        "|Thing |      Value|\n"
        "+------+-----------+\n"
        "|Foo   |12345      |\n"
        "|Bar   | 1234.5    |\n"
        "|Baz   |  123.45   |\n"
        "|Quux  |   12.345  |\n"
        "|Glarch|    1.2345 |\n"
        "|Gnusto|    0.12345|\n"
        "+------+-----------+"
    )


@pytest.mark.parametrize("align", ["n", "ln", "nl", "cn", "nc", "rn", "nr"])
def test_align_n_integers(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", 1234],
            ["Baz", 123],
            ["Quux", 12],
            ["Glarch", 1],
            ["Gnusto", 0],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+-----+\n"
        "|Thing |Value|\n"
        "+------+-----+\n"
        "|Foo   |12345|\n"
        "|Bar   | 1234|\n"
        "|Baz   |  123|\n"
        "|Quux  |   12|\n"
        "|Glarch|    1|\n"
        "|Gnusto|    0|\n"
        "+------+-----+"
    )


@pytest.mark.parametrize("align", ["n", "ln", "nl"])
def test_align_n_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.2345],
            ["Gnusto", "green"],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+----------+\n"
        "|Thing |Value     |\n"
        "+------+----------+\n"
        "|Foo   |12345     |\n"
        "|Bar   |red       |\n"
        "|Baz   |  123.45  |\n"
        "|Quux  |blue      |\n"
        "|Glarch|    1.2345|\n"
        "|Gnusto|green     |\n"
        "+------+----------+"
    )


@pytest.mark.parametrize("align", ["cn", "nc"])
def test_align_nc_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.2345],
            ["Gnusto", "green"],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+----------+\n"
        "|Thing |  Value   |\n"
        "+------+----------+\n"
        "|Foo   |12345     |\n"
        "|Bar   |   red    |\n"
        "|Baz   |  123.45  |\n"
        "|Quux  |   blue   |\n"
        "|Glarch|    1.2345|\n"
        "|Gnusto|  green   |\n"
        "+------+----------+"
    )


@pytest.mark.parametrize("align", ["rn", "nr"])
def test_align_nr_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.2345],
            ["Gnusto", "green"],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+----------+\n"
        "|Thing |     Value|\n"
        "+------+----------+\n"
        "|Foo   |12345     |\n"
        "|Bar   |       red|\n"
        "|Baz   |  123.45  |\n"
        "|Quux  |      blue|\n"
        "|Glarch|    1.2345|\n"
        "|Gnusto|     green|\n"
        "+------+----------+"
    )


@pytest.mark.parametrize("align", ["n", "ln", "nl"])
def test_align_n_long_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red red red red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.2345],
            ["Gnusto", "green"],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+---------------+\n"
        "|Thing |Value          |\n"
        "+------+---------------+\n"
        "|Foo   |12345          |\n"
        "|Bar   |red red red red|\n"
        "|Baz   |  123.45       |\n"
        "|Quux  |blue           |\n"
        "|Glarch|    1.2345     |\n"
        "|Gnusto|green          |\n"
        "+------+---------------+"
    )


@pytest.mark.parametrize("align", ["cn", "nc"])
def test_align_nc_long_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red red red red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.2345],
            ["Gnusto", "green"],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+---------------+\n"
        "|Thing |     Value     |\n"
        "+------+---------------+\n"
        "|Foo   |  12345        |\n"
        "|Bar   |red red red red|\n"
        "|Baz   |    123.45     |\n"
        "|Quux  |     blue      |\n"
        "|Glarch|      1.2345   |\n"
        "|Gnusto|     green     |\n"
        "+------+---------------+"
    )


@pytest.mark.parametrize("align", ["rn", "nr"])
def test_align_nr_long_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red red red red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.2345],
            ["Gnusto", "green"],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+---------------+\n"
        "|Thing |          Value|\n"
        "+------+---------------+\n"
        "|Foo   |     12345     |\n"
        "|Bar   |red red red red|\n"
        "|Baz   |       123.45  |\n"
        "|Quux  |           blue|\n"
        "|Glarch|         1.2345|\n"
        "|Gnusto|          green|\n"
        "+------+---------------+"
    )


@pytest.mark.parametrize("align", ["n", "ln", "nl"])
def test_align_n_long_width_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red red red red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.23],
            ["Gnusto", "green"],
        ],
        align=["l", align],
        widths=[None, 9],
    )
    assert str(tbl) == (
        "+------+---------+\n"
        "|Thing |Value    |\n"
        "+------+---------+\n"
        "|Foo   |12345    |\n"
        "|Bar   |red red  |\n"
        "|      |red red  |\n"
        "|Baz   |  123.45 |\n"
        "|Quux  |blue     |\n"
        "|Glarch|    1.23 |\n"
        "|Gnusto|green    |\n"
        "+------+---------+"
    )


@pytest.mark.parametrize("align", ["cn", "nc"])
def test_align_nc_long_width_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red red red red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.23],
            ["Gnusto", "green"],
        ],
        align=["l", align],
        widths=[None, 9],
    )
    assert str(tbl) == (
        "+------+---------+\n"
        "|Thing |  Value  |\n"
        "+------+---------+\n"
        "|Foo   |12345    |\n"
        "|Bar   | red red |\n"
        "|      | red red |\n"
        "|Baz   |  123.45 |\n"
        "|Quux  |  blue   |\n"
        "|Glarch|    1.23 |\n"
        "|Gnusto|  green  |\n"
        "+------+---------+"
    )


@pytest.mark.parametrize("align", ["rn", "nr"])
def test_align_nr_long_width_mixed(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", "red red red red"],
            ["Baz", 123.45],
            ["Quux", "blue"],
            ["Glarch", 1.23],
            ["Gnusto", "green"],
        ],
        align=["l", align],
        widths=[None, 9],
    )
    assert str(tbl) == (
        "+------+---------+\n"
        "|Thing |    Value|\n"
        "+------+---------+\n"
        "|Foo   | 12345   |\n"
        "|Bar   |  red red|\n"
        "|      |  red red|\n"
        "|Baz   |   123.45|\n"
        "|Quux  |     blue|\n"
        "|Glarch|     1.23|\n"
        "|Gnusto|    green|\n"
        "+------+---------+"
    )


@pytest.mark.parametrize("align", ["n", "ln", "nl"])
def test_align_n_mixed_numstr(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Baz", "1.2"],
            ["Glarch", 1.2345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+----------+\n"
        "|Thing |Value     |\n"
        "+------+----------+\n"
        "|Foo   |12345     |\n"
        "|Baz   |1.2       |\n"
        "|Glarch|    1.2345|\n"
        "+------+----------+"
    )


@pytest.mark.parametrize("align", ["cn", "nc"])
def test_align_nc_mixed_numstr(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Baz", "1.2"],
            ["Glarch", 1.2345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+----------+\n"
        "|Thing |  Value   |\n"
        "+------+----------+\n"
        "|Foo   |12345     |\n"
        "|Baz   |   1.2    |\n"
        "|Glarch|    1.2345|\n"
        "+------+----------+"
    )


@pytest.mark.parametrize("align", ["rn", "nr"])
def test_align_nr_mixed_numstr(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Baz", "1.2"],
            ["Glarch", 1.2345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+----------+\n"
        "|Thing |     Value|\n"
        "+------+----------+\n"
        "|Foo   |12345     |\n"
        "|Baz   |       1.2|\n"
        "|Glarch|    1.2345|\n"
        "+------+----------+"
    )


@pytest.mark.parametrize("align", ["n", "ln", "nl"])
def test_align_n_long_header(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Numeric Value"],
        data=[
            ["Foo", 12345],
            ["Baz", 123.45],
            ["Glarch", 1.2345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+-------------+\n"
        "|Thing |Numeric Value|\n"
        "+------+-------------+\n"
        "|Foo   |12345        |\n"
        "|Baz   |  123.45     |\n"
        "|Glarch|    1.2345   |\n"
        "+------+-------------+"
    )


@pytest.mark.parametrize("align", ["cn", "nc"])
def test_align_nc_long_header(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Numeric Value"],
        data=[
            ["Foo", 12345],
            ["Baz", 123.45],
            ["Glarch", 1.2345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+-------------+\n"
        "|Thing |Numeric Value|\n"
        "+------+-------------+\n"
        "|Foo   | 12345       |\n"
        "|Baz   |   123.45    |\n"
        "|Glarch|     1.2345  |\n"
        "+------+-------------+"
    )


@pytest.mark.parametrize("align", ["rn", "nr"])
def test_align_nr_long_header(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Numeric Value"],
        data=[
            ["Foo", 12345],
            ["Baz", 123.45],
            ["Glarch", 1.2345],
        ],
        align=["l", align],
    )
    assert str(tbl) == (
        "+------+-------------+\n"
        "|Thing |Numeric Value|\n"
        "+------+-------------+\n"
        "|Foo   |   12345     |\n"
        "|Baz   |     123.45  |\n"
        "|Glarch|       1.2345|\n"
        "+------+-------------+"
    )


def test_align_n_no_border() -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", 1234.5],
            ["Baz", 123.45],
            ["Quux", 12.345],
            ["Glarch", 1.2345],
            ["Gnusto", 0.12345],
        ],
        align=["l", "n"],
        border=False,
    )
    assert str(tbl) == (
        "Thing |Value\n"
        "------+-----------\n"
        "Foo   |12345\n"
        "Bar   | 1234.5\n"
        "Baz   |  123.45\n"
        "Quux  |   12.345\n"
        "Glarch|    1.2345\n"
        "Gnusto|    0.12345"
    )


def test_align_n_header_number() -> None:
    tbl = Txtble(
        headers=["Thing", 12.345],
        data=[
            ["Foo", 12345],
            ["Bar", 1234.5],
            ["Baz", 123.45],
            ["Quux", 12.345],
            ["Glarch", 1.2345],
            ["Gnusto", 0.12345],
        ],
        align=["l", "n"],
    )
    assert str(tbl) == (
        "+------+-----------+\n"
        "|Thing |   12.345  |\n"
        "+------+-----------+\n"
        "|Foo   |12345      |\n"
        "|Bar   | 1234.5    |\n"
        "|Baz   |  123.45   |\n"
        "|Quux  |   12.345  |\n"
        "|Glarch|    1.2345 |\n"
        "|Gnusto|    0.12345|\n"
        "+------+-----------+"
    )


def test_align_n_long_header_number() -> None:
    tbl = Txtble(
        headers=["Thing", 123456.654321],
        data=[
            ["Foo", 12345],
            ["Bar", 1234.5],
            ["Baz", 123.45],
            ["Quux", 12.345],
            ["Glarch", 1.2345],
            ["Gnusto", 0.12345],
        ],
        align=["l", "n"],
    )
    assert str(tbl) == (
        "+------+-------------+\n"
        "|Thing |123456.654321|\n"
        "+------+-------------+\n"
        "|Foo   | 12345       |\n"
        "|Bar   |  1234.5     |\n"
        "|Baz   |   123.45    |\n"
        "|Quux  |    12.345   |\n"
        "|Glarch|     1.2345  |\n"
        "|Gnusto|     0.12345 |\n"
        "+------+-------------+"
    )


def test_align_n_numeric_row_fill() -> None:
    tbl = Txtble(
        [
            ["Foo", 12345],
            ["Bar", 123.45, 54.321],
            ["Baz", 1.2345],
        ],
        align="n",
        row_fill=1.2,
    )
    assert str(tbl) == (
        "+---+----------+------+\n"
        "|Foo|12345     | 1.2  |\n"
        "|Bar|  123.45  |54.321|\n"
        "|Baz|    1.2345| 1.2  |\n"
        "+---+----------+------+"
    )


def test_align_n_numeric_none_str() -> None:
    tbl = Txtble(
        [
            ["Foo", 12345, None],
            ["Bar", 123.45, 54.321],
            ["Baz", 1.2345, None],
        ],
        align="n",
        none_str=1.2,
    )
    assert str(tbl) == (
        "+---+----------+------+\n"
        "|Foo|12345     | 1.2  |\n"
        "|Bar|  123.45  |54.321|\n"
        "|Baz|    1.2345| 1.2  |\n"
        "+---+----------+------+"
    )


def test_align_n_numeric_dict_fill() -> None:
    tbl = Txtble(
        headers=["A", "B", "C"],
        data=[
            {"A": "Foo", "B": 12345},
            {"A": "Bar", "B": 123.45, "C": 54.321},
            {"A": "Baz", "B": 1.2345},
        ],
        align="n",
        dict_fill=1.2,
    )
    assert str(tbl) == (
        "+---+----------+------+\n"
        "|A  |B         |C     |\n"
        "+---+----------+------+\n"
        "|Foo|12345     | 1.2  |\n"
        "|Bar|  123.45  |54.321|\n"
        "|Baz|    1.2345| 1.2  |\n"
        "+---+----------+------+"
    )


def test_align_n_numeric_header_fill() -> None:
    tbl = Txtble(
        [
            ["Foo", 12345, 1.2],
            ["Bar", 123.45, 54.321],
            ["Baz", 1.2345, 2.1],
        ],
        align="n",
        header_fill=54321.12345,
        headers=["Col 1", "Col 2"],
    )
    assert str(tbl) == (
        "+-----+----------+-----------+\n"
        "|Col 1|Col 2     |54321.12345|\n"
        "+-----+----------+-----------+\n"
        "|Foo  |12345     |    1.2    |\n"
        "|Bar  |  123.45  |   54.321  |\n"
        "|Baz  |    1.2345|    2.1    |\n"
        "+-----+----------+-----------+"
    )


@pytest.mark.parametrize("align", ["n", "ln", "nl", "cn", "nc", "rn", "nr"])
def test_numalign_exact_width(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 1.2],
            ["Bar", 0.5],
            ["Baz", 12],
            ["Quux", 12.34],
            ["Glarch", 0.12],
        ],
        align=["l", align],
        widths=[None, 5],
    )
    assert str(tbl) == (
        "+------+-----+\n"
        "|Thing |Value|\n"
        "+------+-----+\n"
        "|Foo   | 1.2 |\n"
        "|Bar   | 0.5 |\n"
        "|Baz   |12   |\n"
        "|Quux  |12.34|\n"
        "|Glarch| 0.12|\n"
        "+------+-----+"
    )


@pytest.mark.parametrize("align", ["n", "ln", "nl"])
def test_numalign_extra_width_left(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 1.2],
            ["Bar", 0.5],
            ["Baz", 12],
            ["Quux", 12.34],
            ["Glarch", 0.12],
        ],
        align=["l", align],
        widths=[None, 8],
    )
    assert str(tbl) == (
        "+------+--------+\n"
        "|Thing |Value   |\n"
        "+------+--------+\n"
        "|Foo   | 1.2    |\n"
        "|Bar   | 0.5    |\n"
        "|Baz   |12      |\n"
        "|Quux  |12.34   |\n"
        "|Glarch| 0.12   |\n"
        "+------+--------+"
    )


@pytest.mark.parametrize("align", ["cn", "nc"])
def test_numalign_extra_width_center(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 1.2],
            ["Bar", 0.5],
            ["Baz", 12],
            ["Quux", 12.34],
            ["Glarch", 0.12],
        ],
        align=["l", align],
        widths=[None, 8],
    )
    assert str(tbl) == (
        "+------+--------+\n"
        "|Thing | Value  |\n"
        "+------+--------+\n"
        "|Foo   |  1.2   |\n"
        "|Bar   |  0.5   |\n"
        "|Baz   | 12     |\n"
        "|Quux  | 12.34  |\n"
        "|Glarch|  0.12  |\n"
        "+------+--------+"
    )


@pytest.mark.parametrize("align", ["rn", "nr"])
def test_numalign_extra_width_right(align: str) -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 1.2],
            ["Bar", 0.5],
            ["Baz", 12],
            ["Quux", 12.34],
            ["Glarch", 0.12],
        ],
        align=["l", align],
        widths=[None, 8],
    )
    assert str(tbl) == (
        "+------+--------+\n"
        "|Thing |   Value|\n"
        "+------+--------+\n"
        "|Foo   |    1.2 |\n"
        "|Bar   |    0.5 |\n"
        "|Baz   |   12   |\n"
        "|Quux  |   12.34|\n"
        "|Glarch|    0.12|\n"
        "+------+--------+"
    )


def test_numalign_short_width() -> None:
    """
    Test handling of numbers that are small enough to fit in the width before
    numeric alignment is applied but not after
    """
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", 1234.5],
            ["Baz", 123.45],
            ["Quux", 12.345],
            ["Glarch", 1.2345],
        ],
        align=["l", "n"],
        widths=[None, 6],
    )
    with pytest.raises(NumericWidthOverflowError) as excinfo:
        str(tbl)
    assert str(excinfo.value) == "Numeric alignment overflows column width"


def test_numalign_very_short_width() -> None:
    tbl = Txtble(
        headers=["Thing", "Value"],
        data=[
            ["Foo", 12345],
            ["Bar", 1234.5],
            ["Baz", 123.45],
            ["Quux", 12.345],
            ["Glarch", 1.2345],
            ["Gnusto", 0.12345],
        ],
        align=["l", "n"],
        widths=[None, 4],
    )
    with pytest.raises(NumericWidthOverflowError) as excinfo:
        str(tbl)
    assert str(excinfo.value) == "Numeric alignment overflows column width"


def test_numalign_long_numeric_header() -> None:
    tbl = Txtble(
        headers=["Thing", 123456],
        data=[
            ["Foo", 1.2],
            ["Bar", 0.5],
            ["Baz", 12],
            ["Quux", 12.34],
            ["Glarch", 0.12],
        ],
        align=["l", "n"],
        widths=[None, 5],
    )
    with pytest.raises(NumericWidthOverflowError) as excinfo:
        str(tbl)
    assert str(excinfo.value) == "Numeric alignment overflows column width"
