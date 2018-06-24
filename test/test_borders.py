import pytest
from   txtble    import Txtble
from   test_data import HEADERS, DATA, TABLE

@pytest.mark.parametrize('header_border', [None, True])
def test_no_border(header_border):
    tbl = Txtble(
        DATA,
        border        = False,
        header_border = header_border,
        headers       = HEADERS,
    )
    assert str(tbl) == (
        'Month    |Birthstone|Birth Flower\n'
        '---------+----------+------------------\n'
        'January  |Garnet    |Carnation\n'
        'February |Amethyst  |Violet\n'
        'March    |Aquamarine|Jonquil\n'
        'April    |Diamond   |Sweetpea\n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose\n'
        'July     |Ruby      |Larkspur\n'
        'August   |Peridot   |Gladiolus\n'
        'September|Sapphire  |Aster\n'
        'October  |Opal      |Calendula\n'
        'November |Topaz     |Chrysanthemum\n'
        'December |Turquoise |Narcissus'
    )

def test_no_border_no_rstrip():
    tbl = Txtble(DATA, headers=HEADERS, border=False, rstrip=False)
    assert str(tbl) == (
        'Month    |Birthstone|Birth Flower      \n'
        '---------+----------+------------------\n'
        'January  |Garnet    |Carnation         \n'
        'February |Amethyst  |Violet            \n'
        'March    |Aquamarine|Jonquil           \n'
        'April    |Diamond   |Sweetpea          \n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose              \n'
        'July     |Ruby      |Larkspur          \n'
        'August   |Peridot   |Gladiolus         \n'
        'September|Sapphire  |Aster             \n'
        'October  |Opal      |Calendula         \n'
        'November |Topaz     |Chrysanthemum     \n'
        'December |Turquoise |Narcissus         '
    )

@pytest.mark.parametrize('header_border', [None, False])
def test_no_headers_no_border(header_border):
    tbl = Txtble(DATA, border=False, header_border=header_border)
    assert str(tbl) == (
        'January  |Garnet    |Carnation\n'
        'February |Amethyst  |Violet\n'
        'March    |Aquamarine|Jonquil\n'
        'April    |Diamond   |Sweetpea\n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose\n'
        'July     |Ruby      |Larkspur\n'
        'August   |Peridot   |Gladiolus\n'
        'September|Sapphire  |Aster\n'
        'October  |Opal      |Calendula\n'
        'November |Topaz     |Chrysanthemum\n'
        'December |Turquoise |Narcissus'
    )

def test_header_border_no_headers_no_border():
    tbl = Txtble(DATA, border=False, header_border=True)
    assert str(tbl) == (
        '---------+----------+------------------\n'
        'January  |Garnet    |Carnation\n'
        'February |Amethyst  |Violet\n'
        'March    |Aquamarine|Jonquil\n'
        'April    |Diamond   |Sweetpea\n'
        'May      |Emerald   |Lily Of The Valley\n'
        'June     |Pearl     |Rose\n'
        'July     |Ruby      |Larkspur\n'
        'August   |Peridot   |Gladiolus\n'
        'September|Sapphire  |Aster\n'
        'October  |Opal      |Calendula\n'
        'November |Topaz     |Chrysanthemum\n'
        'December |Turquoise |Narcissus'
    )

def test_row_border():
    tbl = Txtble(DATA, headers=HEADERS, row_border=True)
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|Month    |Birthstone|Birth Flower      |\n'
        '+---------+----------+------------------+\n'
        '|January  |Garnet    |Carnation         |\n'
        '+---------+----------+------------------+\n'
        '|February |Amethyst  |Violet            |\n'
        '+---------+----------+------------------+\n'
        '|March    |Aquamarine|Jonquil           |\n'
        '+---------+----------+------------------+\n'
        '|April    |Diamond   |Sweetpea          |\n'
        '+---------+----------+------------------+\n'
        '|May      |Emerald   |Lily Of The Valley|\n'
        '+---------+----------+------------------+\n'
        '|June     |Pearl     |Rose              |\n'
        '+---------+----------+------------------+\n'
        '|July     |Ruby      |Larkspur          |\n'
        '+---------+----------+------------------+\n'
        '|August   |Peridot   |Gladiolus         |\n'
        '+---------+----------+------------------+\n'
        '|September|Sapphire  |Aster             |\n'
        '+---------+----------+------------------+\n'
        '|October  |Opal      |Calendula         |\n'
        '+---------+----------+------------------+\n'
        '|November |Topaz     |Chrysanthemum     |\n'
        '+---------+----------+------------------+\n'
        '|December |Turquoise |Narcissus         |\n'
        '+---------+----------+------------------+'
    )

