import attr
from   six           import integer_types, string_types, text_type
from   .border_style import ASCII_BORDERS
from   .errors       import IndeterminateWidthError
from   .util         import carry_over_color, join_cells, mkpadding, strify, \
                            strwidth, to_len, to_lines, wrap, first_style

try:
    from collections.abc import Mapping
except ImportError:
    from collections     import Mapping

DICT_FILL_RAISE = object()

def data_converter(value):
    data = []
    for row in value:
        if not isinstance(row, Mapping):
            row = list(row)
        data.append(row)
    return data

@attr.s
class Txtble(object):
    data             = attr.ib(default=(), converter=data_converter)
    align            = attr.ib(default=())
    align_fill       = attr.ib(default='l')
    border           = attr.ib(default=True)
    border_style     = attr.ib(default=ASCII_BORDERS)
    bottom_border    = attr.ib(default=None)
    break_long_words = attr.ib(default=True)
    break_on_hyphens = attr.ib(default=True)
    column_border    = attr.ib(default=True)
    columns          = attr.ib(default=None)
    dict_fill        = attr.ib(default=DICT_FILL_RAISE)
    header_border    = attr.ib(default=None)
    header_fill      = attr.ib(default=None)
    headers          = attr.ib(default=None, converter=attr.converters.optional(list))
    left_border      = attr.ib(default=None)
    left_padding     = attr.ib(default=None)
    len_func         = attr.ib(default=strwidth)
    none_str         = attr.ib(default='')
    padding          = attr.ib(default=0)
    right_border     = attr.ib(default=None)
    right_padding    = attr.ib(default=None)
    row_border       = attr.ib(default=False)
    row_fill         = attr.ib(default='')
    rstrip           = attr.ib(default=True)
    top_border       = attr.ib(default=None)
    width_fill       = attr.ib(default=None)
    widths           = attr.ib(default=())
    wrap_func        = attr.ib(default=None)

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
        if not isinstance(row, Mapping):
            row = list(row)
        self.data.append(row)

    def extend(self, data):
        for row in data:
            self.append(row)

    def __str__(self):
        return str(self.show())

    def __unicode__(self):
        return text_type(self.show())

    def show(self):
        if self.row_fill is None:
            raise ValueError('row_fill cannot be None')
        if self.columns is not None and self.columns < 1:
            raise ValueError('columns must be at least 1')

        def dict_get(d,k):
            try:
                return d[k]
            except KeyError:
                if self.dict_fill is DICT_FILL_RAISE:
                    raise
                else:
                    return self.dict_fill

        data = []
        for row in self.data:
            if isinstance(row, Mapping):
                if self.headers is None:
                    raise ValueError('dict row not allowed when headers is None')
                data.append([Cell(self, dict_get(row,h)) for h in self.headers])
            else:
                data.append([Cell(self, c) for c in row])

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

        if isinstance(self.widths, (integer_types, type(None))):
            wrap_widths = [self.widths] * columns
        else:
            wrap_widths = to_len(list(self.widths), columns, self.width_fill)
        for row in data:
            for c,w in zip(row, wrap_widths):
                c.wrap(w)

        widths = [
            max(w or 0, max(c.width for c in col))
            for w,col in zip(wrap_widths, zip(*data))
        ]
        if headers is not None:
            for h,w in zip(headers, wrap_widths):
                h.wrap(w)
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

        border = self.border and first_style(self.border, self.border_style)

        if self.left_border is None:
            left_border = border
        else:
            left_border = self.left_border and \
                first_style(self.left_border, border, self.border_style)

        if self.right_border is None:
            right_border = border
        else:
            right_border = self.right_border and \
                first_style(self.right_border, border, self.border_style)

        if self.top_border is None:
            top_border = border
        else:
            top_border = self.top_border and \
                first_style(self.top_border, border, self.border_style)

        if self.bottom_border is None:
            bottom_border = border
        else:
            bottom_border = self.bottom_border and \
                first_style(self.bottom_border, border, self.border_style)

        if self.header_border or \
                (self.header_border is None and headers is not None):
            header_border = first_style(self.header_border, self.border_style)
        else:
            header_border = None

        column_border = self.column_border and \
            first_style(self.column_border, self.border_style)
        row_border = self.row_border and \
            first_style(self.row_border, self.border_style)

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
                left_border_line  = left_border.vline  if left_border  else '',
                right_border_line = right_border.vline if right_border else '',
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
            bool(left_border),
            bool(right_border),
            bool(column_border),
        )
        if top_border:
            output.append(top_border.top_rule(*rule_args))
        if headers is not None:
            output.extend(showrow(headers))
            if data and header_border:
                output.append(header_border.mid_rule(*rule_args))
        elif header_border and not top_border:
            output.append(header_border.top_rule(*rule_args))
        for i,row in enumerate(data):
            if i>0 and row_border:
                output.append(row_border.mid_rule(*rule_args))
            output.extend(showrow(row))
        if bottom_border:
            output.append(bottom_border.bot_rule(*rule_args))
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
        self.table = tbl

    def box(self, width, height, align):
        if width == 0:
            lines = list(self.lines)
        else:
            lines = [self.afill(line, width, align) for line in self.lines]
        return to_len(lines, height, ' ' * width)

    def afill(self, s, width, align):
        spaces = width - self.table.len_func(s)
        if align == 'l':
            return s + ' ' * spaces
        elif align == 'c':
            return ' ' * (spaces // 2) + s + ' ' * ((spaces+1) // 2)
        elif align == 'r':
            return ' ' * spaces + s
        else:
            raise ValueError('{!r}: invalid alignment specifier'.format(align))

    def wrap(self, width):
        if width is None:
            return
        elif width <= 0:
            raise ValueError(width)
        elif not isinstance(width, integer_types):
            raise TypeError(width)
        if self.table.wrap_func is None:
            def wrap_func(s):
                return carry_over_color(wrap(
                    s, width,
                    len_func         = self.table.len_func,
                    break_long_words = self.table.break_long_words,
                    break_on_hyphens = self.table.break_on_hyphens,
                ))
        else:
            def wrap_func(s):
                if self.table.len_func(s) <= width:
                    return [s]
                return carry_over_color(
                    [x.expandtabs() for x in self.table.wrap_func(s, width)]
                )
        self.lines = [
            wrapped for line in self.lines for wrapped in wrap_func(line)
        ]
        for line in self.lines:
            if self.table.len_func(line) < 0:
                raise IndeterminateWidthError(line)
        self.width = max(map(self.table.len_func, self.lines))
