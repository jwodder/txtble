"""
Yet another plain-text table typesetter

Visit <https://github.com/jwodder/txtble> for more information.
"""

__version__      = '0.1.0.dev1'
__author__       = 'John Thorvald Wodder II'
__author_email__ = 'txtble@varonathe.org'
__license__      = 'MIT'
__url__          = 'https://github.com/jwodder/txtble'

import attr
from   six     import string_types, text_type
from   wcwidth import wcswidth

__all__ = ['Txtble']

@attr.s
class Txtble(object):
    data          = attr.ib(default=(), converter=lambda d: list(map(list, d)))
    border        = attr.ib(default=True)
    column_border = attr.ib(default=True)
    header_border = attr.ib(default=None)
    header_fill   = attr.ib(default=None)
    headers       = attr.ib(default=None, converter=attr.converters.optional(list))
    none_str      = attr.ib(default='')
    row_border    = attr.ib(default=False)
    row_fill      = attr.ib(default='')
    rstrip        = attr.ib(default=True)

    @row_fill.validator
    def _row_fill_validator(self, attrib, value):
        if value is None:
            # Reserved to mean something in a later version
            raise ValueError('row_fill cannot be None')

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
        data = [[Cell(self, c) for c in row] for row in self.data]
        if self.headers is not None:
            headers = [Cell(self, h) for h in self.headers]
            columns = len(headers)
            if self.header_fill is not None:
                columns = max(columns, max(map(len, data)) if data else 0)
                headers = to_len(headers, columns, Cell(self, self.header_fill))
        else:
            headers = None
            columns = max(map(len, data)) if data else 0
        data = [to_len(row, columns, Cell(self, self.row_fill)) for row in data]
        widths = [max(c.width for c in col) for col in zip(*data)]
        if headers is not None:
            if widths:
                widths = [max(w, h.width) for (w,h) in zip(widths, headers)]
            else:
                # This happens when there are no data rows
                widths = [h.width for h in headers]

        def showrow(row):
            return join_cells(
                row,
                widths,
                col_sep = '|' if self.column_border else '',
                border  = '|' if self.border        else '',
                rstrip  = self.rstrip,
            )

        hrule = ('+' if self.column_border else '').join('-'*w for w in widths)
        if self.border:
            hrule = '+' + hrule + '+'
        output = []
        if self.border:
            output.append(hrule)
        if self.headers is not None:
            output.extend(showrow(headers))
            if data and (self.header_border or self.header_border is None):
                output.append(hrule)
        elif self.header_border and not self.border:
            output.append(hrule)
        for i,row in enumerate(data):
            if i>0 and self.row_border:
                output.append(hrule)
            output.extend(showrow(row))
        if self.border:
            output.append(hrule)
        return '\n'.join(output)


class Cell(object):
    def __init__(self, tbl, value):
        if value is None:
            value = tbl.none_str
        if not isinstance(value, string_types):
            value = str(value)
        self.lines = to_lines(value.expandtabs())
        self.width = max(map(wcswidth, self.lines))

    def box(self, width, height):
        if width == 0:
            lines = list(self.lines)
        else:
            lines = [line + ' ' * (width-wcswidth(line)) for line in self.lines]
        return to_len(lines, height, ' ' * width)


def join_cells(cells, widths, col_sep='|', border='|', rstrip=True):
    assert 0 < len(cells) == len(widths)
    height = max(len(c.lines) for c in cells)
    boxes = [c.box(w, height) for (c,w) in zip(cells, widths)]
    if not border and rstrip:
        boxes[-1] = cells[-1].box(0, height)
    return [
        border + col_sep.join(line_bits) + border
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
    return lines
