# -*- coding: utf-8 -*-
from six    import text_type
from txtble import Txtble

class Custom(object):
    def __str__(self):
        return 'str'

    def __unicode__(self):
        return u'unicode'

    def __bytes__(self):
        return b'bytes'


def test_none():
    tbl = Txtble(
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

def test_none_str():
    tbl = Txtble(
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

def test_tab_none_str():
    tbl = Txtble(
        headers=('repr', 'value'),
        data=[
            ("''", ''),
            ('None', None),
            ("'None'", 'None'),
        ],
        none_str='<\t>',
    )
    assert str(tbl) == (
        '+------+---------+\n'
        '|repr  |value    |\n'
        '+------+---------+\n'
        "|''    |         |\n"
        "|None  |<       >|\n"
        "|'None'|None     |\n"
        '+------+---------+'
    )

def test_custom():
    tbl = Txtble(data=[['A', 'B'], ['C', Custom()]])
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
    tbl = Txtble(data=[[u'Å', u'B'], [u'Č', Custom()]])
    assert text_type(tbl) == (
        u'+-+---+\n'
        u'|Å|B  |\n'
        u'|Č|str|\n'
        u'+-+---+'
    )
