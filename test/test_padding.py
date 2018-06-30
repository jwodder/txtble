import pytest
from   txtble    import Txtble
from   test_data import HEADERS, DATA, TABLE

@pytest.mark.parametrize('padding', ['', 0, None, False])
def test_no_padding(padding):
    tbl = Txtble(DATA, headers=HEADERS, padding=padding)
    assert str(tbl) == TABLE

@pytest.mark.parametrize('padding', [' ', 1])
def test_one_padding(padding):
    tbl = Txtble(DATA, headers=HEADERS, padding=padding)
    assert str(tbl) == (
        '+-----------+------------+--------------------+\n'
        '| Month     | Birthstone | Birth Flower       |\n'
        '+-----------+------------+--------------------+\n'
        '| January   | Garnet     | Carnation          |\n'
        '| February  | Amethyst   | Violet             |\n'
        '| March     | Aquamarine | Jonquil            |\n'
        '| April     | Diamond    | Sweetpea           |\n'
        '| May       | Emerald    | Lily Of The Valley |\n'
        '| June      | Pearl      | Rose               |\n'
        '| July      | Ruby       | Larkspur           |\n'
        '| August    | Peridot    | Gladiolus          |\n'
        '| September | Sapphire   | Aster              |\n'
        '| October   | Opal       | Calendula          |\n'
        '| November  | Topaz      | Chrysanthemum      |\n'
        '| December  | Turquoise  | Narcissus          |\n'
        '+-----------+------------+--------------------+'
    )

@pytest.mark.parametrize('padding', ['  ', 2])
def test_two_padding(padding):
    tbl = Txtble(DATA, headers=HEADERS, padding=padding)
    assert str(tbl) == (
        '+-------------+--------------+----------------------+\n'
        '|  Month      |  Birthstone  |  Birth Flower        |\n'
        '+-------------+--------------+----------------------+\n'
        '|  January    |  Garnet      |  Carnation           |\n'
        '|  February   |  Amethyst    |  Violet              |\n'
        '|  March      |  Aquamarine  |  Jonquil             |\n'
        '|  April      |  Diamond     |  Sweetpea            |\n'
        '|  May        |  Emerald     |  Lily Of The Valley  |\n'
        '|  June       |  Pearl       |  Rose                |\n'
        '|  July       |  Ruby        |  Larkspur            |\n'
        '|  August     |  Peridot     |  Gladiolus           |\n'
        '|  September  |  Sapphire    |  Aster               |\n'
        '|  October    |  Opal        |  Calendula           |\n'
        '|  November   |  Topaz       |  Chrysanthemum       |\n'
        '|  December   |  Turquoise   |  Narcissus           |\n'
        '+-------------+--------------+----------------------+'
    )

def test_tab_padding():
    tbl = Txtble(DATA, headers=HEADERS, padding='\t')
    assert str(tbl) == (
        '+-------------------------+--------------------------+----------------------------------+\n'
        '|        Month            |        Birthstone        |        Birth Flower              |\n'
        '+-------------------------+--------------------------+----------------------------------+\n'
        '|        January          |        Garnet            |        Carnation                 |\n'
        '|        February         |        Amethyst          |        Violet                    |\n'
        '|        March            |        Aquamarine        |        Jonquil                   |\n'
        '|        April            |        Diamond           |        Sweetpea                  |\n'
        '|        May              |        Emerald           |        Lily Of The Valley        |\n'
        '|        June             |        Pearl             |        Rose                      |\n'
        '|        July             |        Ruby              |        Larkspur                  |\n'
        '|        August           |        Peridot           |        Gladiolus                 |\n'
        '|        September        |        Sapphire          |        Aster                     |\n'
        '|        October          |        Opal              |        Calendula                 |\n'
        '|        November         |        Topaz             |        Chrysanthemum             |\n'
        '|        December         |        Turquoise         |        Narcissus                 |\n'
        '+-------------------------+--------------------------+----------------------------------+'
    )

def test_non_space_padding():
    tbl = Txtble(DATA, headers=HEADERS, padding='x')
    assert str(tbl) == (
        '+-----------+------------+--------------------+\n'
        '|xMonth    x|xBirthstonex|xBirth Flower      x|\n'
        '+-----------+------------+--------------------+\n'
        '|xJanuary  x|xGarnet    x|xCarnation         x|\n'
        '|xFebruary x|xAmethyst  x|xViolet            x|\n'
        '|xMarch    x|xAquamarinex|xJonquil           x|\n'
        '|xApril    x|xDiamond   x|xSweetpea          x|\n'
        '|xMay      x|xEmerald   x|xLily Of The Valleyx|\n'
        '|xJune     x|xPearl     x|xRose              x|\n'
        '|xJuly     x|xRuby      x|xLarkspur          x|\n'
        '|xAugust   x|xPeridot   x|xGladiolus         x|\n'
        '|xSeptemberx|xSapphire  x|xAster             x|\n'
        '|xOctober  x|xOpal      x|xCalendula         x|\n'
        '|xNovember x|xTopaz     x|xChrysanthemum     x|\n'
        '|xDecember x|xTurquoise x|xNarcissus         x|\n'
        '+-----------+------------+--------------------+'
    )

