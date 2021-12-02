from txtble import ASCII_EQ_BORDERS, HEAVY_BORDERS, LIGHT_BORDERS, HRule, Txtble


def test_hrule():
    tbl = Txtble(
        headers=["Month", "Birthstone", "Birth Flower"],
        data=[
            ["January", "Garnet", "Carnation"],
            ["February", "Amethyst", "Violet"],
            ["March", "Aquamarine", "Jonquil"],
            HRule(),
            ["April", "Diamond", "Sweetpea"],
            ["May", "Emerald", "Lily Of The Valley"],
            ["June", "Pearl", "Rose"],
            HRule(),
            ["July", "Ruby", "Larkspur"],
            ["August", "Peridot", "Gladiolus"],
            ["September", "Sapphire", "Aster"],
            HRule(),
            ["October", "Opal", "Calendula"],
            ["November", "Topaz", "Chrysanthemum"],
            ["December", "Turquoise", "Narcissus"],
        ],
    )
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|Month    |Birthstone|Birth Flower      |\n"
        "+---------+----------+------------------+\n"
        "|January  |Garnet    |Carnation         |\n"
        "|February |Amethyst  |Violet            |\n"
        "|March    |Aquamarine|Jonquil           |\n"
        "+---------+----------+------------------+\n"
        "|April    |Diamond   |Sweetpea          |\n"
        "|May      |Emerald   |Lily Of The Valley|\n"
        "|June     |Pearl     |Rose              |\n"
        "+---------+----------+------------------+\n"
        "|July     |Ruby      |Larkspur          |\n"
        "|August   |Peridot   |Gladiolus         |\n"
        "|September|Sapphire  |Aster             |\n"
        "+---------+----------+------------------+\n"
        "|October  |Opal      |Calendula         |\n"
        "|November |Topaz     |Chrysanthemum     |\n"
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_hrule_table_border_style():
    tbl = Txtble(
        headers=["Month", "Birthstone", "Birth Flower"],
        data=[
            ["January", "Garnet", "Carnation"],
            ["February", "Amethyst", "Violet"],
            ["March", "Aquamarine", "Jonquil"],
            HRule(),
            ["April", "Diamond", "Sweetpea"],
            ["May", "Emerald", "Lily Of The Valley"],
            ["June", "Pearl", "Rose"],
            HRule(),
            ["July", "Ruby", "Larkspur"],
            ["August", "Peridot", "Gladiolus"],
            ["September", "Sapphire", "Aster"],
            HRule(),
            ["October", "Opal", "Calendula"],
            ["November", "Topaz", "Chrysanthemum"],
            ["December", "Turquoise", "Narcissus"],
        ],
        border_style=HEAVY_BORDERS,
    )
    assert str(tbl) == (
        "┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n"
        "┃Month    ┃Birthstone┃Birth Flower      ┃\n"
        "┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n"
        "┃January  ┃Garnet    ┃Carnation         ┃\n"
        "┃February ┃Amethyst  ┃Violet            ┃\n"
        "┃March    ┃Aquamarine┃Jonquil           ┃\n"
        "┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n"
        "┃April    ┃Diamond   ┃Sweetpea          ┃\n"
        "┃May      ┃Emerald   ┃Lily Of The Valley┃\n"
        "┃June     ┃Pearl     ┃Rose              ┃\n"
        "┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n"
        "┃July     ┃Ruby      ┃Larkspur          ┃\n"
        "┃August   ┃Peridot   ┃Gladiolus         ┃\n"
        "┃September┃Sapphire  ┃Aster             ┃\n"
        "┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n"
        "┃October  ┃Opal      ┃Calendula         ┃\n"
        "┃November ┃Topaz     ┃Chrysanthemum     ┃\n"
        "┃December ┃Turquoise ┃Narcissus         ┃\n"
        "┗━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛"
    )


def test_hrule_rule_border_styles():
    tbl = Txtble(
        headers=["Month", "Birthstone", "Birth Flower"],
        data=[
            ["January", "Garnet", "Carnation"],
            ["February", "Amethyst", "Violet"],
            ["March", "Aquamarine", "Jonquil"],
            HRule(border_style=ASCII_EQ_BORDERS),
            ["April", "Diamond", "Sweetpea"],
            ["May", "Emerald", "Lily Of The Valley"],
            ["June", "Pearl", "Rose"],
            HRule(border_style=LIGHT_BORDERS),
            ["July", "Ruby", "Larkspur"],
            ["August", "Peridot", "Gladiolus"],
            ["September", "Sapphire", "Aster"],
            HRule(border_style=HEAVY_BORDERS),
            ["October", "Opal", "Calendula"],
            ["November", "Topaz", "Chrysanthemum"],
            ["December", "Turquoise", "Narcissus"],
        ],
    )
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|Month    |Birthstone|Birth Flower      |\n"
        "+---------+----------+------------------+\n"
        "|January  |Garnet    |Carnation         |\n"
        "|February |Amethyst  |Violet            |\n"
        "|March    |Aquamarine|Jonquil           |\n"
        "+=========+==========+==================+\n"
        "|April    |Diamond   |Sweetpea          |\n"
        "|May      |Emerald   |Lily Of The Valley|\n"
        "|June     |Pearl     |Rose              |\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "|July     |Ruby      |Larkspur          |\n"
        "|August   |Peridot   |Gladiolus         |\n"
        "|September|Sapphire  |Aster             |\n"
        "┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n"
        "|October  |Opal      |Calendula         |\n"
        "|November |Topaz     |Chrysanthemum     |\n"
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )


