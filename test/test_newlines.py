from txtble    import Txtble
from test_data import DATA

def test_embedded_newlines():
    tbl = Txtble(
        [
            ['Verse 1', 'Twas brillig, and the slithy toves\n'
                        'Did gyre and gimble in the wabe;\n'
                        'All mimsy were the borogoves,\n'
                        'And the mome raths outgrabe.'],
            ['Verse 2', '"Beware the Jabberwock, my son!\n'
                        'The jaws that bite, the claws that catch!\n'
                        'Beware the Jubjub bird, and shun\n'
                        'The frumious Bandersnatch!"'],
        ]
    )
    assert str(tbl) == (
        '+-------+-----------------------------------------+\n'
        '|Verse 1|Twas brillig, and the slithy toves       |\n'
        '|       |Did gyre and gimble in the wabe;         |\n'
        '|       |All mimsy were the borogoves,            |\n'
        '|       |And the mome raths outgrabe.             |\n'
        '|Verse 2|"Beware the Jabberwock, my son!          |\n'
        '|       |The jaws that bite, the claws that catch!|\n'
        '|       |Beware the Jubjub bird, and shun         |\n'
        '|       |The frumious Bandersnatch!"              |\n'
        '+-------+-----------------------------------------+'
    )

def test_embedded_trailing_newlines():
    tbl = Txtble(
        [
            ['Verse 1', 'Twas brillig, and the slithy toves\n'
                        'Did gyre and gimble in the wabe;\n'
                        'All mimsy were the borogoves,\n'
                        'And the mome raths outgrabe.\n'],
            ['Verse 2', '"Beware the Jabberwock, my son!\n'
                        'The jaws that bite, the claws that catch!\n'
                        'Beware the Jubjub bird, and shun\n'
                        'The frumious Bandersnatch!"\n'],
        ]
    )
    assert str(tbl) == (
        '+-------+-----------------------------------------+\n'
        '|Verse 1|Twas brillig, and the slithy toves       |\n'
        '|       |Did gyre and gimble in the wabe;         |\n'
        '|       |All mimsy were the borogoves,            |\n'
        '|       |And the mome raths outgrabe.             |\n'
        '|       |                                         |\n'
        '|Verse 2|"Beware the Jabberwock, my son!          |\n'
        '|       |The jaws that bite, the claws that catch!|\n'
        '|       |Beware the Jubjub bird, and shun         |\n'
        '|       |The frumious Bandersnatch!"              |\n'
        '|       |                                         |\n'
        '+-------+-----------------------------------------+'
    )

def test_embedded_trailing_newlines_no_border():
    tbl = Txtble(
        [
            ['Verse 1', 'Twas brillig, and the slithy toves\n'
                        'Did gyre and gimble in the wabe;\n'
                        'All mimsy were the borogoves,\n'
                        'And the mome raths outgrabe.\n'],
            ['Verse 2', '"Beware the Jabberwock, my son!\n'
                        'The jaws that bite, the claws that catch!\n'
                        'Beware the Jubjub bird, and shun\n'
                        'The frumious Bandersnatch!"\n'],
        ],
        border=False,
    )
    assert str(tbl) == (
        'Verse 1|Twas brillig, and the slithy toves\n'
        '       |Did gyre and gimble in the wabe;\n'
        '       |All mimsy were the borogoves,\n'
        '       |And the mome raths outgrabe.\n'
        '       |\n'
        'Verse 2|"Beware the Jabberwock, my son!\n'
        '       |The jaws that bite, the claws that catch!\n'
        '       |Beware the Jubjub bird, and shun\n'
        '       |The frumious Bandersnatch!"\n'
        '       |'
    )

def test_embedded_form_feeds():
    tbl = Txtble(
        [
            ['Verse 1', 'Twas brillig, and the slithy toves\f'
                        'Did gyre and gimble in the wabe;\f'
                        'All mimsy were the borogoves,\f'
                        'And the mome raths outgrabe.'],
            ['Verse 2', '"Beware the Jabberwock, my son!\f'
                        'The jaws that bite, the claws that catch!\f'
                        'Beware the Jubjub bird, and shun\f'
                        'The frumious Bandersnatch!"'],
        ]
    )
    assert str(tbl) == (
        '+-------+-----------------------------------------+\n'
        '|Verse 1|Twas brillig, and the slithy toves       |\n'
        '|       |Did gyre and gimble in the wabe;         |\n'
        '|       |All mimsy were the borogoves,            |\n'
        '|       |And the mome raths outgrabe.             |\n'
        '|Verse 2|"Beware the Jabberwock, my son!          |\n'
        '|       |The jaws that bite, the claws that catch!|\n'
        '|       |Beware the Jubjub bird, and shun         |\n'
        '|       |The frumious Bandersnatch!"              |\n'
        '+-------+-----------------------------------------+'
    )

