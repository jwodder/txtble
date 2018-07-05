import pytest
from   txtble    import Txtble
from   test_data import HEADERS, DATA, TABLE

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

def test_headers_attr():
    tbl = Txtble(DATA)
    tbl.headers = HEADERS
    assert str(tbl) == TABLE

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

def test_headers_empty_row():
    tbl = Txtble(headers=('This', 'That'), data=[[]])
    assert str(tbl) == (
        '+----+----+\n'
        '|This|That|\n'
        '+----+----+\n'
        '|    |    |\n'
        '+----+----+'
    )

def test_headers_blank_row():
    tbl = Txtble(headers=('This', 'That'), data=[['', '']])
    assert str(tbl) == (
        '+----+----+\n'
        '|This|That|\n'
        '+----+----+\n'
        '|    |    |\n'
        '+----+----+'
    )

def test_headers_no_rows_no_border():
    tbl = Txtble(headers=('This', 'That'), border=False)
    assert str(tbl) == 'This|That'

def test_tabs():
    tbl = Txtble(
        headers=['Head\ter'],
        data=[
            ['\t*'],
            ['*\t*'],
            ['*\t\t*'],
        ],
    )
    assert str(tbl) == (
        '+-----------------+\n'
        '|Head    er       |\n'
        '+-----------------+\n'
        '|        *        |\n'
        '|*       *        |\n'
        '|*               *|\n'
        '+-----------------+'
    )

def test_extra_whitespace():
    tbl = Txtble([
        ['  .leading.', '.trailing.  '],
        ['              ', 'inn   er'],
    ])
    assert str(tbl) == (
        '+--------------+------------+\n'
        '|  .leading.   |.trailing.  |\n'
        '|              |inn   er    |\n'
        '+--------------+------------+'
    )

def test_extra_whitespace_no_border():
    tbl = Txtble([
        ['  .leading.', '.trailing.  '],
        ['              ', 'inn   er'],
    ], border=False)
    assert str(tbl) == (
        '  .leading.   |.trailing.  \n'
        '              |inn   er'
    )

def test_headers_matching_columns():
    tbl = Txtble(DATA, headers=HEADERS, columns=len(HEADERS))
    assert str(tbl) == TABLE

@pytest.mark.parametrize('columns', [len(HEADERS)-1, len(HEADERS)+1])
def test_headers_not_matching_columns(columns):
    tbl = Txtble(DATA, headers=HEADERS, columns=columns)
    with pytest.raises(ValueError):
        str(tbl)

@pytest.mark.parametrize('columns', [0, -1])
def test_bad_columns(columns):
    with pytest.raises(ValueError, match='columns must be at least 1'):
        Txtble(DATA, columns=columns)

@pytest.mark.parametrize('columns', [0, -1])
def test_bad_columns_attr(columns):
    tbl = Txtble(DATA)
    tbl.columns = columns
    with pytest.raises(ValueError, match='columns must be at least 1'):
        str(tbl)