def test_row_border_embedded_newlines():
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
        row_border=True,
    )
    assert str(tbl) == (
        '+-------+-----------------------------------------+\n'
        '|Verse 1|Twas brillig, and the slithy toves       |\n'
        '|       |Did gyre and gimble in the wabe;         |\n'
        '|       |All mimsy were the borogoves,            |\n'
        '|       |And the mome raths outgrabe.             |\n'
        '+-------+-----------------------------------------+\n'
        '|Verse 2|"Beware the Jabberwock, my son!          |\n'
        '|       |The jaws that bite, the claws that catch!|\n'
        '|       |Beware the Jubjub bird, and shun         |\n'
        '|       |The frumious Bandersnatch!"              |\n'
        '+-------+-----------------------------------------+'
    )

def test_no_column_border():
    tbl = Txtble(DATA, headers=HEADERS, column_border=False)
    assert str(tbl) == (
        '+-------------------------------------+\n'
        '|Month    BirthstoneBirth Flower      |\n'
        '+-------------------------------------+\n'
        '|January  Garnet    Carnation         |\n'
        '|February Amethyst  Violet            |\n'
        '|March    AquamarineJonquil           |\n'
        '|April    Diamond   Sweetpea          |\n'
        '|May      Emerald   Lily Of The Valley|\n'
        '|June     Pearl     Rose              |\n'
        '|July     Ruby      Larkspur          |\n'
        '|August   Peridot   Gladiolus         |\n'
        '|SeptemberSapphire  Aster             |\n'
        '|October  Opal      Calendula         |\n'
        '|November Topaz     Chrysanthemum     |\n'
        '|December Turquoise Narcissus         |\n'
        '+-------------------------------------+'
    )

def test_row_border_no_column_border():
    tbl = Txtble(DATA, headers=HEADERS, column_border=False, row_border=True)
    assert str(tbl) == (
        '+-------------------------------------+\n'
        '|Month    BirthstoneBirth Flower      |\n'
        '+-------------------------------------+\n'
        '|January  Garnet    Carnation         |\n'
        '+-------------------------------------+\n'
        '|February Amethyst  Violet            |\n'
        '+-------------------------------------+\n'
        '|March    AquamarineJonquil           |\n'
        '+-------------------------------------+\n'
        '|April    Diamond   Sweetpea          |\n'
        '+-------------------------------------+\n'
        '|May      Emerald   Lily Of The Valley|\n'
        '+-------------------------------------+\n'
        '|June     Pearl     Rose              |\n'
        '+-------------------------------------+\n'
        '|July     Ruby      Larkspur          |\n'
        '+-------------------------------------+\n'
        '|August   Peridot   Gladiolus         |\n'
        '+-------------------------------------+\n'
        '|SeptemberSapphire  Aster             |\n'
        '+-------------------------------------+\n'
        '|October  Opal      Calendula         |\n'
        '+-------------------------------------+\n'
        '|November Topaz     Chrysanthemum     |\n'
        '+-------------------------------------+\n'
        '|December Turquoise Narcissus         |\n'
        '+-------------------------------------+'
    )

@pytest.mark.parametrize('header_border', [None, True])
def test_headers_header_border(header_border):
    tbl = Txtble(DATA, headers=HEADERS, header_border=header_border)
    assert str(tbl) == TABLE

def test_headers_no_header_border():
    tbl = Txtble(DATA, headers=HEADERS, header_border=False)
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|Month    |Birthstone|Birth Flower      |\n'
        '|January  |Garnet    |Carnation         |\n'
        '|February |Amethyst  |Violet            |\n'
        '|March    |Aquamarine|Jonquil           |\n'
        '|April    |Diamond   |Sweetpea          |\n'
        '|May      |Emerald   |Lily Of The Valley|\n'
        '|June     |Pearl     |Rose              |\n'
        '|July     |Ruby      |Larkspur          |\n'
        '|August   |Peridot   |Gladiolus         |\n'
        '|September|Sapphire  |Aster             |\n'
        '|October  |Opal      |Calendula         |\n'
        '|November |Topaz     |Chrysanthemum     |\n'
        '|December |Turquoise |Narcissus         |\n'
        '+---------+----------+------------------+'
    )

