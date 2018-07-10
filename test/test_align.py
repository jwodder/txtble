import pytest
from   txtble    import Txtble
from   test_data import HEADERS, DATA, TABLE

def test_align_lll():
    tbl = Txtble(DATA, headers=HEADERS, align=['l', 'l', 'l'])
    assert str(tbl) == TABLE

def test_align_ccc():
    tbl = Txtble(DATA, headers=HEADERS, align=['c', 'c', 'c'])
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|  Month  |Birthstone|   Birth Flower   |\n'
        '+---------+----------+------------------+\n'
        '| January |  Garnet  |    Carnation     |\n'
        '|February | Amethyst |      Violet      |\n'
        '|  March  |Aquamarine|     Jonquil      |\n'
        '|  April  | Diamond  |     Sweetpea     |\n'
        '|   May   | Emerald  |Lily Of The Valley|\n'
        '|  June   |  Pearl   |       Rose       |\n'
        '|  July   |   Ruby   |     Larkspur     |\n'
        '| August  | Peridot  |    Gladiolus     |\n'
        '|September| Sapphire |      Aster       |\n'
        '| October |   Opal   |    Calendula     |\n'
        '|November |  Topaz   |  Chrysanthemum   |\n'
        '|December |Turquoise |    Narcissus     |\n'
        '+---------+----------+------------------+'
    )

def test_align_rrr():
    tbl = Txtble(DATA, headers=HEADERS, align=['r', 'r', 'r'])
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|    Month|Birthstone|      Birth Flower|\n'
        '+---------+----------+------------------+\n'
        '|  January|    Garnet|         Carnation|\n'
        '| February|  Amethyst|            Violet|\n'
        '|    March|Aquamarine|           Jonquil|\n'
        '|    April|   Diamond|          Sweetpea|\n'
        '|      May|   Emerald|Lily Of The Valley|\n'
        '|     June|     Pearl|              Rose|\n'
        '|     July|      Ruby|          Larkspur|\n'
        '|   August|   Peridot|         Gladiolus|\n'
        '|September|  Sapphire|             Aster|\n'
        '|  October|      Opal|         Calendula|\n'
        '| November|     Topaz|     Chrysanthemum|\n'
        '| December| Turquoise|         Narcissus|\n'
        '+---------+----------+------------------+'
    )

def test_align_rcl():
    tbl = Txtble(DATA, headers=HEADERS, align=['r', 'c', 'l'])
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|    Month|Birthstone|Birth Flower      |\n'
        '+---------+----------+------------------+\n'
        '|  January|  Garnet  |Carnation         |\n'
        '| February| Amethyst |Violet            |\n'
        '|    March|Aquamarine|Jonquil           |\n'
        '|    April| Diamond  |Sweetpea          |\n'
        '|      May| Emerald  |Lily Of The Valley|\n'
        '|     June|  Pearl   |Rose              |\n'
        '|     July|   Ruby   |Larkspur          |\n'
        '|   August| Peridot  |Gladiolus         |\n'
        '|September| Sapphire |Aster             |\n'
        '|  October|   Opal   |Calendula         |\n'
        '| November|  Topaz   |Chrysanthemum     |\n'
        '| December|Turquoise |Narcissus         |\n'
        '+---------+----------+------------------+'
    )

def test_align_ccc_right_padding():
    tbl = Txtble(DATA, headers=HEADERS, align=['c', 'c', 'c'], right_padding=2)
    assert str(tbl) == (
        '+-----------+------------+--------------------+\n'
        '|  Month    |Birthstone  |   Birth Flower     |\n'
        '+-----------+------------+--------------------+\n'
        '| January   |  Garnet    |    Carnation       |\n'
        '|February   | Amethyst   |      Violet        |\n'
        '|  March    |Aquamarine  |     Jonquil        |\n'
        '|  April    | Diamond    |     Sweetpea       |\n'
        '|   May     | Emerald    |Lily Of The Valley  |\n'
        '|  June     |  Pearl     |       Rose         |\n'
        '|  July     |   Ruby     |     Larkspur       |\n'
        '| August    | Peridot    |    Gladiolus       |\n'
        '|September  | Sapphire   |      Aster         |\n'
        '| October   |   Opal     |    Calendula       |\n'
        '|November   |  Topaz     |  Chrysanthemum     |\n'
        '|December   |Turquoise   |    Narcissus       |\n'
        '+-----------+------------+--------------------+'
    )

