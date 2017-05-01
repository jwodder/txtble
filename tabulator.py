from itertools import izip_longest

__all__ = ["Tabulator"]

class Tabulator(object):
    def __init__(self, include_extra_columns=True,
                       extra_header=u'',
                       fill_empty_columns=u'',
                       border=False,
                       trim_spaces=True):
        self.include_extra_columns = include_extra_columns
        self.extra_header = extra_header
        self.fill_empty_columns = fill_empty_columns
        self.border = border
        self.trim_spaces = trim_spaces

    def show(self, table, headers=None):
        data = []
        if headers is not None:
            headers = map(unistr, headers)
            columns = len(headers)
            widths = [max(len, h.splitlines()) for h in headers]
        else:
            columns = 0
            widths = []
        for row in table:
            row = map(unistr, row)
            if len(row) > columns:
                if headers is not None and not self.include_extra_columns:
                    row = row[:columns]
                else:
                    columns = max(len(row), columns)
            elif len(row) < columns:
                row = (row + [self.fill_empty_columns] * columns)[:columns]
            widths = map(max, izip_longest(widths, map(len, row), fillvalue=0))
            data.append(row)
        def showrow(row):
            s = u''
            for row_ in izip_longest(*map(unicode.splitlines, row),
                                     fillvalue=u''):
                s1 = u'|'.join(u'%-*s' % (w, cell)
                               for (w, cell) in zip(widths, row))
                if self.border:
                    s1 = u'|' + s1 + u'|'
                elif self.trim_spaces:
                    s1 = s1.rstrip()
                s += s1 + u'\n'
            return s
        hrule = u'+'.join(u'-' * w for w in widths)
        if self.border:
            hrule = u'+' + hrule + u'+'
        hrule += u'\n'
        output = u''
        if self.border:
            output += hrule
        if self.headers is not None:
            output += showrow(headers + [self.extra_header] * (columns - len(headers)))
            output += hrule
        output += u''.join(showrow(row) for row in data)
        if self.border:
            output += hrule
        return output

def unistr(val):  # internal helper function
    try:
        s = unicode(val)
    except Exception:
        try:
            s1 = str(val)
        except Exception:
            s1 = repr(val)
        try:
            s = s1.decode('utf-8')
        except UnicodeDecodeError:
            s = s1.decode('latin-1')
    return s
