# -*- coding: utf-8 -*-
from collections import namedtuple

class BorderStyle(namedtuple('BorderStyle', '''
    hline    vline
    ulcorner urcorner llcorner lrcorner
    vrtee    vltee    dhtee    uhtee
    plus
''')):

    def top_rule(self, widths, left_capped, right_capped, sep_cols):
        return rule(
            widths,
            self.hline,
            left_cap  = self.ulcorner if left_capped else '',
            right_cap = self.urcorner if right_capped else '',
            sep       = self.dhtee if sep_cols else '',
        )

    def mid_rule(self, widths, left_capped, right_capped, sep_cols):
        return rule(
            widths,
            self.hline,
            left_cap  = self.vrtee if left_capped else '',
            right_cap = self.vltee if right_capped else '',
            sep       = self.plus if sep_cols else '',
        )

    def bot_rule(self, widths, left_capped, right_capped, sep_cols):
        return rule(
            widths,
            self.hline,
            left_cap  = self.llcorner if left_capped else '',
            right_cap = self.lrcorner if right_capped else '',
            sep       = self.uhtee if sep_cols else '',
        )


ASCII_BORDERS    = BorderStyle(*'-|+++++++++')
ASCII_EQ_BORDERS = BorderStyle(*'=|+++++++++')
LIGHT_BORDERS    = BorderStyle(*u'─│┌┐└┘├┤┬┴┼')
HEAVY_BORDERS    = BorderStyle(*u'━┃┏┓┗┛┣┫┳┻╋')
DOUBLE_BORDERS   = BorderStyle(*u'═║╔╗╚╝╠╣╦╩╬')
DOT_BORDERS      = BorderStyle(*u'⋯⋮·········')

def rule(widths, char, left_cap, right_cap, sep):
    return left_cap + sep.join(char * w for w in widths) + right_cap
