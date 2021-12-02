from test_data import DATA, HEADERS, TABLE
from txtble import Cell, Txtble


def test_cell_noop():
    tbl = Txtble(data=[[Cell(c) for c in row] for row in DATA], headers=HEADERS)
    assert str(tbl) == TABLE


def test_cell_class_alignments():
    tbl = Txtble(
        [
            [
                Cell("-"),
                "Red\nGreen\nBlue",
                Cell("-", align="r"),
            ],
            [
                "Earth\nWind\nFire",
                Cell("-", align="c", valign="m"),
                "Maiden\nMother\nCrone",
            ],
            [
                Cell("-", valign="b"),
                "Executive\nLegislative\nJudicial",
                Cell("-", align="r", valign="b"),
            ],
        ],
        row_border=True,
    )
    assert str(tbl) == (
        "+-----+-----------+------+\n"
        "|-    |Red        |     -|\n"
        "|     |Green      |      |\n"
        "|     |Blue       |      |\n"
        "+-----+-----------+------+\n"
        "|Earth|           |Maiden|\n"
        "|Wind |     -     |Mother|\n"
        "|Fire |           |Crone |\n"
        "+-----+-----------+------+\n"
        "|     |Executive  |      |\n"
        "|     |Legislative|      |\n"
        "|-    |Judicial   |     -|\n"
        "+-----+-----------+------+"
    )


# Test Cell alignment vs. column alignment
# Test Cell padding vs. table padding
# Test setting `none_str` or `*_fill` to a Cell
