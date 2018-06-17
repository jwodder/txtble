# -*- coding: utf-8 -*-
from six    import text_type
from txtble import Txtble

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
