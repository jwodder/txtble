# -*- coding: utf-8 -*-
from six       import text_type
from tabulator import Tabulator

class Custom(object):
    def __str__(self):
        return 'str'

    def __unicode__(self):
        return u'unicode'

    def __bytes__(self):
        return b'bytes'


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

def test_custom():
    tbl = Tabulator(data=[['A', 'B'], ['C', Custom()]])
    assert str(tbl) == (
        '+-+---+\n'
        '|A|B  |\n'
        '|C|str|\n'
        '+-+---+'
    )
    assert text_type(tbl) == (
        u'+-+---+\n'
        u'|A|B  |\n'
        u'|C|str|\n'
        u'+-+---+'
    )

def test_custom_plus_unicode():
    tbl = Tabulator(data=[[u'Å', u'B'], [u'Č', Custom()]])
    assert text_type(tbl) == (
        u'+-+---+\n'
        u'|Å|B  |\n'
        u'|Č|str|\n'
        u'+-+---+'
    )
