# -*- coding: utf-8 -*-
import pytest
from   six         import text_type
from   wcwidth     import wcswidth
from   txtble      import Txtble, UnterminatedColorError
from   txtble.util import strwidth
from   test_data   import HEADERS, DATA

COLORED_STRINGS = [
    ('\033[31mRed\033[0m', 'Red'),
    ('\033[31mRed\033[m', 'Red'),
    ('\033[3;1mIndeterminate\033[0m', 'Indeterminate'),
    ('\033[3;;1mIndeterminate\033[0m', 'Indeterminate'),
    ('\033[31mRed\033[0m and \033[32mGreen\033[0m', 'Red and Green'),
    ('An \033[4munderlined\033[m word', 'An underlined word'),
    ('Misplaced \033[0m sgr0', 'Misplaced  sgr0'),
    ('\033[32mGr\033[34mue\033[m', 'Grue'),
    ('\033[41mExtra\033[00m \033[05mzeroes\033[000m', 'Extra zeroes'),
    (u'\033[30;47mPoke\u0301mon\033[m', u'Poke\u0301mon'),
    (u'\033[37;40mＴｅｓｔ\u3000ｔｅｘｔ\033[m', u'Ｔｅｓｔ\u3000ｔｅｘｔ'),
]

@pytest.mark.parametrize('colored,plain', COLORED_STRINGS)
def test_color_aware_len(colored, plain):
    assert strwidth(colored) == wcswidth(plain)

def test_bad_color_aware_len():
    s = '\033[1mNo terminating sgr0'
    with pytest.raises(UnterminatedColorError) as excinfo:
        strwidth(s)
    assert excinfo.value.string == s
    assert str(excinfo.value) == repr(s) + ': ANSI color sequence not reset'

@pytest.mark.parametrize('colored,plain', COLORED_STRINGS)
def test_colored_text(colored, plain):
    tbl = Txtble(data=[[colored], [plain]])
    w = wcswidth(plain)
    assert text_type(tbl) == (
          '+' + '-' * w + '+\n'
        + '|' + colored + '|\n'
        + '|' + plain   + '|\n'
        + '+' + '-' * w + '+'
    )

def test_multiline_colors():
    tbl = Txtble([
        [
            'The \033[4mFlower\033[m Poem\n'
            'All of the \033[31mred\n'
            'flowers\033[m are very \033[01;32mbold\n'
            'green\033[0m, and the petals are \033[34mblue\033[46m\n'
            'on cyan\033[00m.  The \033[36mC\033[35mM\033[33mY\033[30mK\n'
            'of it all\033[m just \033[40;34;46;0;7mboggles\n'
            'the mind\033[0m.'
        ]
    ])
    assert str(tbl) == (
        '+------------------------------+\n'
        '|The \033[4mFlower\033[m Poem               |\n'
        '|All of the \033[31mred\033[m                |\n'
        '|\033[31mflowers\033[m are very \033[01;32mbold\033[m         |\n'
        '|\033[01;32mgreen\033[0m, and the petals are \033[34mblue\033[46m\033[m|\n'
        '|\033[34m\033[46mon cyan\033[00m.  The \033[36mC\033[35mM\033[33mY\033[30mK\033[m            |\n'
        '|\033[36m\033[35m\033[33m\033[30mof it all\033[m just \033[40;34;46;0;7mboggles\033[m        |\n'
        '|\033[40;34;46;0;7mthe mind\033[0m.                     |\n'
        '+------------------------------+'
    )

def test_multiline_long_colors():
    tbl = Txtble([
        [
            '\033[1mThe Flower Poem\n'
            'All of the red\n'
            'flowers are \033[4mvery bold\n'
            'green, and\033[m the petals are \033[7mblue\n'
            'on cyan.  The CMYK\n'
            'of it all just boggles\n'
            'the mind.\033[m'
        ]
    ])
    assert str(tbl) == (
        '+------------------------------+\n'
        '|\033[1mThe Flower Poem\033[m               |\n'
        '|\033[1mAll of the red\033[m                |\n'
        '|\033[1mflowers are \033[4mvery bold\033[m         |\n'
        '|\033[1m\033[4mgreen, and\033[m the petals are \033[7mblue\033[m|\n'
        '|\033[7mon cyan.  The CMYK\033[m            |\n'
        '|\033[7mof it all just boggles\033[m        |\n'
        '|\033[7mthe mind.\033[m                     |\n'
        '+------------------------------+'
    )

def test_color_none_str():
    tbl = Txtble(
        headers=('repr', 'value'),
        data=[
            ("''", ''),
            ('None', None),
            ("'None'", 'None'),
        ],
        none_str='\033[31mRed\ntext\033[0m',
    )
    assert str(tbl) == (
        '+------+-----+\n'
        '|repr  |value|\n'
        '+------+-----+\n'
        "|''    |     |\n"
        "|None  |\033[31mRed\033[m  |\n"
        "|      |\033[31mtext\033[0m |\n"
        "|'None'|None |\n"
        '+------+-----+'
    )

