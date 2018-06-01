from tabulator import Tabulator

def test_none():
    tbl = Tabulator(
        headers=('repr', 'value'),
        data=[
            ("''", ''),
            ('None', None),
            ("'None'", 'None'),
        ],
    )
    assert str(tbl) == (
        '+------+-----+\n'
        '|repr  |value|\n'
        '+------+-----+\n'
        "|''    |     |\n"
        "|None  |     |\n"
        "|'None'|None |\n"
        '+------+-----+'
    )

def test_none_str_empty():
    tbl = Tabulator(
        headers=('repr', 'value'),
        data=[
            ("''", ''),
            ('None', None),
            ("'None'", 'None'),
        ],
        none_str='None',
    )
    assert str(tbl) == (
        '+------+-----+\n'
        '|repr  |value|\n'
        '+------+-----+\n'
        "|''    |     |\n"
        "|None  |None |\n"
        "|'None'|None |\n"
        '+------+-----+'
    )
