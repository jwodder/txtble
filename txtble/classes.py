import attr
from   six           import string_types, text_type
from   .border_style import BorderStyle, ASCII_BORDERS
from   .errors       import IndeterminateWidthError
from   .util         import carry_over_color, join_cells, mkpadding, strify, \
                            strwidth, to_len, to_lines

@attr.s
class Txtble(object):
    data          = attr.ib(default=(), converter=lambda d: list(map(list, d)))
    align         = attr.ib(default=())
    align_fill    = attr.ib(default='l')
    border        = attr.ib(default=True)
    border_style  = attr.ib(default=ASCII_BORDERS)
    column_border = attr.ib(default=True)
    columns       = attr.ib(default=None)
    header_border = attr.ib(default=None)
    header_fill   = attr.ib(default=None)
    headers       = attr.ib(default=None, converter=attr.converters.optional(list))
    left_padding  = attr.ib(default=None)
    len_func      = attr.ib(default=strwidth)
    none_str      = attr.ib(default='')
    padding       = attr.ib(default=0)
    right_padding = attr.ib(default=None)
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

        padding = mkpadding(self.padding, self.len_func)
        if self.left_padding is None:
            left_padding = padding
        else:
            left_padding = mkpadding(self.left_padding, self.len_func)
        if self.right_padding is None:
            right_padding = padding
        else:
            right_padding = mkpadding(self.right_padding, self.len_func)

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

        if isinstance(self.align, string_types):
            align = [self.align] * columns
        else:
            align = to_len(list(self.align), columns, self.align_fill)

        def showrow(row):
            return join_cells(
                row,
                widths,
                align   = align,
                col_sep = column_border.vline if column_border else '',
                border  = border.vline        if border        else '',
                rstrip  = self.rstrip,
                left_padding  = left_padding,
                right_padding = right_padding,
            )

        output = []
        rule_args = (
            [
                w + self.len_func(left_padding) + self.len_func(right_padding)
                for w in widths
            ],
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
        self.lines = carry_over_color(to_lines(strify(value)))
        for line in self.lines:
            if tbl.len_func(line) < 0:
                raise IndeterminateWidthError(line)
        self.width = max(map(tbl.len_func, self.lines))
        self.len_func = tbl.len_func

    def box(self, width, height, align):
        if width == 0:
            lines = list(self.lines)
        else:
            lines = [self.afill(line, width, align) for line in self.lines]
        return to_len(lines, height, ' ' * width)

    def afill(self, s, width, align):
        spaces = width - self.len_func(s)
        if align == 'l':
            return s + ' ' * spaces
        elif align == 'c':
            return ' ' * (spaces // 2) + s + ' ' * ((spaces+1) // 2)
        elif align == 'r':
            return ' ' * spaces + s
        else:
            raise ValueError('{!r}: invalid alignment specifier'.format(align))