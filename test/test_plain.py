from tabulator import Tabulator

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
    tbl = Tabulator(DATA, headers=HEADERS)
    assert str(tbl) == TABLE

def test_append_each():
    tbl = Tabulator(headers=HEADERS)
    for row in DATA:
        tbl.append(row)
    assert str(tbl) == TABLE

def test_extend_all():
    tbl = Tabulator(headers=HEADERS)
    tbl.extend(DATA)
    assert str(tbl) == TABLE

def test_no_border():
    tbl = Tabulator(DATA, headers=HEADERS, border=False)
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
    tbl = Tabulator(DATA, headers=HEADERS, border=False, rstrip=False)
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
    tbl = Tabulator(DATA, headers=HEADERS, rstrip=False)
    assert str(tbl) == TABLE

def test_no_headers():
    tbl = Tabulator(DATA)
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

def test_no_headers_no_border():
    tbl = Tabulator(DATA, border=False)
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

def test_embedded_newlines():
    tbl = Tabulator(
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
    tbl = Tabulator()
    assert str(tbl) == '++\n++'

def test_empty_no_border():
    tbl = Tabulator(border=False)
    assert str(tbl) == ''

def test_headers_no_rows():
    tbl = Tabulator(headers=('This', 'That'))
    assert str(tbl) == (
        '+----+----+\n'
        '|This|That|\n'
        '+----+----+'
    )

def test_headers_no_rows_no_border():
    tbl = Tabulator(headers=('This', 'That'), border=False)
    assert str(tbl) == 'This|That'
