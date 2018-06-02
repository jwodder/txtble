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