def test_mixed_padding():
    tbl = Txtble(DATA, headers=HEADERS, padding=' x ')
    assert str(tbl) == (
        '+---------------+----------------+------------------------+\n'
        '| x Month     x | x Birthstone x | x Birth Flower       x |\n'
        '+---------------+----------------+------------------------+\n'
        '| x January   x | x Garnet     x | x Carnation          x |\n'
        '| x February  x | x Amethyst   x | x Violet             x |\n'
        '| x March     x | x Aquamarine x | x Jonquil            x |\n'
        '| x April     x | x Diamond    x | x Sweetpea           x |\n'
        '| x May       x | x Emerald    x | x Lily Of The Valley x |\n'
        '| x June      x | x Pearl      x | x Rose               x |\n'
        '| x July      x | x Ruby       x | x Larkspur           x |\n'
        '| x August    x | x Peridot    x | x Gladiolus          x |\n'
        '| x September x | x Sapphire   x | x Aster              x |\n'
        '| x October   x | x Opal       x | x Calendula          x |\n'
        '| x November  x | x Topaz      x | x Chrysanthemum      x |\n'
        '| x December  x | x Turquoise  x | x Narcissus          x |\n'
        '+---------------+----------------+------------------------+'
    )

def test_padding_no_border():
    tbl = Txtble(DATA, headers=HEADERS, padding=1, border=False)
    assert str(tbl) == (
        ' Month     | Birthstone | Birth Flower\n'
        '-----------+------------+--------------------\n'
        ' January   | Garnet     | Carnation\n'
        ' February  | Amethyst   | Violet\n'
        ' March     | Aquamarine | Jonquil\n'
        ' April     | Diamond    | Sweetpea\n'
        ' May       | Emerald    | Lily Of The Valley\n'
        ' June      | Pearl      | Rose\n'
        ' July      | Ruby       | Larkspur\n'
        ' August    | Peridot    | Gladiolus\n'
        ' September | Sapphire   | Aster\n'
        ' October   | Opal       | Calendula\n'
        ' November  | Topaz      | Chrysanthemum\n'
        ' December  | Turquoise  | Narcissus'
    )

def test_left_padding_right_padding_no_border():
    tbl = Txtble(DATA, headers=HEADERS, left_padding='x', right_padding='y',
                 border=False)
    assert str(tbl) == (
        'xMonth    y|xBirthstoney|xBirth Flower\n'
        '-----------+------------+--------------------\n'
        'xJanuary  y|xGarnet    y|xCarnation\n'
        'xFebruary y|xAmethyst  y|xViolet\n'
        'xMarch    y|xAquamariney|xJonquil\n'
        'xApril    y|xDiamond   y|xSweetpea\n'
        'xMay      y|xEmerald   y|xLily Of The Valley\n'
        'xJune     y|xPearl     y|xRose\n'
        'xJuly     y|xRuby      y|xLarkspur\n'
        'xAugust   y|xPeridot   y|xGladiolus\n'
        'xSeptembery|xSapphire  y|xAster\n'
        'xOctober  y|xOpal      y|xCalendula\n'
        'xNovember y|xTopaz     y|xChrysanthemum\n'
        'xDecember y|xTurquoise y|xNarcissus'
    )

def test_padding_no_border_no_rstrip():
    tbl = Txtble(DATA, headers=HEADERS, padding=1, border=False, rstrip=False)
    assert str(tbl) == (
        ' Month     | Birthstone | Birth Flower       \n'
        '-----------+------------+--------------------\n'
        ' January   | Garnet     | Carnation          \n'
        ' February  | Amethyst   | Violet             \n'
        ' March     | Aquamarine | Jonquil            \n'
        ' April     | Diamond    | Sweetpea           \n'
        ' May       | Emerald    | Lily Of The Valley \n'
        ' June      | Pearl      | Rose               \n'
        ' July      | Ruby       | Larkspur           \n'
        ' August    | Peridot    | Gladiolus          \n'
        ' September | Sapphire   | Aster              \n'
        ' October   | Opal       | Calendula          \n'
        ' November  | Topaz      | Chrysanthemum      \n'
        ' December  | Turquoise  | Narcissus          '
    )

