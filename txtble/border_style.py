# -*- coding: utf-8 -*-
from collections import namedtuple

class BorderStyle(namedtuple('BorderStyle', '''
    hline    vline
    ulcorner urcorner llcorner lrcorner
    vrtee    vltee    dhtee    uhtee
    plus
''')):
    def top_rule(self, widths, capped, sep_cols):
        rule = (self.dhtee if sep_cols else '')\
                .join(self.hline * w for w in widths)
        return self.ulcorner + rule + self.urcorner if capped else rule

    def mid_rule(self, widths, capped, sep_cols):
        rule = (self.plus if sep_cols else '')\
                .join(self.hline * w for w in widths)
        return self.vrtee + rule + self.vltee if capped else rule

    def bot_rule(self, widths, capped, sep_cols):
        rule = (self.uhtee if sep_cols else '')\
                .join(self.hline * w for w in widths)
        return self.llcorner + rule + self.lrcorner if capped else rule


ASCII_BORDERS    = BorderStyle(*'-|+++++++++')
ASCII_EQ_BORDERS = BorderStyle(*'=|+++++++++')
LIGHT_BORDERS    = BorderStyle(*u'─│┌┐└┘├┤┬┴┼')
HEAVY_BORDERS    = BorderStyle(*u'━┃┏┓┗┛┣┫┳┻╋')
DOUBLE_BORDERS   = BorderStyle(*u'═║╔╗╚╝╠╣╦╩╬')
DOT_BORDERS      = BorderStyle(*u'⋯⋮·········')
