import pytest
from   txtble import Txtble

# Taken from /usr/share/misc/birthtoken.gz in Ubuntu Xenial's miscfiles package:
HEADERS = ['Month', 'Birthstone', 'Birth Flower']
DATA = [
    ['January',   'Garnet',     'Carnation'],
    ['February',  'Amethyst',   'Violet'],
    ['March',     'Aquamarine', 'Jonquil'],
    ['April',     'Diamond',    'Sweetpea'],
    ['May',       'Emerald',    'Lily Of The Valley'],
    ['June',      'Pearl',      'Rose'],
    ['July',      'Ruby',       'Larkspur'],
    ['August',    'Peridot',    'Gladiolus'],
    ['September', 'Sapphire',   'Aster'],
    ['October',   'Opal',       'Calendula'],
    ['November',  'Topaz',      'Chrysanthemum'],
    ['December',  'Turquoise',  'Narcissus'],
]

TABLE = (
    '+---------+----------+------------------+\n'
    '|Month    |Birthstone|Birth Flower      |\n'
    '+---------+----------+------------------+\n'
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

def test_one_expression():
    tbl = Txtble(DATA, headers=HEADERS)
    assert str(tbl) == TABLE

def test_append_each():
    tbl = Txtble(headers=HEADERS)
    for row in DATA:
        tbl.append(row)
    assert str(tbl) == TABLE

def test_extend_all():
    tbl = Txtble(headers=HEADERS)
    tbl.extend(DATA)
    assert str(tbl) == TABLE

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

def test_no_rstrip():
    tbl = Txtble(DATA, headers=HEADERS, rstrip=False)
    assert str(tbl) == TABLE

@pytest.mark.parametrize('header_border', [None, True, False])
def test_no_headers(header_border):
    tbl = Txtble(DATA, header_border=header_border)
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
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

def test_empty():
    tbl = Txtble()
    assert str(tbl) == '++\n++'

def test_empty_no_border():
    tbl = Txtble(border=False)
    assert str(tbl) == ''

def test_headers_no_rows():
    tbl = Txtble(headers=('This', 'That'))
    assert str(tbl) == (
        '+----+----+\n'
        '|This|That|\n'
        '+----+----+'
    )

def test_headers_no_rows_no_border():
    tbl = Txtble(headers=('This', 'That'), border=False)
    assert str(tbl) == 'This|That'

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