def test_left_padding_right_padding_no_border_no_rstrip():
    tbl = Txtble(DATA, headers=HEADERS, left_padding='x', right_padding='y',
                 border=False, rstrip=False)
    assert str(tbl) == (
        'xMonth    y|xBirthstoney|xBirth Flower      y\n'
        '-----------+------------+--------------------\n'
        'xJanuary  y|xGarnet    y|xCarnation         y\n'
        'xFebruary y|xAmethyst  y|xViolet            y\n'
        'xMarch    y|xAquamariney|xJonquil           y\n'
        'xApril    y|xDiamond   y|xSweetpea          y\n'
        'xMay      y|xEmerald   y|xLily Of The Valleyy\n'
        'xJune     y|xPearl     y|xRose              y\n'
        'xJuly     y|xRuby      y|xLarkspur          y\n'
        'xAugust   y|xPeridot   y|xGladiolus         y\n'
        'xSeptembery|xSapphire  y|xAster             y\n'
        'xOctober  y|xOpal      y|xCalendula         y\n'
        'xNovember y|xTopaz     y|xChrysanthemum     y\n'
        'xDecember y|xTurquoise y|xNarcissus         y'
    )

@pytest.mark.parametrize('padding', [
    'x\ny', 'x\ry', 'x\fy', 'x\vy', u'x\x85y', u'x\u2028y', u'x\u2029y',
])
def test_multiline_padding(padding):
    tbl = Txtble(DATA, headers=HEADERS, padding=padding)
    with pytest.raises(ValueError):
        tbl.show()

def test_padding_no_column_border():
    tbl = Txtble(DATA, headers=HEADERS, padding=1, column_border=False)
    assert str(tbl) == (
        '+-------------------------------------------+\n'
        '| Month      Birthstone  Birth Flower       |\n'
        '+-------------------------------------------+\n'
        '| January    Garnet      Carnation          |\n'
        '| February   Amethyst    Violet             |\n'
        '| March      Aquamarine  Jonquil            |\n'
        '| April      Diamond     Sweetpea           |\n'
        '| May        Emerald     Lily Of The Valley |\n'
        '| June       Pearl       Rose               |\n'
        '| July       Ruby        Larkspur           |\n'
        '| August     Peridot     Gladiolus          |\n'
        '| September  Sapphire    Aster              |\n'
        '| October    Opal        Calendula          |\n'
        '| November   Topaz       Chrysanthemum      |\n'
        '| December   Turquoise   Narcissus          |\n'
        '+-------------------------------------------+'
    )

def test_left_padding_right_padding():
    tbl = Txtble(DATA, headers=HEADERS, left_padding=' ', right_padding='x')
    assert str(tbl) == (
        '+-----------+------------+--------------------+\n'
        '| Month    x| Birthstonex| Birth Flower      x|\n'
        '+-----------+------------+--------------------+\n'
        '| January  x| Garnet    x| Carnation         x|\n'
        '| February x| Amethyst  x| Violet            x|\n'
        '| March    x| Aquamarinex| Jonquil           x|\n'
        '| April    x| Diamond   x| Sweetpea          x|\n'
        '| May      x| Emerald   x| Lily Of The Valleyx|\n'
        '| June     x| Pearl     x| Rose              x|\n'
        '| July     x| Ruby      x| Larkspur          x|\n'
        '| August   x| Peridot   x| Gladiolus         x|\n'
        '| Septemberx| Sapphire  x| Aster             x|\n'
        '| October  x| Opal      x| Calendula         x|\n'
        '| November x| Topaz     x| Chrysanthemum     x|\n'
        '| December x| Turquoise x| Narcissus         x|\n'
        '+-----------+------------+--------------------+'
    )

def test_padding_left_padding_right_padding():
    tbl = Txtble(DATA, headers=HEADERS, left_padding=' ', right_padding='x',
                 padding='anything')
    assert str(tbl) == (
        '+-----------+------------+--------------------+\n'
        '| Month    x| Birthstonex| Birth Flower      x|\n'
        '+-----------+------------+--------------------+\n'
        '| January  x| Garnet    x| Carnation         x|\n'
        '| February x| Amethyst  x| Violet            x|\n'
        '| March    x| Aquamarinex| Jonquil           x|\n'
        '| April    x| Diamond   x| Sweetpea          x|\n'
        '| May      x| Emerald   x| Lily Of The Valleyx|\n'
        '| June     x| Pearl     x| Rose              x|\n'
        '| July     x| Ruby      x| Larkspur          x|\n'
        '| August   x| Peridot   x| Gladiolus         x|\n'
        '| Septemberx| Sapphire  x| Aster             x|\n'
        '| October  x| Opal      x| Calendula         x|\n'
        '| November x| Topaz     x| Chrysanthemum     x|\n'
        '| December x| Turquoise x| Narcissus         x|\n'
        '+-----------+------------+--------------------+'
    )

