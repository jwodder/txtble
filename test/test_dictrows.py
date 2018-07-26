from   collections import defaultdict
import pytest
from   txtble      import Txtble
from   test_data   import HEADERS, DATA, TABLE

def test_dict_rows():
    tbl = Txtble(
        data=[dict(zip(HEADERS, row)) for row in DATA],
        headers=HEADERS,
    )
    assert str(tbl) == TABLE

def test_dict_rows_append_each():
    tbl = Txtble(headers=HEADERS)
    for row in DATA:
        tbl.append(dict(zip(HEADERS, row)))
    assert str(tbl) == TABLE

def test_dict_rows_extend_all():
    tbl = Txtble(headers=HEADERS)
    tbl.extend(dict(zip(HEADERS, row)) for row in DATA)
    assert str(tbl) == TABLE

def test_dict_rows_no_headers():
    tbl = Txtble(data=[dict(zip(HEADERS, row)) for row in DATA])
    with pytest.raises(ValueError):
        str(tbl)

def test_missing_key():
    tbl = Txtble(
        headers = ['Red', 'Green', 'Blue'],
        data    = [{"Red": 42, "Green": 23}],
    )
    with pytest.raises(KeyError):
        str(tbl)

def test_missing_key_dict_fill_none():
    tbl = Txtble(
        headers   = ['Red', 'Green', 'Blue'],
        data      = [{"Red": 42, "Green": 23}],
        dict_fill = None,
    )
    assert str(tbl) == (
        '+---+-----+----+\n'
        '|Red|Green|Blue|\n'
        '+---+-----+----+\n'
        '|42 |23   |    |\n'
        '+---+-----+----+'
    )

def test_missing_key_dict_fill_str():
    tbl = Txtble(
        headers   = ['Red', 'Green', 'Blue'],
        data      = [{"Red": 42, "Green": 23}],
        dict_fill = 'Missing!',
    )
    assert str(tbl) == (
        '+---+-----+--------+\n'
        '|Red|Green|Blue    |\n'
        '+---+-----+--------+\n'
        '|42 |23   |Missing!|\n'
        '+---+-----+--------+'
    )

def test_missing_key_dict_fill_none_none_str():
    tbl = Txtble(
        headers   = ['Red', 'Green', 'Blue'],
        data      = [{"Red": 42, "Green": 23}],
        dict_fill = None,
        none_str  = 'Missing!',
    )
    assert str(tbl) == (
        '+---+-----+--------+\n'
        '|Red|Green|Blue    |\n'
        '+---+-----+--------+\n'
        '|42 |23   |Missing!|\n'
        '+---+-----+--------+'
    )

def test_dict_row_mixture():
    tbl = Txtble(
        headers = ['Red', 'Green', 'Blue'],
        data    = [
            {"Red": 42, "Green": 23, "Blue": 17},
            ["Ruby", "Emerald", "Sapphire"],
        ],
    )
    assert str(tbl) == (
        '+----+-------+--------+\n'
        '|Red |Green  |Blue    |\n'
        '+----+-------+--------+\n'
        '|42  |23     |17      |\n'
        '|Ruby|Emerald|Sapphire|\n'
        '+----+-------+--------+'
    )

def test_extra_dict_keys():
    tbl = Txtble(headers=['Red', 'Green'])
    tbl.append({"Red": 42, "Green": 23, "Blue": 17, "Yellow": 3.14})
    assert str(tbl) == (
        '+---+-----+\n'
        '|Red|Green|\n'
        '+---+-----+\n'
        '|42 |23   |\n'
        '+---+-----+'
    )

def test_change_dict_headers():
    tbl = Txtble(
        headers = ['Red', 'Green'],
        data    = [{"Red": 42, "Green": 23, "Blue": 17, "Yellow": 3.14}],
    )
    tbl.headers = ['Blue', 'Yellow']
    assert str(tbl) == (
        '+----+------+\n'
        '|Blue|Yellow|\n'
        '+----+------+\n'
        '|17  |3.14  |\n'
        '+----+------+'
    )

def test_set_dict_headers_late():
    tbl = Txtble([{"Red": 42, "Green": 23, "Blue": 17, "Yellow": 3.14}])
    tbl.headers = ['Blue', 'Yellow']
    assert str(tbl) == (
        '+----+------+\n'
        '|Blue|Yellow|\n'
        '+----+------+\n'
        '|17  |3.14  |\n'
        '+----+------+'
    )

def test_pairs_are_not_dict():
    tbl = Txtble(
        headers = ['Red', 'Green', 'Blue'],
        data    = [[('Red', 42), ('Green', 23), ('Blue', 17)]],
    )
    assert str(tbl) == (
        '+-----------+-------------+------------+\n'
        '|Red        |Green        |Blue        |\n'
        '+-----------+-------------+------------+\n'
        "|('Red', 42)|('Green', 23)|('Blue', 17)|\n"
        '+-----------+-------------+------------+'
    )

def test_defaultdict_row():
    tbl = Txtble(
        headers = ['Red', 'Green', 'Blue'],
        data    = [defaultdict(lambda: 'Missing!', {"Red": 42, "Green": 23})],
    )
    assert str(tbl) == (
        '+---+-----+--------+\n'
        '|Red|Green|Blue    |\n'
        '+---+-----+--------+\n'
        '|42 |23   |Missing!|\n'
        '+---+-----+--------+'
    )

def test_dict_row_mixture_extra_column():
    tbl = Txtble(
        headers = ['Red', 'Green', 'Blue'],
        data    = [
            ["Ruby", "Emerald", "Sapphire", "Topaz"],
            {"Red": 42, "Green": 23, "Blue": 17, "Filler": 3.14},
        ],
        header_fill = 'Filler',
        row_fill    = 'row_fill',
    )
    assert str(tbl) == (
        '+----+-------+--------+--------+\n'
        '|Red |Green  |Blue    |Filler  |\n'
        '+----+-------+--------+--------+\n'
        '|Ruby|Emerald|Sapphire|Topaz   |\n'
        '|42  |23     |17      |row_fill|\n'
        '+----+-------+--------+--------+'
    )

def test_dict_row_repeated_header_key():
    tbl = Txtble(
        headers = ['Red', 'Green', 'Blue', 'Green'],
        data    = [{"Red": 42, "Green": 23, "Blue": 17}],
    )
    assert str(tbl) == (
        '+---+-----+----+-----+\n'
        '|Red|Green|Blue|Green|\n'
        '+---+-----+----+-----+\n'
        '|42 |23   |17  |23   |\n'
        '+---+-----+----+-----+'
    )
