# -*- coding: utf-8 -*-
from six       import text_type
from txtble    import Txtble
from test_data import HEADERS, DATA

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

def test_leading_combining_padding():
    tbl = Txtble(DATA, headers=HEADERS, padding=u'\u0301')
    assert text_type(tbl) == (
        u'+-----------+------------+--------------------+\n'
        u'| \u0301Month     \u0301| \u0301Birthstone \u0301| \u0301Birth Flower       \u0301|\n'
        u'+-----------+------------+--------------------+\n'
        u'| \u0301January   \u0301| \u0301Garnet     \u0301| \u0301Carnation          \u0301|\n'
        u'| \u0301February  \u0301| \u0301Amethyst   \u0301| \u0301Violet             \u0301|\n'
        u'| \u0301March     \u0301| \u0301Aquamarine \u0301| \u0301Jonquil            \u0301|\n'
        u'| \u0301April     \u0301| \u0301Diamond    \u0301| \u0301Sweetpea           \u0301|\n'
        u'| \u0301May       \u0301| \u0301Emerald    \u0301| \u0301Lily Of The Valley \u0301|\n'
        u'| \u0301June      \u0301| \u0301Pearl      \u0301| \u0301Rose               \u0301|\n'
        u'| \u0301July      \u0301| \u0301Ruby       \u0301| \u0301Larkspur           \u0301|\n'
        u'| \u0301August    \u0301| \u0301Peridot    \u0301| \u0301Gladiolus          \u0301|\n'
        u'| \u0301September \u0301| \u0301Sapphire   \u0301| \u0301Aster              \u0301|\n'
        u'| \u0301October   \u0301| \u0301Opal       \u0301| \u0301Calendula          \u0301|\n'
        u'| \u0301November  \u0301| \u0301Topaz      \u0301| \u0301Chrysanthemum      \u0301|\n'
        u'| \u0301December  \u0301| \u0301Turquoise  \u0301| \u0301Narcissus          \u0301|\n'
        u'+-----------+------------+--------------------+'
    )

def test_leading_combining_none_str():
    tbl = Txtble(
        headers=('repr', 'value'),
        data=[
            ("''", ''),
            ('None', None),
            ("'None'", 'None'),
        ],
        none_str=u'\u0301',
    )
    assert text_type(tbl) == (
        u'+------+-----+\n'
        u'|repr  |value|\n'
        u'+------+-----+\n'
        u"|''    |     |\n"
        u"|None  | \u0301    |\n"
        u"|'None'|None |\n"
        u'+------+-----+'
    )

def test_leading_combining_header_fill():
    tbl = Txtble(
        headers=['Header'],
        header_fill=u'\u0301',
        data=[['A'], ['B', 'C']],
    )
    assert text_type(tbl) == (
        u'+------+-+\n'
        u'|Header| \u0301|\n'
        u'+------+-+\n'
        u'|A     | |\n'
        u'|B     |C|\n'
        u'+------+-+'
    )

def test_leading_combining_row_fill():
    tbl = Txtble(
        headers=['Header', 'Header'],
        row_fill=u'\u0301',
        data=[['A'], ['B', 'C']],
    )
    assert text_type(tbl) == (
        u'+------+------+\n'
        u'|Header|Header|\n'
        u'+------+------+\n'
        u'|A     | \u0301     |\n'
        u'|B     |C     |\n'
        u'+------+------+'
    )

# vim:set nowrap:
