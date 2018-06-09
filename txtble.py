__version__      = '0.1.0.dev1'
__author__       = 'John Thorvald Wodder II'
__author_email__ = 'txtble@varonathe.org'
__license__      = 'MIT'
__url__          = 'https://github.com/jwodder/txtble'

from operator  import methodcaller
from six       import text_type
from six.moves import zip_longest
from wcwidth   import wcswidth

class Txtble(object):
    def __init__(
        self,
        data        = (),
        border      = True,
        header_fill = None,
        headers     = None,
        none_str    = '',
        row_fill    = '',
        rstrip      = True,
    ):
        self.data = list(map(list, data))
        self.border = border
        self.header_fill = header_fill
        self.headers = list(headers) if headers is not None else None
        self.none_str = none_str
        if row_fill is None:
            # Reserved to mean something in a later version
            raise ValueError('row_fill cannot be None')
        self.row_fill = row_fill
        self.rstrip = rstrip

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
        data = []
        widths = []
        if self.headers is not None:
            headers = list(map(self._show_cell, self.headers))
            columns = len(headers)
        else:
            headers = None
            columns = 0
        for row in self.data:
            row = list(map(self._show_cell, row))
            if len(row) > columns and \
                    (headers is None or self.header_fill is not None):
                if widths:
                    widths = list(widths) + _row_widths([self.row_fill]) \
                                          * (len(row) - columns)
                columns = len(row)
            row = _to_len(row, columns, self.row_fill)
            widths = map(max, zip_longest(widths, _row_widths(row), fillvalue=0))
            data.append(row)
        if headers is not None:
            if self.header_fill is None:
                assert len(headers) == columns or columns == 0
            else:
                assert len(headers) <= columns
            headers = _to_len(headers, columns, self.header_fill)
            widths = map(max, zip_longest(widths, _row_widths(headers), fillvalue=0))
        widths = list(widths)

        def showrow(row):
            row = _to_len(row, columns, self.row_fill)
            for r in zip_longest(*map(methodcaller('splitlines'), row),
                                 fillvalue=''):
                s = '|'.join(cell + ' ' * (w - wcswidth(cell))
                             for (w, cell) in zip(widths, r))
                if self.border:
                    s = '|' + s + '|'
                elif self.rstrip:
                    s = s.rstrip()
                yield s

        hrule = '+'.join('-' * w for w in widths)
        if self.border:
            hrule = '+' + hrule + '+'
        output = []
        if self.border:
            output.append(hrule)
        if self.headers is not None:
            output.extend(showrow(headers))
            if data:
                output.append(hrule)
        for row in data:
            output.extend(showrow(row))
        if self.border:
            output.append(hrule)
        return '\n'.join(output)

    def _show_cell(self, s):
        if isinstance(s, text_type):
            return s
        elif s is None:
            return self.none_str
        else:
            return str(s)

def _row_widths(row):
    return [max(map(wcswidth, c.splitlines())) if c else 0 for c in row]

def _to_len(xs, length, fill):
    return (xs + [fill] * length)[:length]