def test_align_extra_columns():
    tbl = Txtble(DATA, headers=HEADERS, align=['c', 'c'])
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|  Month  |Birthstone|Birth Flower      |\n'
        '+---------+----------+------------------+\n'
        '| January |  Garnet  |Carnation         |\n'
        '|February | Amethyst |Violet            |\n'
        '|  March  |Aquamarine|Jonquil           |\n'
        '|  April  | Diamond  |Sweetpea          |\n'
        '|   May   | Emerald  |Lily Of The Valley|\n'
        '|  June   |  Pearl   |Rose              |\n'
        '|  July   |   Ruby   |Larkspur          |\n'
        '| August  | Peridot  |Gladiolus         |\n'
        '|September| Sapphire |Aster             |\n'
        '| October |   Opal   |Calendula         |\n'
        '|November |  Topaz   |Chrysanthemum     |\n'
        '|December |Turquoise |Narcissus         |\n'
        '+---------+----------+------------------+'
    )

def test_align_extra_columns_align_fill():
    tbl = Txtble(DATA, headers=HEADERS, align=['c', 'c'], align_fill='r')
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|  Month  |Birthstone|      Birth Flower|\n'
        '+---------+----------+------------------+\n'
        '| January |  Garnet  |         Carnation|\n'
        '|February | Amethyst |            Violet|\n'
        '|  March  |Aquamarine|           Jonquil|\n'
        '|  April  | Diamond  |          Sweetpea|\n'
        '|   May   | Emerald  |Lily Of The Valley|\n'
        '|  June   |  Pearl   |              Rose|\n'
        '|  July   |   Ruby   |          Larkspur|\n'
        '| August  | Peridot  |         Gladiolus|\n'
        '|September| Sapphire |             Aster|\n'
        '| October |   Opal   |         Calendula|\n'
        '|November |  Topaz   |     Chrysanthemum|\n'
        '|December |Turquoise |         Narcissus|\n'
        '+---------+----------+------------------+'
    )

def test_align_extra_aligns():
    tbl = Txtble(DATA, headers=HEADERS, align=['r', 'c', 'l', 'c', 'r'])
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|    Month|Birthstone|Birth Flower      |\n'
        '+---------+----------+------------------+\n'
        '|  January|  Garnet  |Carnation         |\n'
        '| February| Amethyst |Violet            |\n'
        '|    March|Aquamarine|Jonquil           |\n'
        '|    April| Diamond  |Sweetpea          |\n'
        '|      May| Emerald  |Lily Of The Valley|\n'
        '|     June|  Pearl   |Rose              |\n'
        '|     July|   Ruby   |Larkspur          |\n'
        '|   August| Peridot  |Gladiolus         |\n'
        '|September| Sapphire |Aster             |\n'
        '|  October|   Opal   |Calendula         |\n'
        '| November|  Topaz   |Chrysanthemum     |\n'
        '| December|Turquoise |Narcissus         |\n'
        '+---------+----------+------------------+'
    )

@pytest.mark.parametrize('align', ['q', 'L', 'left', None, '<'])
def test_bad_align(align):
    tbl = Txtble(DATA, headers=HEADERS, align=['r', 'c', align])
    with pytest.raises(ValueError):
        str(tbl)

@pytest.mark.parametrize('align_fill', [None, 'l'])
def test_align_all_c(align_fill):
    tbl = Txtble(DATA, headers=HEADERS, align='c', align_fill=align_fill)
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|  Month  |Birthstone|   Birth Flower   |\n'
        '+---------+----------+------------------+\n'
        '| January |  Garnet  |    Carnation     |\n'
        '|February | Amethyst |      Violet      |\n'
        '|  March  |Aquamarine|     Jonquil      |\n'
        '|  April  | Diamond  |     Sweetpea     |\n'
        '|   May   | Emerald  |Lily Of The Valley|\n'
        '|  June   |  Pearl   |       Rose       |\n'
        '|  July   |   Ruby   |     Larkspur     |\n'
        '| August  | Peridot  |    Gladiolus     |\n'
        '|September| Sapphire |      Aster       |\n'
        '| October |   Opal   |    Calendula     |\n'
        '|November |  Topaz   |  Chrysanthemum   |\n'
        '|December |Turquoise |    Narcissus     |\n'
        '+---------+----------+------------------+'
    )

def test_align_fill_c():
    tbl = Txtble(DATA, headers=HEADERS, align_fill='c')
    assert str(tbl) == (
        '+---------+----------+------------------+\n'
        '|  Month  |Birthstone|   Birth Flower   |\n'
        '+---------+----------+------------------+\n'
        '| January |  Garnet  |    Carnation     |\n'
        '|February | Amethyst |      Violet      |\n'
        '|  March  |Aquamarine|     Jonquil      |\n'
        '|  April  | Diamond  |     Sweetpea     |\n'
        '|   May   | Emerald  |Lily Of The Valley|\n'
        '|  June   |  Pearl   |       Rose       |\n'
        '|  July   |   Ruby   |     Larkspur     |\n'
        '| August  | Peridot  |    Gladiolus     |\n'
        '|September| Sapphire |      Aster       |\n'
        '| October |   Opal   |    Calendula     |\n'
        '|November |  Topaz   |  Chrysanthemum   |\n'
        '|December |Turquoise |    Narcissus     |\n'
        '+---------+----------+------------------+'
    )