def test_color_row_fill():
    tbl = Txtble(
        [
            ['1', '1'],
            ['Z_6', '1', 'x', 'x^2', 'x^3', 'x^4', 'x^5'],
            ['S_3', '1', 'a', 'b', 'aba', 'ba', 'ab'],
            ['Z_4', '1', 'x', 'x^2', 'x^3'],
            ['V_4', '1', 'a', 'b', 'ab'],
        ],
        row_fill='\033[31mRed\ntext\033[0m',
    )
    assert str(tbl) == (
        '+---+-+----+----+----+----+----+\n'
        '|1  |1|\033[31mRed\033[m |\033[31mRed\033[m |\033[31mRed\033[m |\033[31mRed\033[m |\033[31mRed\033[m |\n'
        '|   | |\033[31mtext\033[0m|\033[31mtext\033[0m|\033[31mtext\033[0m|\033[31mtext\033[0m|\033[31mtext\033[0m|\n'
        '|Z_6|1|x   |x^2 |x^3 |x^4 |x^5 |\n'
        '|S_3|1|a   |b   |aba |ba  |ab  |\n'
        '|Z_4|1|x   |x^2 |x^3 |\033[31mRed\033[m |\033[31mRed\033[m |\n'
        '|   | |    |    |    |\033[31mtext\033[0m|\033[31mtext\033[0m|\n'
        '|V_4|1|a   |b   |ab  |\033[31mRed\033[m |\033[31mRed\033[m |\n'
        '|   | |    |    |    |\033[31mtext\033[0m|\033[31mtext\033[0m|\n'
        '+---+-+----+----+----+----+----+'
    )

def test_color_header_fill():
    tbl = Txtble(
        [
            ['1', '1'],
            ['Z_6', '1', 'x', 'x^2', 'x^3', 'x^4', 'x^5'],
            ['S_3', '1', 'a', 'b', 'aba', 'ba', 'ab'],
            ['Z_4', '1', 'x', 'x^2', 'x^3'],
            ['V_4', '1', 'a', 'b', 'ab'],
        ],
        header_fill = '\033[31mRed\ntext\033[0m',
        headers     = ('Group', 'Elements'),
    )
    assert str(tbl) == (
        '+-----+--------+----+----+----+----+----+\n'
        '|Group|Elements|\033[31mRed\033[m |\033[31mRed\033[m |\033[31mRed\033[m |\033[31mRed\033[m |\033[31mRed\033[m |\n'
        '|     |        |\033[31mtext\033[0m|\033[31mtext\033[0m|\033[31mtext\033[0m|\033[31mtext\033[0m|\033[31mtext\033[0m|\n'
        '+-----+--------+----+----+----+----+----+\n'
        '|1    |1       |    |    |    |    |    |\n'
        '|Z_6  |1       |x   |x^2 |x^3 |x^4 |x^5 |\n'
        '|S_3  |1       |a   |b   |aba |ba  |ab  |\n'
        '|Z_4  |1       |x   |x^2 |x^3 |    |    |\n'
        '|V_4  |1       |a   |b   |ab  |    |    |\n'
        '+-----+--------+----+----+----+----+----+'
    )

def test_color_padding():
    tbl = Txtble(DATA, headers=HEADERS, padding='\033[31m-\033[m')
    assert str(tbl) == (
        '+-----------+------------+--------------------+\n'
        '|\033[31m-\033[mMonth    \033[31m-\033[m|\033[31m-\033[mBirthstone\033[31m-\033[m|\033[31m-\033[mBirth Flower      \033[31m-\033[m|\n'
        '+-----------+------------+--------------------+\n'
        '|\033[31m-\033[mJanuary  \033[31m-\033[m|\033[31m-\033[mGarnet    \033[31m-\033[m|\033[31m-\033[mCarnation         \033[31m-\033[m|\n'
        '|\033[31m-\033[mFebruary \033[31m-\033[m|\033[31m-\033[mAmethyst  \033[31m-\033[m|\033[31m-\033[mViolet            \033[31m-\033[m|\n'
        '|\033[31m-\033[mMarch    \033[31m-\033[m|\033[31m-\033[mAquamarine\033[31m-\033[m|\033[31m-\033[mJonquil           \033[31m-\033[m|\n'
        '|\033[31m-\033[mApril    \033[31m-\033[m|\033[31m-\033[mDiamond   \033[31m-\033[m|\033[31m-\033[mSweetpea          \033[31m-\033[m|\n'
        '|\033[31m-\033[mMay      \033[31m-\033[m|\033[31m-\033[mEmerald   \033[31m-\033[m|\033[31m-\033[mLily Of The Valley\033[31m-\033[m|\n'
        '|\033[31m-\033[mJune     \033[31m-\033[m|\033[31m-\033[mPearl     \033[31m-\033[m|\033[31m-\033[mRose              \033[31m-\033[m|\n'
        '|\033[31m-\033[mJuly     \033[31m-\033[m|\033[31m-\033[mRuby      \033[31m-\033[m|\033[31m-\033[mLarkspur          \033[31m-\033[m|\n'
        '|\033[31m-\033[mAugust   \033[31m-\033[m|\033[31m-\033[mPeridot   \033[31m-\033[m|\033[31m-\033[mGladiolus         \033[31m-\033[m|\n'
        '|\033[31m-\033[mSeptember\033[31m-\033[m|\033[31m-\033[mSapphire  \033[31m-\033[m|\033[31m-\033[mAster             \033[31m-\033[m|\n'
        '|\033[31m-\033[mOctober  \033[31m-\033[m|\033[31m-\033[mOpal      \033[31m-\033[m|\033[31m-\033[mCalendula         \033[31m-\033[m|\n'
        '|\033[31m-\033[mNovember \033[31m-\033[m|\033[31m-\033[mTopaz     \033[31m-\033[m|\033[31m-\033[mChrysanthemum     \033[31m-\033[m|\n'
        '|\033[31m-\033[mDecember \033[31m-\033[m|\033[31m-\033[mTurquoise \033[31m-\033[m|\033[31m-\033[mNarcissus         \033[31m-\033[m|\n'
        '+-----------+------------+--------------------+'
    )
