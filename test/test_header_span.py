from txtble import ASCII_EQ_BORDERS, Cell, Txtble


def test_cellspans_in_header():
    tbl = Txtble(
        headers=[
            [
                Cell("Level", rowspan=2),
                Cell("Proficiency Bonus", rowspan=2),
                Cell("Features", rowspan=2),
                Cell("Cantrips Known", rowspan=2),
                Cell("Spells Known", rowspan=2),
                Cell("— Spell Slots per Spell Level —", colspan=9),
            ],
            ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"],
        ],
        data=[
            [
                "1st",
                "+2",
                "Spellcasting, Bardic Inspiration (d6)",
                2,
                4,
                2,
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
            ],
        ],
        row_border=True,
        header_border=ASCII_EQ_BORDERS,
    )
    assert str(tbl) == (
        "+-----+-----------------+-------------------------------------+--------------+------------+---+---+---+---+---+---+---+---+---+\n"
        "|Level|Proficiency Bonus|Features                             |Cantrips Known|Spells Known|— Spell Slots per Spell Level —    |\n"
        "|     |                 |                                     |              |            +---+---+---+---+---+---+---+---+---+\n"
        "|     |                 |                                     |              |            |1st|2nd|3rd|4th|5th|6th|7th|8th|9th|\n"
        "+=====+=================+=====================================+==============+============+===+===+===+===+===+===+===+===+===+\n"
        "|1st  |+2               |Spellcasting, Bardic Inspiration (d6)|2             |4           |2  |—  |—  |—  |—  |—  |—  |—  |—  |\n"
        "+-----+-----------------+-------------------------------------+--------------+------------+---+---+---+---+---+---+---+---+---+"
    )


# TO TEST:
# - error on rowspans across header border (with & without header_border)
# - one header row containing colspans + dict rows (error?)
# - header_fill is spanning Cell

# vim:set nowrap:
