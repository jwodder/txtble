from typing import Iterable, NamedTuple

class BorderStyle(NamedTuple):
    hline: str
    vline: str
    ulcorner: str
    urcorner: str
    llcorner: str
    lrcorner: str
    vrtee: str
    vltee: str
    dhtee: str
    uhtee: str
    plus: str

    def top_rule(
        self,
        widths: Iterable[int],
        left_capped: bool,
        right_capped: bool,
        sep_cols: bool,
    ) -> str:
        return rule(
            widths,
            self.hline,
            left_cap  = self.ulcorner if left_capped else '',
            right_cap = self.urcorner if right_capped else '',
            sep       = self.dhtee if sep_cols else '',
        )

    def mid_rule(
        self,
        widths: Iterable[int],
        left_capped: bool,
        right_capped: bool,
        sep_cols: bool,
    ) -> str:
        return rule(
            widths,
            self.hline,
            left_cap  = self.vrtee if left_capped else '',
            right_cap = self.vltee if right_capped else '',
            sep       = self.plus if sep_cols else '',
        )

    def bot_rule(
        self,
        widths: Iterable[int],
        left_capped: bool,
        right_capped: bool,
        sep_cols: bool,
    ) -> str:
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

def rule(widths: Iterable[int], char: str, left_cap: str, right_cap: str, sep: str) -> str:
    return left_cap + sep.join(char * w for w in widths) + right_cap