def test_padding_left_padding():
    tbl = Txtble(DATA, headers=HEADERS, left_padding=' ', padding='x')
    assert str(tbl) == (
        '+-----------+------------+--------------------+\n'
        '| Month    x| Birthstonex| Birth Flower      x|\n'
        '+-----------+------------+--------------------+\n'
        '| January  x| Garnet    x| Carnation         x|\n'
        '| February x| Amethyst  x| Violet            x|\n'
        '| March    x| Aquamarinex| Jonquil           x|\n'
        '| April    x| Diamond   x| Sweetpea          x|\n'
        '| May      x| Emerald   x| Lily Of The Valleyx|\n'
        '| June     x| Pearl     x| Rose              x|\n'
        '| July     x| Ruby      x| Larkspur          x|\n'
        '| August   x| Peridot   x| Gladiolus         x|\n'
        '| Septemberx| Sapphire  x| Aster             x|\n'
        '| October  x| Opal      x| Calendula         x|\n'
        '| November x| Topaz     x| Chrysanthemum     x|\n'
        '| December x| Turquoise x| Narcissus         x|\n'
        '+-----------+------------+--------------------+'
    )

def test_padding_right_padding():
    tbl = Txtble(DATA, headers=HEADERS, right_padding='x', padding=' ')
    assert str(tbl) == (
        '+-----------+------------+--------------------+\n'
        '| Month    x| Birthstonex| Birth Flower      x|\n'
        '+-----------+------------+--------------------+\n'
        '| January  x| Garnet    x| Carnation         x|\n'
        '| February x| Amethyst  x| Violet            x|\n'
        '| March    x| Aquamarinex| Jonquil           x|\n'
        '| April    x| Diamond   x| Sweetpea          x|\n'
        '| May      x| Emerald   x| Lily Of The Valleyx|\n'
        '| June     x| Pearl     x| Rose              x|\n'
        '| July     x| Ruby      x| Larkspur          x|\n'
        '| August   x| Peridot   x| Gladiolus         x|\n'
        '| Septemberx| Sapphire  x| Aster             x|\n'
        '| October  x| Opal      x| Calendula         x|\n'
        '| November x| Topaz     x| Chrysanthemum     x|\n'
        '| December x| Turquoise x| Narcissus         x|\n'
        '+-----------+------------+--------------------+'
    )

@pytest.mark.parametrize('padding', [' ', 1])
def test_left_padding(padding):
    tbl = Txtble(DATA, headers=HEADERS, left_padding=padding)
    assert str(tbl) == (
        '+----------+-----------+-------------------+\n'
        '| Month    | Birthstone| Birth Flower      |\n'
        '+----------+-----------+-------------------+\n'
        '| January  | Garnet    | Carnation         |\n'
        '| February | Amethyst  | Violet            |\n'
        '| March    | Aquamarine| Jonquil           |\n'
        '| April    | Diamond   | Sweetpea          |\n'
        '| May      | Emerald   | Lily Of The Valley|\n'
        '| June     | Pearl     | Rose              |\n'
        '| July     | Ruby      | Larkspur          |\n'
        '| August   | Peridot   | Gladiolus         |\n'
        '| September| Sapphire  | Aster             |\n'
        '| October  | Opal      | Calendula         |\n'
        '| November | Topaz     | Chrysanthemum     |\n'
        '| December | Turquoise | Narcissus         |\n'
        '+----------+-----------+-------------------+'
    )

@pytest.mark.parametrize('padding', [' ', 1])
def test_right_padding(padding):
    tbl = Txtble(DATA, headers=HEADERS, right_padding=padding)
    assert str(tbl) == (
        '+----------+-----------+-------------------+\n'
        '|Month     |Birthstone |Birth Flower       |\n'
        '+----------+-----------+-------------------+\n'
        '|January   |Garnet     |Carnation          |\n'
        '|February  |Amethyst   |Violet             |\n'
        '|March     |Aquamarine |Jonquil            |\n'
        '|April     |Diamond    |Sweetpea           |\n'
        '|May       |Emerald    |Lily Of The Valley |\n'
        '|June      |Pearl      |Rose               |\n'
        '|July      |Ruby       |Larkspur           |\n'
        '|August    |Peridot    |Gladiolus          |\n'
        '|September |Sapphire   |Aster              |\n'
        '|October   |Opal       |Calendula          |\n'
        '|November  |Topaz      |Chrysanthemum      |\n'
        '|December  |Turquoise  |Narcissus          |\n'
        '+----------+-----------+-------------------+'
    )

# vim:set nowrap:
