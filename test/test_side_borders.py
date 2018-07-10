from txtble    import Txtble
from test_data import HEADERS, DATA

def test_vborders_off():
    tbl = Txtble(DATA, headers=HEADERS, left_border=False, right_border=False)
    assert str(tbl) == (
        '---------+----------+------------------\n'
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
        'December |Turquoise |Narcissus\n'
        '---------+----------+------------------'
    )

def test_hborders_on():
    tbl = Txtble(
        DATA,
        headers       = HEADERS,
        border        = False,
        top_border    = True,
        bottom_border = True,
    )
    assert str(tbl) == (
        '---------+----------+------------------\n'
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
        'December |Turquoise |Narcissus\n'
        '---------+----------+------------------'
    )

def test_hborders_off():
    tbl = Txtble(DATA, headers=HEADERS, top_border=False, bottom_border=False)
    assert str(tbl) == (
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
        '|December |Turquoise |Narcissus         |'
    )

def test_ulborder():
    tbl = Txtble(DATA, headers=HEADERS, bottom_border=False, right_border=False)
    assert str(tbl) == (
        '+---------+----------+------------------\n'
        '|Month    |Birthstone|Birth Flower\n'
        '+---------+----------+------------------\n'
        '|January  |Garnet    |Carnation\n'
        '|February |Amethyst  |Violet\n'
        '|March    |Aquamarine|Jonquil\n'
        '|April    |Diamond   |Sweetpea\n'
        '|May      |Emerald   |Lily Of The Valley\n'
        '|June     |Pearl     |Rose\n'
        '|July     |Ruby      |Larkspur\n'
        '|August   |Peridot   |Gladiolus\n'
        '|September|Sapphire  |Aster\n'
        '|October  |Opal      |Calendula\n'
        '|November |Topaz     |Chrysanthemum\n'
        '|December |Turquoise |Narcissus\n'
    )

def test_no_right_border():
    tbl = Txtble(DATA, headers=HEADERS, right_border=False)
    assert str(tbl) == (
        '+---------+----------+------------------\n'
        '|Month    |Birthstone|Birth Flower\n'
        '+---------+----------+------------------\n'
        '|January  |Garnet    |Carnation\n'
        '|February |Amethyst  |Violet\n'
        '|March    |Aquamarine|Jonquil\n'
        '|April    |Diamond   |Sweetpea\n'
        '|May      |Emerald   |Lily Of The Valley\n'
        '|June     |Pearl     |Rose\n'
        '|July     |Ruby      |Larkspur\n'
        '|August   |Peridot   |Gladiolus\n'
        '|September|Sapphire  |Aster\n'
        '|October  |Opal      |Calendula\n'
        '|November |Topaz     |Chrysanthemum\n'
        '|December |Turquoise |Narcissus\n'
        '+---------+----------+------------------'
    )

def test_no_right_border_no_rstrip():
    tbl = Txtble(DATA, headers=HEADERS, right_border=False, rstrip=False)
    assert str(tbl) == (
        '+---------+----------+------------------\n'
        '|Month    |Birthstone|Birth Flower      \n'
        '+---------+----------+------------------\n'
        '|January  |Garnet    |Carnation         \n'
        '|February |Amethyst  |Violet            \n'
        '|March    |Aquamarine|Jonquil           \n'
        '|April    |Diamond   |Sweetpea          \n'
        '|May      |Emerald   |Lily Of The Valley\n'
        '|June     |Pearl     |Rose              \n'
        '|July     |Ruby      |Larkspur          \n'
        '|August   |Peridot   |Gladiolus         \n'
        '|September|Sapphire  |Aster             \n'
        '|October  |Opal      |Calendula         \n'
        '|November |Topaz     |Chrysanthemum     \n'
        '|December |Turquoise |Narcissus         \n'
        '+---------+----------+------------------'
    )

def test_bottom_border_only():
    tbl = Txtble(DATA, headers=HEADERS, border=False, bottom_border=True)
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
        'December |Turquoise |Narcissus\n'
        '---------+----------+------------------'
    )