def test_row_border_no_header_border():
    tbl = Txtble(DATA, headers=HEADERS, row_border=True, header_border=False)
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|Month    |Birthstone|Birth Flower      |\n'
        '|January  |Garnet    |Carnation         |\n'
        '+---------+----------+------------------+\n'
        '|February |Amethyst  |Violet            |\n'
        '+---------+----------+------------------+\n'
        '|March    |Aquamarine|Jonquil           |\n'
        '+---------+----------+------------------+\n'
        '|April    |Diamond   |Sweetpea          |\n'
        '+---------+----------+------------------+\n'
        '|May      |Emerald   |Lily Of The Valley|\n'
        '+---------+----------+------------------+\n'
        '|June     |Pearl     |Rose              |\n'
        '+---------+----------+------------------+\n'
        '|July     |Ruby      |Larkspur          |\n'
        '+---------+----------+------------------+\n'
        '|August   |Peridot   |Gladiolus         |\n'
        '+---------+----------+------------------+\n'
        '|September|Sapphire  |Aster             |\n'
        '+---------+----------+------------------+\n'
        '|October  |Opal      |Calendula         |\n'
        '+---------+----------+------------------+\n'
        '|November |Topaz     |Chrysanthemum     |\n'
        '+---------+----------+------------------+\n'
        '|December |Turquoise |Narcissus         |\n'
        '+---------+----------+------------------+'
    )

def test_all_borders_off():
    tbl = Txtble(
        DATA,
        border        = False,
        column_border = False,
        header_border = False,
        headers       = HEADERS,
    )
    assert str(tbl) == (
        'Month    BirthstoneBirth Flower\n'
        'January  Garnet    Carnation\n'
        'February Amethyst  Violet\n'
        'March    AquamarineJonquil\n'
        'April    Diamond   Sweetpea\n'
        'May      Emerald   Lily Of The Valley\n'
        'June     Pearl     Rose\n'
        'July     Ruby      Larkspur\n'
        'August   Peridot   Gladiolus\n'
        'SeptemberSapphire  Aster\n'
        'October  Opal      Calendula\n'
        'November Topaz     Chrysanthemum\n'
        'December Turquoise Narcissus'
    )

def test_invert_all_borders():
    tbl = Txtble(
        DATA,
        border        = False,
        column_border = False,
        header_border = False,
        headers       = HEADERS,
        row_border    = True,
    )
    assert str(tbl) == (
        'Month    BirthstoneBirth Flower\n'
        'January  Garnet    Carnation\n'
        '-------------------------------------\n'
        'February Amethyst  Violet\n'
        '-------------------------------------\n'
        'March    AquamarineJonquil\n'
        '-------------------------------------\n'
        'April    Diamond   Sweetpea\n'
        '-------------------------------------\n'
        'May      Emerald   Lily Of The Valley\n'
        '-------------------------------------\n'
        'June     Pearl     Rose\n'
        '-------------------------------------\n'
        'July     Ruby      Larkspur\n'
        '-------------------------------------\n'
        'August   Peridot   Gladiolus\n'
        '-------------------------------------\n'
        'SeptemberSapphire  Aster\n'
        '-------------------------------------\n'
        'October  Opal      Calendula\n'
        '-------------------------------------\n'
        'November Topaz     Chrysanthemum\n'
        '-------------------------------------\n'
        'December Turquoise Narcissus'
    )

def test_outer_border_only():
    tbl = Txtble(
        DATA,
        border        = True,
        column_border = False,
        header_border = False,
        headers       = HEADERS,
    )
    assert str(tbl) == (
        '+-------------------------------------+\n'
        '|Month    BirthstoneBirth Flower      |\n'
        '|January  Garnet    Carnation         |\n'
        '|February Amethyst  Violet            |\n'
        '|March    AquamarineJonquil           |\n'
        '|April    Diamond   Sweetpea          |\n'
        '|May      Emerald   Lily Of The Valley|\n'
        '|June     Pearl     Rose              |\n'
        '|July     Ruby      Larkspur          |\n'
        '|August   Peridot   Gladiolus         |\n'
        '|SeptemberSapphire  Aster             |\n'
        '|October  Opal      Calendula         |\n'
        '|November Topaz     Chrysanthemum     |\n'
        '|December Turquoise Narcissus         |\n'
        '+-------------------------------------+'
    )
