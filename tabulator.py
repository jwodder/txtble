# -*- coding: utf-8 -*-

# TO ADD:
# - Parameters for setting minimum, maximum, and exact column widths
#  - Parameter for setting how to handle overly large fields: let them
#    overflow, truncate them, or line-wrap them
# - Parameters for setting exact (and/or min/max?) number of columns
# - Unicode output with box-drawing characters:
#
#    ASCII         - | + + + + + + + + +
#    Light         ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
#    Heavy         ━ ┃ ┏ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋
#    Double        ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
#    Dots          ⋯ ⋮ · · · · · · · · ·
#
# - Setting the strings to use for column separators, hrules, joints, corners,
#   etc.
# - Parameter for adding an hrule between every pair of rows
#  - Parameter for a special hrule after the headers?
# - Parameter for putting an hrule at the top in the absence of headers or
#   borders
# - Parameter for padding between vertical bars and cell contents
# - Parameter for adding vertical but not horizontal borders
# - Parameter for adding horizontal but not vertical borders
# - Centering & right-aligning of specified columns
# - Add a method that simply returns the padded & folded cells as an array of
#   arrays of strings rather than formatting them
# - cells that span multiple columns and/or rows
# - constructing a table from a sequence of dicts or objects with
#   elements/attributes that match the table's headers
# - Add an "hrule" class that can be passed in place of a data row to indicate
#   that a horizontal rule should be added.  Its constructor should take
#   optional keyword arguments for setting the box-drawing characters to use
#   ('dash', 'joint', 'left_joint', 'right_join', 'midjoint'?)
# - parameter for setting how to display `None`s
# - parameter for setting how to show bools?
# - parameter for producing Markdown- or reStructuredText-compatible tables
# - parameter for producing HTML tables
# - parsing a text table back into a Tabulator object?
# - transposition
# - handling of Unicode characters with non-unit width

# cf. texttable, prettytable, tabulate

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