def test_hrule_rule_and_table_border_styles():
    tbl = Txtble(
        headers=["Month", "Birthstone", "Birth Flower"],
        data=[
            ["January", "Garnet", "Carnation"],
            ["February", "Amethyst", "Violet"],
            ["March", "Aquamarine", "Jonquil"],
            HRule(border_style=ASCII_EQ_BORDERS),
            ["April", "Diamond", "Sweetpea"],
            ["May", "Emerald", "Lily Of The Valley"],
            ["June", "Pearl", "Rose"],
            HRule(border_style=LIGHT_BORDERS),
            ["July", "Ruby", "Larkspur"],
            ["August", "Peridot", "Gladiolus"],
            ["September", "Sapphire", "Aster"],
            HRule(border_style=HEAVY_BORDERS),
            ["October", "Opal", "Calendula"],
            ["November", "Topaz", "Chrysanthemum"],
            ["December", "Turquoise", "Narcissus"],
        ],
        border_style=HEAVY_BORDERS,
    )
    assert str(tbl) == (
        "┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n"
        "┃Month    ┃Birthstone┃Birth Flower      ┃\n"
        "┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n"
        "┃January  ┃Garnet    ┃Carnation         ┃\n"
        "┃February ┃Amethyst  ┃Violet            ┃\n"
        "┃March    ┃Aquamarine┃Jonquil           ┃\n"
        "+=========+==========+==================+\n"
        "┃April    ┃Diamond   ┃Sweetpea          ┃\n"
        "┃May      ┃Emerald   ┃Lily Of The Valley┃\n"
        "┃June     ┃Pearl     ┃Rose              ┃\n"
        "├─────────┼──────────┼──────────────────┤\n"
        "┃July     ┃Ruby      ┃Larkspur          ┃\n"
        "┃August   ┃Peridot   ┃Gladiolus         ┃\n"
        "┃September┃Sapphire  ┃Aster             ┃\n"
        "┣━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n"
        "┃October  ┃Opal      ┃Calendula         ┃\n"
        "┃November ┃Topaz     ┃Chrysanthemum     ┃\n"
        "┃December ┃Turquoise ┃Narcissus         ┃\n"
        "┗━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛"
    )


def test_consecutive_hrules():
    tbl = Txtble(
        headers=["Month", "Birthstone", "Birth Flower"],
        data=[
            ["January", "Garnet", "Carnation"],
            ["February", "Amethyst", "Violet"],
            ["March", "Aquamarine", "Jonquil"],
            ["April", "Diamond", "Sweetpea"],
            ["May", "Emerald", "Lily Of The Valley"],
            ["June", "Pearl", "Rose"],
            HRule(),
            HRule(),
            ["July", "Ruby", "Larkspur"],
            ["August", "Peridot", "Gladiolus"],
            ["September", "Sapphire", "Aster"],
            ["October", "Opal", "Calendula"],
            ["November", "Topaz", "Chrysanthemum"],
            ["December", "Turquoise", "Narcissus"],
        ],
    )
    assert str(tbl) == (
        "+---------+----------+------------------+\n"
        "|Month    |Birthstone|Birth Flower      |\n"
        "+---------+----------+------------------+\n"
        "|January  |Garnet    |Carnation         |\n"
        "|February |Amethyst  |Violet            |\n"
        "|March    |Aquamarine|Jonquil           |\n"
        "|April    |Diamond   |Sweetpea          |\n"
        "|May      |Emerald   |Lily Of The Valley|\n"
        "|June     |Pearl     |Rose              |\n"
        "+---------+----------+------------------+\n"
        "+---------+----------+------------------+\n"
        "|July     |Ruby      |Larkspur          |\n"
        "|August   |Peridot   |Gladiolus         |\n"
        "|September|Sapphire  |Aster             |\n"
        "|October  |Opal      |Calendula         |\n"
        "|November |Topaz     |Chrysanthemum     |\n"
        "|December |Turquoise |Narcissus         |\n"
        "+---------+----------+------------------+"
    )
