# -*- coding: utf-8 -*-
"""
Yet another plain-text table typesetter

``txtble`` is yet another Python library for creating plain-text tables.  (All
the good names were taken, OK?)  Pass in a list of lists of strings (or other
stringable things) and get out something nice like::

    +---------+----------+------------------+
    |Month    |Birthstone|Birth Flower      |
    +---------+----------+------------------+
    |January  |Garnet    |Carnation         |
    |February |Amethyst  |Violet            |
    |March    |Aquamarine|Jonquil           |
    |April    |Diamond   |Sweetpea          |
    |May      |Emerald   |Lily Of The Valley|
    |June     |Pearl     |Rose              |
    |July     |Ruby      |Larkspur          |
    |August   |Peridot   |Gladiolus         |
    |September|Sapphire  |Aster             |
    |October  |Opal      |Calendula         |
    |November |Topaz     |Chrysanthemum     |
    |December |Turquoise |Narcissus         |
    +---------+----------+------------------+

Visit <https://github.com/jwodder/txtble> for more information.
"""

__version__      = '0.3.0'
__author__       = 'John Thorvald Wodder II'
__author_email__ = 'txtble@varonathe.org'
__license__      = 'MIT'
__url__          = 'https://github.com/jwodder/txtble'

from   collections import namedtuple
from   unicodedata import category
import attr
from   six         import PY2, integer_types, string_types, text_type
from   wcwidth     import wcswidth

__all__ = [
    'ASCII_BORDERS',
    'ASCII_EQ_BORDERS',
    'BorderStyle',
    'DOT_BORDERS',
    'DOUBLE_BORDERS',
    'HEAVY_BORDERS',
    'IndeterminateWidthError',
    'LIGHT_BORDERS',
    'Txtble',
]

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


@attr.s
class Txtble(object):
    data          = attr.ib(default=(), converter=lambda d: list(map(list, d)))
    border        = attr.ib(default=True)
    border_style  = attr.ib(default=ASCII_BORDERS)
    column_border = attr.ib(default=True)
    columns       = attr.ib(default=None)
    header_border = attr.ib(default=None)
    header_fill   = attr.ib(default=None)
    headers       = attr.ib(default=None, converter=attr.converters.optional(list))
    none_str      = attr.ib(default='')
    padding       = attr.ib(default=0)
    row_border    = attr.ib(default=False)
    row_fill      = attr.ib(default='')
    rstrip        = attr.ib(default=True)

    @row_fill.validator
    def _row_fill_validator(self, attrib, value):
        if value is None:
            # Reserved to mean something in a later version
            raise ValueError('row_fill cannot be None')

    @columns.validator
    def _columns_validator(self, attrib, value):
        if value is not None and value < 1:
            raise ValueError('columns must be at least 1')

    def append(self, row):
        self.data.append(list(row))

    def extend(self, data):
        self.data.extend(map(list, data))

    def __str__(self):
        return str(self.show())

    def __unicode__(self):
        return text_type(self.show())

    def show(self):
        if self.row_fill is None:
            raise ValueError('row_fill cannot be None')
        if self.columns is not None and self.columns < 1:
            raise ValueError('columns must be at least 1')
        data = [[Cell(self, c) for c in row] for row in self.data]
        if self.headers is not None:
            headers = [Cell(self, h) for h in self.headers]
            columns = len(headers)
            if self.columns is not None:
                if self.columns != columns:
                    raise ValueError('len(headers) and columns do not match')
            elif self.header_fill is not None:
                columns = max(columns, max(map(len, data)) if data else 0)
                headers = to_len(headers, columns, Cell(self, self.header_fill))
            elif not headers:
                raise ValueError('headers is empty but header_fill is None')
        else:
            headers = None
            if self.columns is not None:
                columns = self.columns
            else:
                columns = max(map(len, data)) if data else 0
        data = [to_len(row, columns, Cell(self, self.row_fill)) for row in data]
        widths = [max(c.width for c in col) for col in zip(*data)]
        if headers is not None:
            if widths:
                widths = [max(w, h.width) for (w,h) in zip(widths, headers)]
            else:
                # This happens when there are no data rows
                widths = [h.width for h in headers]

        if not self.padding:
            padding = ''
        elif isinstance(self.padding, integer_types):
            padding = ' ' * self.padding
        else:
            padding = strify(self.padding)
        if wcswidth(padding) < 0:
            raise IndeterminateWidthError(padding)
        if len(to_lines(padding)) > 1:
            raise ValueError('padding cannot contain newlines')

        if not self.border:
            border = None
        elif isinstance(self.border, BorderStyle):
            border = self.border
        else:
            border = self.border_style

        if self.header_border or \
                (self.header_border is None and headers is not None):
            if isinstance(self.header_border, BorderStyle):
                header_border = self.header_border
            else:
                header_border = self.border_style
        else:
            header_border = None

        if not self.column_border:
            column_border = None
        elif isinstance(self.column_border, BorderStyle):
            column_border = self.column_border
        else:
            column_border = self.border_style

        if not self.row_border:
            row_border = None
        elif isinstance(self.row_border, BorderStyle):
            row_border = self.row_border
        else:
            row_border = self.border_style

        def showrow(row):
            return join_cells(
                row,
                widths,
                col_sep = column_border.vline if column_border else '',
                border  = border.vline        if border        else '',
                rstrip  = self.rstrip,
                padding = padding,
            )

        output = []
        rule_args = (
            [w + 2*wcswidth(padding) for w in widths],
            bool(border),
            bool(column_border),
        )
        if border:
            output.append(border.top_rule(*rule_args))
        if headers is not None:
            output.extend(showrow(headers))
            if data and header_border:
                output.append(header_border.mid_rule(*rule_args))
        elif header_border and not border:
            output.append(header_border.top_rule(*rule_args))
        for i,row in enumerate(data):
            if i>0 and row_border:
                output.append(row_border.mid_rule(*rule_args))
            output.extend(showrow(row))
        if border:
            output.append(border.bot_rule(*rule_args))
        return '\n'.join(output)