def test_embedded_vtabs():
    tbl = Txtble(
        [
            ['Verse 1', 'Twas brillig, and the slithy toves\v'
                        'Did gyre and gimble in the wabe;\v'
                        'All mimsy were the borogoves,\v'
                        'And the mome raths outgrabe.'],
            ['Verse 2', '"Beware the Jabberwock, my son!\v'
                        'The jaws that bite, the claws that catch!\v'
                        'Beware the Jubjub bird, and shun\v'
                        'The frumious Bandersnatch!"'],
        ]
    )
    assert str(tbl) == (
        '+-------+-----------------------------------------+\n'
        '|Verse 1|Twas brillig, and the slithy toves       |\n'
        '|       |Did gyre and gimble in the wabe;         |\n'
        '|       |All mimsy were the borogoves,            |\n'
        '|       |And the mome raths outgrabe.             |\n'
        '|Verse 2|"Beware the Jabberwock, my son!          |\n'
        '|       |The jaws that bite, the claws that catch!|\n'
        '|       |Beware the Jubjub bird, and shun         |\n'
        '|       |The frumious Bandersnatch!"              |\n'
        '+-------+-----------------------------------------+'
    )

def test_embedded_form_feeds_and_vtabs():
    tbl = Txtble(
        [
            ['Verse 1', 'Twas brillig, and the slithy toves\f'
                        'Did gyre and gimble in the wabe;\v'
                        'All mimsy were the borogoves,\f'
                        'And the mome raths outgrabe.'],
            ['Verse 2', '"Beware the Jabberwock, my son!\v'
                        'The jaws that bite, the claws that catch!\f'
                        'Beware the Jubjub bird, and shun\v'
                        'The frumious Bandersnatch!"'],
        ]
    )
    assert str(tbl) == (
        '+-------+-----------------------------------------+\n'
        '|Verse 1|Twas brillig, and the slithy toves       |\n'
        '|       |Did gyre and gimble in the wabe;         |\n'
        '|       |All mimsy were the borogoves,            |\n'
        '|       |And the mome raths outgrabe.             |\n'
        '|Verse 2|"Beware the Jabberwock, my son!          |\n'
        '|       |The jaws that bite, the claws that catch!|\n'
        '|       |Beware the Jubjub bird, and shun         |\n'
        '|       |The frumious Bandersnatch!"              |\n'
        '+-------+-----------------------------------------+'
    )

def test_padding_embedded_newlines():
    tbl = Txtble(
        [
            ['Verse 1', 'Twas brillig, and the slithy toves\n'
                        'Did gyre and gimble in the wabe;\n'
                        'All mimsy were the borogoves,\n'
                        'And the mome raths outgrabe.'],
            ['Verse 2', '"Beware the Jabberwock, my son!\n'
                        'The jaws that bite, the claws that catch!\n'
                        'Beware the Jubjub bird, and shun\n'
                        'The frumious Bandersnatch!"'],
        ],
        padding='.',
    )
    assert str(tbl) == (
        '+---------+-------------------------------------------+\n'
        '|.Verse 1.|.Twas brillig, and the slithy toves       .|\n'
        '|.       .|.Did gyre and gimble in the wabe;         .|\n'
        '|.       .|.All mimsy were the borogoves,            .|\n'
        '|.       .|.And the mome raths outgrabe.             .|\n'
        '|.Verse 2.|."Beware the Jabberwock, my son!          .|\n'
        '|.       .|.The jaws that bite, the claws that catch!.|\n'
        '|.       .|.Beware the Jubjub bird, and shun         .|\n'
        '|.       .|.The frumious Bandersnatch!"              .|\n'
        '+---------+-------------------------------------------+'
    )

def test_embedded_newline_headers():
    tbl = Txtble(
        headers=['Month', 'Birth Thingy\n(Gem)', 'Birth Thingy\n(Flower)'],
        data=DATA
    )
    assert str(tbl) ==(
        '+---------+------------+------------------+\n'
        '|Month    |Birth Thingy|Birth Thingy      |\n'
        '|         |(Gem)       |(Flower)          |\n'
        '+---------+------------+------------------+\n'
        '|January  |Garnet      |Carnation         |\n'
        '|February |Amethyst    |Violet            |\n'
        '|March    |Aquamarine  |Jonquil           |\n'
        '|April    |Diamond     |Sweetpea          |\n'
        '|May      |Emerald     |Lily Of The Valley|\n'
        '|June     |Pearl       |Rose              |\n'
        '|July     |Ruby        |Larkspur          |\n'
        '|August   |Peridot     |Gladiolus         |\n'
        '|September|Sapphire    |Aster             |\n'
        '|October  |Opal        |Calendula         |\n'
        '|November |Topaz       |Chrysanthemum     |\n'
        '|December |Turquoise   |Narcissus         |\n'
        '+---------+------------+------------------+'
    )
