from txtble    import Txtble, color_aware
from test_data import HEADERS, DATA, TABLE

def test_custom_len_func_old_not_called(mocker):
    strwidth = mocker.patch('txtble.strwidth')
    tbl = Txtble(DATA, headers=HEADERS, len_func=len)
    assert str(tbl) == TABLE
    assert not strwidth.called

def test_constant_len_func():
    tbl = Txtble(DATA, headers=HEADERS, len_func=lambda _: 5)
    assert str(tbl) == (
        '+-----+-----+-----+\n'
        '|Month|Birthstone|Birth Flower|\n'
        '+-----+-----+-----+\n'
        '|January|Garnet|Carnation|\n'
        '|February|Amethyst|Violet|\n'
        '|March|Aquamarine|Jonquil|\n'
        '|April|Diamond|Sweetpea|\n'
        '|May|Emerald|Lily Of The Valley|\n'
        '|June|Pearl|Rose|\n'
        '|July|Ruby|Larkspur|\n'
        '|August|Peridot|Gladiolus|\n'
        '|September|Sapphire|Aster|\n'
        '|October|Opal|Calendula|\n'
        '|November|Topaz|Chrysanthemum|\n'
        '|December|Turquoise|Narcissus|\n'
        '+-----+-----+-----+'
    )

def test_builtin_len_func_ansi():
    tbl = Txtble([['\033[31mRed\033[0m'], ['Red']], len_func=len)
    assert str(tbl) == (
        '+------------+\n'
        '|\033[31mRed\033[0m|\n'
        '|Red         |\n'
        '+------------+'
    )

def test_color_aware_len_func_ansi():
    tbl = Txtble([['\033[31mRed\033[0m'], ['Red']], len_func=color_aware(len))
    assert str(tbl) == (
        '+---+\n'
        '|\033[31mRed\033[0m|\n'
        '|Red|\n'
        '+---+'
    )