class Cell(object):
    def __init__(self, tbl, value):
        if value is None:
            value = tbl.none_str
        self.lines = to_lines(strify(value))
        for line in self.lines:
            if wcswidth(line) < 0:
                raise IndeterminateWidthError(line)
        self.width = max(map(wcswidth, self.lines))

    def box(self, width, height):
        if width == 0:
            lines = list(self.lines)
        else:
            lines = [line + ' ' * (width-wcswidth(line)) for line in self.lines]
        return to_len(lines, height, ' ' * width)


def join_cells(cells, widths, col_sep='|', border='|', rstrip=True, padding=''):
    assert 0 < len(cells) == len(widths)
    height = max(len(c.lines) for c in cells)
    boxes = [c.box(w, height) for (c,w) in zip(cells, widths)]
    if not border and rstrip:
        boxes[-1] = cells[-1].box(0, height)
    return [
        border + padding
            + (padding + col_sep + padding).join(line_bits)
            + (padding if border or not rstrip else '') + border
        for line_bits in zip(*boxes)
    ]

def to_len(xs, length, fill):
    return (xs + [fill] * length)[:length]

def to_lines(s):
    """
    Like `str.splitlines()`, except that an empty string results in a
    one-element list and a trailing newline results in a trailing empty string
    (and all without re-implementing Python's changing line-splitting
    algorithm).

    >>> to_lines('')
    ['']
    >>> to_lines('\\n')
    ['', '']
    >>> to_lines('foo')
    ['foo']
    >>> to_lines('foo\\n')
    ['foo', '']
    >>> to_lines('foo\\nbar')
    ['foo', 'bar']
    >>> to_lines('foo\\fbar')
    ['foo', 'bar']
    >>> to_lines('foo\\vbar')
    ['foo', 'bar']
    """
    lines = s.splitlines(True)
    if not lines:
        return ['']
    if lines[-1].splitlines() != [lines[-1]]:
        lines.append('')
    for i,l in enumerate(lines):
        l2 = l.splitlines()
        assert len(l2) in (0,1)
        lines[i] = l2[0] if l2 else ''
    if PY2 and isinstance(s, str):
        # Manually split on \f and \v
        lines = [
            lf for l in lines
               for lv in l.split('\v')
               for lf in lv.split('\f')
        ]
    return lines

def strify(s):
    if not isinstance(s, string_types):
        s = str(s)
    if s and isinstance(s, text_type) and category(s[0]).startswith('M'):
        s = ' ' + s
    return s.expandtabs()


class IndeterminateWidthError(ValueError):
    """
    Raised when a string is reported as having negative/indeterminate width
    """

    def __init__(self, string):
        #: The string in question
        self.string = string
        super(IndeterminateWidthError, self).__init__(string)

    def __str__(self):
        return '{0.string!r}: string has indeterminate width'.format(self)
