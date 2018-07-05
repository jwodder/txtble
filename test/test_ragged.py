import pytest
from   txtble import Txtble

DATA = [
    ['1', '1'],
    ['Z_6', '1', 'x', 'x^2', 'x^3', 'x^4', 'x^5'],
    ['S_3', '1', 'a', 'b', 'aba', 'ba', 'ab'],
    ['Z_4', '1', 'x', 'x^2', 'x^3'],
    ['V_4', '1', 'a', 'b', 'ab'],
]

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers(header_fill):
    tbl = Txtble(
        data        = DATA,
        header_fill = header_fill,
    )
    assert str(tbl) == (
        '+---+-+-+---+---+---+---+\n'
        '|1  |1| |   |   |   |   |\n'
        '|Z_6|1|x|x^2|x^3|x^4|x^5|\n'
        '|S_3|1|a|b  |aba|ba |ab |\n'
        '|Z_4|1|x|x^2|x^3|   |   |\n'
        '|V_4|1|a|b  |ab |   |   |\n'
        '+---+-+-+---+---+---+---+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_row_fill(header_fill):
    tbl = Txtble(
        data        = DATA,
        header_fill = header_fill,
        row_fill    = '#',
    )
    assert str(tbl) == (
        '+---+-+-+---+---+---+---+\n'
        '|1  |1|#|#  |#  |#  |#  |\n'
        '|Z_6|1|x|x^2|x^3|x^4|x^5|\n'
        '|S_3|1|a|b  |aba|ba |ab |\n'
        '|Z_4|1|x|x^2|x^3|#  |#  |\n'
        '|V_4|1|a|b  |ab |#  |#  |\n'
        '+---+-+-+---+---+---+---+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_long_row_fill(header_fill):
    tbl = Txtble(
        data        = DATA,
        header_fill = header_fill,
        row_fill    = 'Empty!',
    )
    assert str(tbl) == (
        '+---+-+------+------+------+------+------+\n'
        '|1  |1|Empty!|Empty!|Empty!|Empty!|Empty!|\n'
        '|Z_6|1|x     |x^2   |x^3   |x^4   |x^5   |\n'
        '|S_3|1|a     |b     |aba   |ba    |ab    |\n'
        '|Z_4|1|x     |x^2   |x^3   |Empty!|Empty!|\n'
        '|V_4|1|a     |b     |ab    |Empty!|Empty!|\n'
        '+---+-+------+------+------+------+------+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_tab_row_fill(header_fill):
    tbl = Txtble(
        data        = DATA,
        header_fill = header_fill,
        row_fill    = 'Fill\ter',
    )
    assert str(tbl) == (
        '+---+-+----------+----------+----------+----------+----------+\n'
        '|1  |1|Fill    er|Fill    er|Fill    er|Fill    er|Fill    er|\n'
        '|Z_6|1|x         |x^2       |x^3       |x^4       |x^5       |\n'
        '|S_3|1|a         |b         |aba       |ba        |ab        |\n'
        '|Z_4|1|x         |x^2       |x^3       |Fill    er|Fill    er|\n'
        '|V_4|1|a         |b         |ab        |Fill    er|Fill    er|\n'
        '+---+-+----------+----------+----------+----------+----------+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_multiline_row_fill(header_fill):
    tbl = Txtble(
        data        = DATA,
        header_fill = header_fill,
        row_fill    = 'Fill\ner',
    )
    assert str(tbl) == (
        '+---+-+----+----+----+----+----+\n'
        '|1  |1|Fill|Fill|Fill|Fill|Fill|\n'
        '|   | |er  |er  |er  |er  |er  |\n'
        '|Z_6|1|x   |x^2 |x^3 |x^4 |x^5 |\n'
        '|S_3|1|a   |b   |aba |ba  |ab  |\n'
        '|Z_4|1|x   |x^2 |x^3 |Fill|Fill|\n'
        '|   | |    |    |    |er  |er  |\n'
        '|V_4|1|a   |b   |ab  |Fill|Fill|\n'
        '|   | |    |    |    |er  |er  |\n'
        '+---+-+----+----+----+----+----+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_columns(header_fill):
    tbl = Txtble(
        columns     = 6,
        data        = DATA,
        header_fill = header_fill,
    )
    assert str(tbl) == (
        '+---+-+-+---+---+---+\n'
        '|1  |1| |   |   |   |\n'
        '|Z_6|1|x|x^2|x^3|x^4|\n'
        '|S_3|1|a|b  |aba|ba |\n'
        '|Z_4|1|x|x^2|x^3|   |\n'
        '|V_4|1|a|b  |ab |   |\n'
        '+---+-+-+---+---+---+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_extra_columns(header_fill):
    tbl = Txtble(
        columns     = 8,
        data        = DATA,
        header_fill = header_fill,
    )
    assert str(tbl) == (
        '+---+-+-+---+---+---+---++\n'
        '|1  |1| |   |   |   |   ||\n'
        '|Z_6|1|x|x^2|x^3|x^4|x^5||\n'
        '|S_3|1|a|b  |aba|ba |ab ||\n'
        '|Z_4|1|x|x^2|x^3|   |   ||\n'
        '|V_4|1|a|b  |ab |   |   ||\n'
        '+---+-+-+---+---+---+---++'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_ragged_rows_no_headers_extra_columns_row_fill(header_fill):
    tbl = Txtble(
        columns     = 8,
        data        = DATA,
        header_fill = header_fill,
        row_fill    = '#',
    )
    assert str(tbl) == (
        '+---+-+-+---+---+---+---+-+\n'
        '|1  |1|#|#  |#  |#  |#  |#|\n'
        '|Z_6|1|x|x^2|x^3|x^4|x^5|#|\n'
        '|S_3|1|a|b  |aba|ba |ab |#|\n'
        '|Z_4|1|x|x^2|x^3|#  |#  |#|\n'
        '|V_4|1|a|b  |ab |#  |#  |#|\n'
        '+---+-+-+---+---+---+---+-+'
    )

@pytest.mark.parametrize('row_fill', ['', 'foo'])
def test_long_rows_headers(row_fill):
    tbl = Txtble(
        data     = DATA,
        headers  = ('Group', 'Elements'),
        row_fill = row_fill,
    )
    assert str(tbl) == (
        '+-----+--------+\n'
        '|Group|Elements|\n'
        '+-----+--------+\n'
        '|1    |1       |\n'
        '|Z_6  |1       |\n'
        '|S_3  |1       |\n'
        '|Z_4  |1       |\n'
        '|V_4  |1       |\n'
        '+-----+--------+'
    )

def test_long_rows_headers_header_fill():
    tbl = Txtble(
        data        = DATA,
        header_fill = '?',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+-+---+---+---+---+\n'
        '|Group|Elements|?|?  |?  |?  |?  |\n'
        '+-----+--------+-+---+---+---+---+\n'
        '|1    |1       | |   |   |   |   |\n'
        '|Z_6  |1       |x|x^2|x^3|x^4|x^5|\n'
        '|S_3  |1       |a|b  |aba|ba |ab |\n'
        '|Z_4  |1       |x|x^2|x^3|   |   |\n'
        '|V_4  |1       |a|b  |ab |   |   |\n'
        '+-----+--------+-+---+---+---+---+'
    )

def test_long_rows_headers_empty_header_fill():
    tbl = Txtble(
        data        = DATA,
        header_fill = '',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+-+---+---+---+---+\n'
        '|Group|Elements| |   |   |   |   |\n'
        '+-----+--------+-+---+---+---+---+\n'
        '|1    |1       | |   |   |   |   |\n'
        '|Z_6  |1       |x|x^2|x^3|x^4|x^5|\n'
        '|S_3  |1       |a|b  |aba|ba |ab |\n'
        '|Z_4  |1       |x|x^2|x^3|   |   |\n'
        '|V_4  |1       |a|b  |ab |   |   |\n'
        '+-----+--------+-+---+---+---+---+'
    )

def test_long_rows_headers_long_header_fill():
    tbl = Txtble(
        data        = DATA,
        header_fill = 'Extra!',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+------+------+------+------+------+\n'
        '|Group|Elements|Extra!|Extra!|Extra!|Extra!|Extra!|\n'
        '+-----+--------+------+------+------+------+------+\n'
        '|1    |1       |      |      |      |      |      |\n'
        '|Z_6  |1       |x     |x^2   |x^3   |x^4   |x^5   |\n'
        '|S_3  |1       |a     |b     |aba   |ba    |ab    |\n'
        '|Z_4  |1       |x     |x^2   |x^3   |      |      |\n'
        '|V_4  |1       |a     |b     |ab    |      |      |\n'
        '+-----+--------+------+------+------+------+------+'
    )

def test_long_rows_headers_tab_header_fill():
    tbl = Txtble(
        data        = DATA,
        header_fill = 'Fill\ter',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+----------+----------+----------+----------+----------+\n'
        '|Group|Elements|Fill    er|Fill    er|Fill    er|Fill    er|Fill    er|\n'
        '+-----+--------+----------+----------+----------+----------+----------+\n'
        '|1    |1       |          |          |          |          |          |\n'
        '|Z_6  |1       |x         |x^2       |x^3       |x^4       |x^5       |\n'
        '|S_3  |1       |a         |b         |aba       |ba        |ab        |\n'
        '|Z_4  |1       |x         |x^2       |x^3       |          |          |\n'
        '|V_4  |1       |a         |b         |ab        |          |          |\n'
        '+-----+--------+----------+----------+----------+----------+----------+'
    )

def test_long_rows_headers_multiline_header_fill():
    tbl = Txtble(
        data        = DATA,
        header_fill = 'Fill\ner',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+----+----+----+----+----+\n'
        '|Group|Elements|Fill|Fill|Fill|Fill|Fill|\n'
        '|     |        |er  |er  |er  |er  |er  |\n'
        '+-----+--------+----+----+----+----+----+\n'
        '|1    |1       |    |    |    |    |    |\n'
        '|Z_6  |1       |x   |x^2 |x^3 |x^4 |x^5 |\n'
        '|S_3  |1       |a   |b   |aba |ba  |ab  |\n'
        '|Z_4  |1       |x   |x^2 |x^3 |    |    |\n'
        '|V_4  |1       |a   |b   |ab  |    |    |\n'
        '+-----+--------+----+----+----+----+----+'
    )

def test_long_rows_headers_header_fill_row_fill():
    tbl = Txtble(
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
        '|Z_6  |1       |x|x^2|x^3|x^4|x^5|\n'
        '|S_3  |1       |a|b  |aba|ba |ab |\n'
        '|Z_4  |1       |x|x^2|x^3|#  |#  |\n'
        '|V_4  |1       |a|b  |ab |#  |#  |\n'
        '+-----+--------+-+---+---+---+---+'
    )

def test_long_rows_headers_header_fill_row_fill_padding():
    tbl = Txtble(
        data        = DATA,
        header_fill = '?',
        headers     = ('Group', 'Elements'),
        padding     = ' ',
        row_fill    = '#',
    )
    assert str(tbl) == (
        '+-------+----------+---+-----+-----+-----+-----+\n'
        '| Group | Elements | ? | ?   | ?   | ?   | ?   |\n'
        '+-------+----------+---+-----+-----+-----+-----+\n'
        '| 1     | 1        | # | #   | #   | #   | #   |\n'
        '| Z_6   | 1        | x | x^2 | x^3 | x^4 | x^5 |\n'
        '| S_3   | 1        | a | b   | aba | ba  | ab  |\n'
        '| Z_4   | 1        | x | x^2 | x^3 | #   | #   |\n'
        '| V_4   | 1        | a | b   | ab  | #   | #   |\n'
        '+-------+----------+---+-----+-----+-----+-----+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_short_rows_headers(header_fill):
    tbl = Txtble(
        data        = DATA,
        header_fill = header_fill,
        headers     = ('Group', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6'),
    )
    assert str(tbl) == (
        '+-----+--+--+---+---+---+---+\n'
        '|Group|E1|E2|E3 |E4 |E5 |E6 |\n'
        '+-----+--+--+---+---+---+---+\n'
        '|1    |1 |  |   |   |   |   |\n'
        '|Z_6  |1 |x |x^2|x^3|x^4|x^5|\n'
        '|S_3  |1 |a |b  |aba|ba |ab |\n'
        '|Z_4  |1 |x |x^2|x^3|   |   |\n'
        '|V_4  |1 |a |b  |ab |   |   |\n'
        '+-----+--+--+---+---+---+---+'
    )

@pytest.mark.parametrize('header_fill', [None, '', 'foo'])
def test_short_rows_headers_row_fill(header_fill):
    tbl = Txtble(
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
        '|Z_6  |1 |x |x^2|x^3|x^4|x^5|\n'
        '|S_3  |1 |a |b  |aba|ba |ab |\n'
        '|Z_4  |1 |x |x^2|x^3|#  |#  |\n'
        '|V_4  |1 |a |b  |ab |#  |#  |\n'
        '+-----+--+--+---+---+---+---+'
    )

def test_empty_headers_no_header_fill():
    tbl = Txtble(DATA, headers=[])
    with pytest.raises(ValueError):
        str(tbl)

def test_empty_headers_header_fill():
    tbl = Txtble(DATA, headers=[], header_fill='Filler')
    assert str(tbl) == (
        '+------+------+------+------+------+------+------+\n'
        '|Filler|Filler|Filler|Filler|Filler|Filler|Filler|\n'
        '+------+------+------+------+------+------+------+\n'
        '|1     |1     |      |      |      |      |      |\n'
        '|Z_6   |1     |x     |x^2   |x^3   |x^4   |x^5   |\n'
        '|S_3   |1     |a     |b     |aba   |ba    |ab    |\n'
        '|Z_4   |1     |x     |x^2   |x^3   |      |      |\n'
        '|V_4   |1     |a     |b     |ab    |      |      |\n'
        '+------+------+------+------+------+------+------+'
    )

def test_bad_row_fill():
    with pytest.raises(ValueError, match='row_fill cannot be None'):
        Txtble(DATA, row_fill=None)

def test_bad_row_fill_attr():
    tbl = Txtble(DATA)
    tbl.row_fill = None
    with pytest.raises(ValueError, match='row_fill cannot be None'):
        str(tbl)

# vim:set nowrap:
