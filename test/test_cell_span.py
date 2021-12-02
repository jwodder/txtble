import pytest
from txtble import ASCII_EQ_BORDERS, Cell, Txtble


def test_colspan_len_lt_first_col():
    tbl = Txtble(
        headers=["One", "Two", "Three", "Four"],
        data=[
            ["Foo", Cell("Bar", colspan=2), "Baz"],
            ["Quux", "Glarch", "Gnusto", "Cleesh"],
        ],
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    assert str(tbl) == (
        "+----+------+------+------+\n"
        "|One |Two   |Three |Four  |\n"
        "+====+======+======+======+\n"
        "|Foo |Bar          |Baz   |\n"
        "+----+------+------+------+\n"
        "|Quux|Glarch|Gnusto|Cleesh|\n"
        "+----+------+------+------+"
    )


def test_colspan_across_col_border():
    tbl = Txtble(
        headers=["One", "Two", "Three", "Four"],
        data=[
            ["Foo", Cell("Something", colspan=2), "Baz"],
            ["Quux", "Glarch", "Gnusto", "Cleesh"],
        ],
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    assert str(tbl) == (
        "+----+------+------+------+\n"
        "|One |Two   |Three |Four  |\n"
        "+====+======+======+======+\n"
        "|Foo |Something    |Baz   |\n"
        "+----+------+------+------+\n"
        "|Quux|Glarch|Gnusto|Cleesh|\n"
        "+----+------+------+------+"
    )


def test_colspan_exact_fit():
    tbl = Txtble(
        headers=["One", "Two", "Three", "Four"],
        data=[
            ["Foo", Cell("Exactly equal", colspan=2), "Baz"],
            ["Quux", "Glarch", "Gnusto", "Cleesh"],
        ],
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    assert str(tbl) == (
        "+----+------+------+------+\n"
        "|One |Two   |Three |Four  |\n"
        "+====+======+======+======+\n"
        "|Foo |Exactly equal|Baz   |\n"
        "+----+------+------+------+\n"
        "|Quux|Glarch|Gnusto|Cleesh|\n"
        "+----+------+------+------+"
    )


def test_colspan_wider_than_spanned():
    tbl = Txtble(
        headers=["One", "Two", "Three", "Four"],
        data=[
            ["Foo", Cell("Wider than below", colspan=2), "Baz"],
            ["Quux", "Glarch", "Gnusto", "Cleesh"],
        ],
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    assert str(tbl) == (
        "+----+--------+-------+------+\n"
        "|One |Two     |Three  |Four  |\n"
        "+====+========+=======+======+\n"
        "|Foo |Wider than below|Baz   |\n"
        "+----+--------+-------+------+\n"
        "|Quux|Glarch  |Gnusto |Cleesh|\n"
        "+----+--------+-------+------+"
    )


def test_colspan_wider_than_spanned_restrict_width():
    tbl = Txtble(
        headers=["One", "Two", "Three", "Four"],
        data=[
            [
                "Foo",
                Cell("Wider than below", colspan=2, restrict_width=True),
                "Baz",
            ],
            ["Quux", "Glarch", "Gnusto", "Cleesh"],
        ],
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    assert str(tbl) == (
        "+----+------+------+------+\n"
        "|One |Two   |Three |Four  |\n"
        "+====+======+======+======+\n"
        "|Foo |Wider than   |Baz   |\n"
        "|    |below        |      |\n"
        "+----+------+------+------+\n"
        "|Quux|Glarch|Gnusto|Cleesh|\n"
        "+----+------+------+------+"
    )


def test_rowspan():
    tbl = Txtble(
        data=[
            ["Foo", Cell("Bar", rowspan=2), "Baz"],
            ["Quux", "Glarch"],
        ],
        row_border=True,
    )
    assert str(tbl) == (
        "+----+---+------+\n"
        "|Foo |Bar|Baz   |\n"
        "+----+   +------+\n"
        "|Quux|   |Glarch|\n"
        "+----+---+------+"
    )


def test_multiline_rowspan():
    tbl = Txtble(
        data=[
            ["Foo", Cell("Bar\nCleesh", rowspan=2), "Baz"],
            ["Quux", "Glarch"],
        ],
        row_border=True,
    )
    assert str(tbl) == (
        "+----+------+------+\n"
        "|Foo |Bar   |Baz   |\n"
        "+----+Cleesh+------+\n"
        "|Quux|      |Glarch|\n"
        "+----+------+------+"
    )


def test_rst_grid_table():
    # Taken from <https://docutils.sourceforge.io/docs/ref/rst/
    #             restructuredtext.html#grid-tables>
    tbl = Txtble(
        headers=[
            "Header row, column 1\n(header rows optional)",
            "Header 2",
            "Header 3",
            "Header 4",
        ],
        data=[
            [
                "body row 1, column 1",
                "column 2",
                "column 3",
                "column 4",
            ],
            [
                "body row 2",
                Cell("Cells may span columns.", colspan=3),
            ],
            [
                "body row 3",
                Cell("Cells may\nspan rows.", rowspan=2),
                Cell(
                    "- Table cells\n- contain\n- body elements.",
                    colspan=2,
                    rowspan=2,
                ),
            ],
            [
                "body row 4",
            ],
        ],
        padding=1,
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    assert str(tbl) == (
        "+------------------------+------------+----------+----------+\n"
        "| Header row, column 1   | Header 2   | Header 3 | Header 4 |\n"
        "| (header rows optional) |            |          |          |\n"
        "+========================+============+==========+==========+\n"
        "| body row 1, column 1   | column 2   | column 3 | column 4 |\n"
        "+------------------------+------------+----------+----------+\n"
        "| body row 2             | Cells may span columns.          |\n"
        "+------------------------+------------+---------------------+\n"
        "| body row 3             | Cells may  | - Table cells       |\n"
        "+------------------------+ span rows. | - contain           |\n"
        "| body row 4             |            | - body elements.    |\n"
        "+------------------------+------------+---------------------+"
    )


def test_uneven_colspans():
    tbl = Txtble(
        data=[
            [Cell("Kumquat", colspan=2), Cell("Gnusto", colspan=2)],
            ["Quux", Cell("Glarch", colspan=2), "Bar"],
            [Cell("Baz", colspan=2), Cell("Pineapple", colspan=2)],
        ],
        row_border=1,
    )
    assert str(tbl) == (
        "+-------+---------+\n"
        "|Kumquat|Gnusto   |\n"
        "+----+--+---+-----+\n"
        "|Quux|Glarch|Bar  |\n"
        "+----+--+---+-----+\n"
        "|Baz    |Pineapple|\n"
        "+-------+---------+"
    )


def test_column_pair_only_spanned():
    tbl = Txtble(
        data=[
            ["Foo", Cell("Bar", colspan=2), "Baz"],
            ["Quux", Cell("Gnusto", colspan=2), "Cleesh"],
        ],
        row_border=1,
    )
    assert str(tbl) == (
        "+----+------+------+\n"
        "|Foo |Bar   |Baz   |\n"
        "+----+------+------+\n"
        "|Quux|Gnusto|Cleesh|\n"
        "+----+------+------+"
    )


@pytest.mark.parametrize("colspan", [0, -1])
def test_error_bad_colspan_kwarg(colspan):
    with pytest.raises(ValueError) as excinfo:
        Cell("Foo", colspan=colspan)
    assert str(excinfo.value) == f"Invalid colspan value: {colspan!r}"


@pytest.mark.parametrize("colspan", [0, -1])
def test_error_bad_colspan_attr(colspan):
    c = Cell("Foo")
    c.colspan = colspan
    tbl = Txtble(
        headers=["One", "Two", "Three", "Four"],
        data=[
            ["Foo", c, "Baz"],
            ["Quux", "Glarch", "Gnusto", "Cleesh"],
        ],
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    with pytest.raises(ValueError) as excinfo:
        str(tbl)
    assert str(excinfo.value) == f"Invalid colspan value: {colspan!r}"


@pytest.mark.parametrize("rowspan", [0, -1])
def test_error_bad_rowspan_kwarg(rowspan):
    with pytest.raises(ValueError) as excinfo:
        Cell("Foo", rowspan=rowspan)
    assert str(excinfo.value) == f"Invalid rowspan value: {rowspan!r}"


@pytest.mark.parametrize("rowspan", [0, -1])
def test_error_bad_rowspan_attr(rowspan):
    c = Cell("Foo")
    c.rowspan = rowspan
    tbl = Txtble(
        headers=["One", "Two", "Three", "Four"],
        data=[
            ["Foo", c, "Baz"],
            ["Quux", "Glarch", "Gnusto", "Cleesh"],
        ],
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    with pytest.raises(ValueError) as excinfo:
        str(tbl)
    assert str(excinfo.value) == f"Invalid rowspan value: {rowspan!r}"


# TO TEST:
# - "cascading"
# - dict row with missing entries corresponding to covered cells, with &
#   without dict_fill set
# - error on rowspanning out of bounds
# - setting colspan/rowspan via Cell attribute
# - colspanning past `columns` (error)
# - row_fill is spanning Cell (error)
# - dict_fill is spanning Cell
# - none_str is spanning Cell (error???)
# - colspans = 4; 3, 1; 2, 2 ?
# - colspans = 3, 3; 2, 2, 2 ?
#  - The 3-3 border splits the middle 2-cell below in half?
# - interaction with alignment
# - non-interaction with `widths` option
# - colspan cell with `restrict_width=True` and unbreakable word longer than
#   spanned columns (with & without spanned columns having set widths)
# - spanning cells with no row border/no column border
# - spanning cells with box drawing border style
