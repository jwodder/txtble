# -*- coding: utf-8 -*-
from six    import text_type
from txtble import Txtble

# Taken from /usr/share/misc/birthtoken.gz in Ubuntu Xenial's miscfiles package:
HEADERS = ['Month', 'Birthstone', 'Birth Flower']
DATA = [
    ['January',   'Garnet',     'Carnation'],
    ['February',  'Amethyst',   'Violet'],
    ['March',     'Aquamarine', 'Jonquil'],
    ['April',     'Diamond',    'Sweetpea'],
    ['May',       'Emerald',    'Lily Of The Valley'],
    ['June',      'Pearl',      'Rose'],
    ['July',      'Ruby',       'Larkspur'],
    ['August',    'Peridot',    'Gladiolus'],
    ['September', 'Sapphire',   'Aster'],
    ['October',   'Opal',       'Calendula'],
    ['November',  'Topaz',      'Chrysanthemum'],
    ['December',  'Turquoise',  'Narcissus'],
]

def test_unicode():
    tbl = Txtble(
        headers=('English', 'Latin'),
        data=[
            ['to love',    u'amāre'],
            ['to teach',   u'docēre'],
            ['to put',     u'pōnere'],
            ['to take',    u'capere'],
            ['to fortify', u'mūnīre'],
        ],
    )
    assert text_type(tbl) == (
        u'+----------+------+\n'
        u'|English   |Latin |\n'
        u'+----------+------+\n'
        u'|to love   |amāre |\n'
        u'|to teach  |docēre|\n'
        u'|to put    |pōnere|\n'
        u'|to take   |capere|\n'
        u'|to fortify|mūnīre|\n'
        u'+----------+------+'
    )

def test_unicode_nfd():
    tbl = Txtble(
        headers=['NFC', 'NFD'],
        data=[
            [u'Pok\u00E9mon', u'Poke\u0301mon'],
        ],
    )
    assert text_type(tbl) == (
        u'+-------+-------+\n'
        u'|NFC    |NFD    |\n'
        u'+-------+-------+\n'
        u'|Pok\u00E9mon|Poke\u0301mon|\n'
        u'+-------+-------+'
    )

def test_fullwidth():
    tbl = Txtble(
        headers=['Halfwidth', 'Fullwidth'],
        data=[
            ['Test text', u'Ｔｅｓｔ\u3000ｔｅｘｔ'],
        ],
    )
    assert text_type(tbl) == (
        u'+---------+------------------+\n'
        u'|Halfwidth|Fullwidth         |\n'
        u'+---------+------------------+\n'
        u'|Test text|Ｔｅｓｔ\u3000ｔｅｘｔ|\n'
        u'+---------+------------------+'
    )

def test_leading_combining():
    tbl = Txtble(
        headers=['Category', 'Name', 'Glyph'],
        data=[
            ['Mn', 'COMBINING ACUTE ACCENT', u'\u0301'],
            ['Mc', 'DEVANAGARI SIGN VISARGA', u'\u0903'],
            ['Me', 'COMBINING CYRILLIC HUNDRED THOUSANDS SIGN', u'\u0488'],
        ]
    )
    assert text_type(tbl) == (
        u'+--------+-----------------------------------------+-----+\n'
        u'|Category|Name                                     |Glyph|\n'
        u'+--------+-----------------------------------------+-----+\n'
        u'|Mn      |COMBINING ACUTE ACCENT                   | \u0301    |\n'
        u'|Mc      |DEVANAGARI SIGN VISARGA                  | \u0903   |\n'
        u'|Me      |COMBINING CYRILLIC HUNDRED THOUSANDS SIGN| \u0488    |\n'
        u'+--------+-----------------------------------------+-----+'
    )

def test_fullwidth_padding():
    tbl = Txtble(DATA, headers=HEADERS, padding=u'\uFF0D')
    assert text_type(tbl) == (
        u'+-------------+--------------+----------------------+\n'
        u'|－Month    －|－Birthstone－|－Birth Flower      －|\n'
        u'+-------------+--------------+----------------------+\n'
        u'|－January  －|－Garnet    －|－Carnation         －|\n'
        u'|－February －|－Amethyst  －|－Violet            －|\n'
        u'|－March    －|－Aquamarine－|－Jonquil           －|\n'
        u'|－April    －|－Diamond   －|－Sweetpea          －|\n'
        u'|－May      －|－Emerald   －|－Lily Of The Valley－|\n'
        u'|－June     －|－Pearl     －|－Rose              －|\n'
        u'|－July     －|－Ruby      －|－Larkspur          －|\n'
        u'|－August   －|－Peridot   －|－Gladiolus         －|\n'
        u'|－September－|－Sapphire  －|－Aster             －|\n'
        u'|－October  －|－Opal      －|－Calendula         －|\n'
        u'|－November －|－Topaz     －|－Chrysanthemum     －|\n'
        u'|－December －|－Turquoise －|－Narcissus         －|\n'
        u'+-------------+--------------+----------------------+'
    )
