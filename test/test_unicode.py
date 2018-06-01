# -*- coding: utf-8 -*-
from six       import text_type
from tabulator import Tabulator

def test_unicode():
    tbl = Tabulator(
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
    tbl = Tabulator(
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
