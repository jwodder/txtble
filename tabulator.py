__version__      = '0.1.0.dev1'
__author__       = 'John Thorvald Wodder II'
__author_email__ = 'tabulator@varonathe.org'
__license__      = 'MIT'
__url__          = 'https://github.com/jwodder/tabulator'

from operator  import methodcaller
from six       import text_type
from six.moves import zip_longest
from wcwidth   import wcswidth

class Tabulator(object):
    def __init__(self, data=(),
        headers=None,
        include_extra_columns=True,
        extra_header='',
        fill_empty_columns='',
        border=True,
        trim_spaces=True,
        none_str='',
    ):
        self.data = list(map(list, data))
        self.headers = list(headers) if headers is not None else None
        self.include_extra_columns = include_extra_columns
        self.extra_header = extra_header
        self.fill_empty_columns = fill_empty_columns
        self.border = border
        self.trim_spaces = trim_spaces
        self.none_str = none_str

    def append(self, row):
        self.data.append(list(row))

    def extend(self, data):
        self.data.extend(map(list, data))

    def __str__(self):
        return str(self.show())

    def __unicode__(self):
        return text_type(self.show())

    def show(self):
        data = []
        if self.headers is not None:
            headers = list(map(self._show_cell, self.headers))
            columns = len(headers)
            widths = [max(map(wcswidth, h.splitlines())) for h in headers]
        else:
            columns = 0
            widths = []
        for row in self.data:
            row = list(map(self._show_cell, row))
            if len(row) > columns:
                if headers is not None and not self.include_extra_columns:
                    row = row[:columns]
                else:
                    columns = max(len(row), columns)
            elif len(row) < columns:
                row = (row + [self.fill_empty_columns] * columns)[:columns]
            widths = map(max, zip_longest(widths, map(wcswidth, row), fillvalue=0))
            data.append(row)
        widths = list(widths)

        def showrow(row):
            s = ''
            for r in zip_longest(*map(methodcaller('splitlines'), row), fillvalue=''):
                s1 = '|'.join(cell + ' ' * (w - wcswidth(cell))
                              for (w, cell) in zip(widths, r))
                if self.border:
                    s1 = '|' + s1 + '|'
                elif self.trim_spaces:
                    s1 = s1.rstrip()
                s += s1
            return s

        hrule = '+'.join('-' * w for w in widths)
        if self.border:
            hrule = '+' + hrule + '+'
        output = ''
        if self.border:
            output += hrule + '\n'
        if self.headers is not None:
            output += showrow(headers + [self.extra_header] * (columns - len(headers))) + '\n'
            output += hrule + '\n'
        output += '\n'.join(map(showrow, data))
        if self.border:
            output += '\n' + hrule
        return output

    def _show_cell(self, s):
        if isinstance(s, text_type):
            return s
        elif s is None:
            return self.none_str
        else:
            return str(s)
