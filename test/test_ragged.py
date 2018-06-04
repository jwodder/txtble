import pytest
from   tabulator import Tabulator

DATA = [
    ['1', '1'],
    ['Z_4', '1', 'x', 'x^2', 'x^3'],
    ['V_4', '1', 'a', 'b', 'ab'],
    ['Z_6', '1', 'x', 'x^2', 'x^3', 'x^4', 'x^5'],
    ['S_3', '1', 'a', 'b', 'aba', 'ba', 'ab'],
]

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers(header_fill):
    tbl = Tabulator(
        data        = DATA,
        header_fill = header_fill,
    )
    assert str(tbl) == (
        '+---+-+-+---+---+---+---+\n'
        '|1  |1| |   |   |   |   |\n'
        '|Z_4|1|x|x^2|x^3|   |   |\n'
        '|V_4|1|a|b  |ab |   |   |\n'
        '|Z_6|1|x|x^2|x^3|x^4|x^5|\n'
        '|S_3|1|a|b  |aba|ba |ab |\n'
        '+---+-+-+---+---+---+---+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_row_fill(header_fill):
    tbl = Tabulator(
        data        = DATA,
        header_fill = header_fill,
        row_fill    = '#',
    )
    assert str(tbl) == (
        '+---+-+-+---+---+---+---+\n'
        '|1  |1|#|#  |#  |#  |#  |\n'
        '|Z_4|1|x|x^2|x^3|#  |#  |\n'
        '|V_4|1|a|b  |ab |#  |#  |\n'
        '|Z_6|1|x|x^2|x^3|x^4|x^5|\n'
        '|S_3|1|a|b  |aba|ba |ab |\n'
        '+---+-+-+---+---+---+---+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_long_row_fill(header_fill):
    tbl = Tabulator(
        data        = DATA,
        header_fill = header_fill,
        row_fill    = 'Empty!',
    )
    assert str(tbl) == (
        '+---+-+------+------+------+------+------+\n'
        '|1  |1|Empty!|Empty!|Empty!|Empty!|Empty!|\n'
        '|Z_4|1|x     |x^2   |x^3   |Empty!|Empty!|\n'
        '|V_4|1|a     |b     |ab    |Empty!|Empty!|\n'
        '|Z_6|1|x     |x^2   |x^3   |x^4   |x^5   |\n'
        '|S_3|1|a     |b     |aba   |ba    |ab    |\n'
        '+---+-+------+------+------+------+------+'
    )

@pytest.mark.parametrize('row_fill', ['', 'foo'])
def test_long_rows_headers(row_fill):
    tbl = Tabulator(
        data     = DATA,
        headers  = ('Group', 'Elements'),
        row_fill = row_fill,
    )
    assert str(tbl) == (
        '+-----+--------+\n'
        '|Group|Elements|\n'
        '+-----+--------+\n'
        '|1    |1       |\n'
        '|Z_4  |1       |\n'
        '|V_4  |1       |\n'
        '|Z_6  |1       |\n'
        '|S_3  |1       |\n'
        '+-----+--------+'
    )

def test_long_rows_headers_header_fill():
    tbl = Tabulator(
        data        = DATA,
        header_fill = '?',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+-+---+---+---+---+\n'
        '|Group|Elements|?|?  |?  |?  |?  |\n'
        '+-----+--------+-+---+---+---+---+\n'
        '|1    |1       | |   |   |   |   |\n'
        '|Z_4  |1       |x|x^2|x^3|   |   |\n'
        '|V_4  |1       |a|b  |ab |   |   |\n'
        '|Z_6  |1       |x|x^2|x^3|x^4|x^5|\n'
        '|S_3  |1       |a|b  |aba|ba |ab |\n'
        '+-----+--------+-+---+---+---+---+'
    )

def test_long_rows_headers_empty_header_fill():
    tbl = Tabulator(
        data        = DATA,
        header_fill = '',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+-+---+---+---+---+\n'
        '|Group|Elements| |   |   |   |   |\n'
        '+-----+--------+-+---+---+---+---+\n'
        '|1    |1       | |   |   |   |   |\n'
        '|Z_4  |1       |x|x^2|x^3|   |   |\n'
        '|V_4  |1       |a|b  |ab |   |   |\n'
        '|Z_6  |1       |x|x^2|x^3|x^4|x^5|\n'
        '|S_3  |1       |a|b  |aba|ba |ab |\n'
        '+-----+--------+-+---+---+---+---+'
    )

def test_long_rows_headers_long_header_fill():
    tbl = Tabulator(
        data        = DATA,
        header_fill = 'Extra!',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+------+------+------+------+------+\n'
        '|Group|Elements|Extra!|Extra!|Extra!|Extra!|Extra!|\n'
        '+-----+--------+------+------+------+------+------+\n'
        '|1    |1       |      |      |      |      |      |\n'
        '|Z_4  |1       |x     |x^2   |x^3   |      |      |\n'
        '|V_4  |1       |a     |b     |ab    |      |      |\n'
        '|Z_6  |1       |x     |x^2   |x^3   |x^4   |x^5   |\n'
        '|S_3  |1       |a     |b     |aba   |ba    |ab    |\n'
        '+-----+--------+------+------+------+------+------+'
    )

def test_long_rows_headers_header_fill_row_fill():
    tbl = Tabulator(
        data        = DATA,
        header_fill = '?',
        headers     = ('Group', 'Elements'),
        row_fill    = '#',
    )
    assert str(tbl) == (
        '+-----+--------+-+---+---+---+---+\n'
        '|Group|Elements|?|?  |?  |?  |?  |\n'
        '+-----+--------+-+---+---+---+---+\n'
        '|1    |1       |#|#  |#  |#  |#  |\n'
        '|Z_4  |1       |x|x^2|x^3|#  |#  |\n'
        '|V_4  |1       |a|b  |ab |#  |#  |\n'
        '|Z_6  |1       |x|x^2|x^3|x^4|x^5|\n'
        '|S_3  |1       |a|b  |aba|ba |ab |\n'
        '+-----+--------+-+---+---+---+---+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_short_rows_headers(header_fill):
    tbl = Tabulator(
        data        = DATA,
        header_fill = header_fill,
        headers     = ('Group', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6'),
    )
    assert str(tbl) == (
        '+-----+--+--+---+---+---+---+\n'
        '|Group|E1|E2|E3 |E4 |E5 |E6 |\n'
        '+-----+--+--+---+---+---+---+\n'
        '|1    |1 |  |   |   |   |   |\n'
        '|Z_4  |1 |x |x^2|x^3|   |   |\n'
        '|V_4  |1 |a |b  |ab |   |   |\n'
        '|Z_6  |1 |x |x^2|x^3|x^4|x^5|\n'
        '|S_3  |1 |a |b  |aba|ba |ab |\n'
        '+-----+--+--+---+---+---+---+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_short_rows_headers_row_fill(header_fill):
    tbl = Tabulator(
        data        = DATA,
        header_fill = header_fill,
        headers     = ('Group', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6'),
        row_fill    = '#',
    )
    assert str(tbl) == (
        '+-----+--+--+---+---+---+---+\n'
        '|Group|E1|E2|E3 |E4 |E5 |E6 |\n'
        '+-----+--+--+---+---+---+---+\n'
        '|1    |1 |# |#  |#  |#  |#  |\n'
        '|Z_4  |1 |x |x^2|x^3|#  |#  |\n'
        '|V_4  |1 |a |b  |ab |#  |#  |\n'
        '|Z_6  |1 |x |x^2|x^3|x^4|x^5|\n'
        '|S_3  |1 |a |b  |aba|ba |ab |\n'
        '+-----+--+--+---+---+---+---+'
    )