from __future__ import annotations
from collections.abc import Callable, Iterable, Mapping, Sequence
from numbers import Number
import re
from typing import Any, Optional
import attr
from .border_style import ASCII_BORDERS, BorderStyle
from .errors import (
    IndeterminateWidthError,
    NumericWidthOverflowError,
    UnterminatedColorError,
)
from .util import (
    LenFunc,
    breakable_units,
    carry_over_color,
    first_style,
    strify,
    strwidth,
    to_len,
    to_lines,
)

DICT_FILL_RAISE = object()


def data_converter(value: Iterable[Iterable | Mapping]) -> list[list | Mapping]:
    data = []
    for row in value:
        if not isinstance(row, Mapping):
            row = list(row)
        data.append(row)
    return data


def headers_converter(value: Iterable | None) -> list | None:
    if value is not None:
        return list(value)
    else:
        return None


@attr.s(auto_attribs=True)
class Txtble:
    data: list[list | Mapping] = attr.ib(default=(), converter=data_converter)
    align: str | Sequence[str] = ()
    align_fill: str = "l"
    border: bool | BorderStyle = True
    border_style: BorderStyle = ASCII_BORDERS
    bottom_border: bool | BorderStyle | None = None
    break_long_words: bool = True
    break_on_hyphens: bool = True
    column_border: bool | BorderStyle = True
    columns: Optional[int] = attr.ib(default=None)
    dict_fill: Any = DICT_FILL_RAISE
    header_border: bool | BorderStyle | None = None
    header_fill: Any = None
    headers: Optional[list] = attr.ib(default=None, converter=headers_converter)
    left_border: bool | BorderStyle | None = None
    left_padding: int | str | None = None
    len_func: Optional[LenFunc] = strwidth
    none_str: Any = ""
    padding: int | str = 0
    right_border: bool | BorderStyle | None = None
    right_padding: int | str | None = None
    row_border: bool | BorderStyle = False
    row_fill: Any = attr.ib(default="")
    rstrip: bool = True
    top_border: bool | BorderStyle | None = None
    valign: str | Sequence[str] = ()
    valign_fill: str = "t"
    width_fill: Optional[int] = None
    widths: int | Sequence[Optional[int]] | None = ()
    wrap_func: Optional[Callable[[str, int], Iterable[str]]] = None

    @row_fill.validator
    def _row_fill_validator(self, _attrib: attr.Attribute, value: Any) -> None:
        if value is None:
            # Reserved to mean something in a later version
            raise ValueError("row_fill cannot be None")

    @columns.validator
    def _columns_validator(
        self,
        _attrib: attr.Attribute,
        value: Optional[int],
    ) -> None:
        if value is not None and value < 1:
            raise ValueError("columns must be at least 1")

    def append(self, row: Iterable | Mapping) -> None:
        if not isinstance(row, Mapping):
            row = list(row)
        self.data.append(row)

    def extend(self, data: Iterable[Iterable | Mapping]) -> None:
        for row in data:
            self.append(row)

    def __str__(self) -> str:
        return str(self.show())

    def _len(self, s: str) -> int:
        w = (self.len_func or strwidth)(s)
        if w < 0:
            raise IndeterminateWidthError(s)
        return w

    def _mkpadding(self, s: Any) -> str:
        if not s:
            padding = ""
        elif isinstance(s, int):
            padding = " " * s
        else:
            padding = strify(s)
            self._len(padding)  # Raise IndeterminateWidthError if neg. width
        if len(to_lines(padding)) > 1:
            raise ValueError("padding cannot contain newlines")
        return padding

    def _wrap(self, s: str, width: int) -> list[str]:
        if self.wrap_func is None:
            return carry_over_color(self._base_wrap(s, width))
        elif self._len(s) <= width:
            return [s]
        else:
            return carry_over_color([x.expandtabs() for x in self.wrap_func(s, width)])

    def _base_wrap(self, s: str, width: int) -> list[str]:
        def length(ss: str) -> int:
            try:
                return self._len(ss)
            except UnterminatedColorError:
                # Appending sgr0 unconditionally is the wrong thing to do when
                # len_func is set to, say, the builtin `len`.
                return self._len(ss + "\033[m")

        if not s:
            return [s]
        wrapped = []
        break_point = r"-| +" if self.break_on_hyphens else r" +"
        while length(s) > width:
            for m in reversed(list(re.finditer(break_point, s))):
                pre = s[: m.end()].rstrip(" ")
                post = s[m.end() :]
                assert not re.search(
                    r"\033[^m]*$", pre
                ), "Space or hyphen inside ANSI sequence"
                ### XXX: Problem: What if a custom len_func accepts ESC not
                ### followed by 'm'?
                if 0 <= length(pre) <= width:
                    wrapped.append(pre)
                    s = post
                    break
            else:
                if self.break_long_words:
                    # Do a binary search on valid breakpoints until we find the
                    # longest initial substring shorter than `width`
                    units = breakable_units(s)
                    low = 0
                    high = len(units)
                    while low < high:
                        i = (low + high) // 2
                        pre = "".join(units[:i])
                        post = "".join(units[i:])
                        w = length(pre)
                        assert w >= 0
                        if w < width:
                            if length("".join(units[: i + 1])) > width:
                                break
                            else:
                                low = i + 1
                        elif w == width:
                            break
                        else:
                            assert w > width
                            high = i
                    else:
                        raise AssertionError(
                            "Unreachable state reached"
                        )  # pragma: no cover
                    wrapped.append(pre)
                    s = post
                else:
                    # Break at the first hyphen or space, if any
                    m2 = re.search(break_point, s)
                    if m2:
                        wrapped.append(s[: m2.end()].rstrip(" "))
                        s = s[m2.end() :]
                    else:
                        # `s` is just one long, unbreakable word; break out of
                        # the `for` loop
                        break
        wrapped.append(s)
        return wrapped

    def show(self) -> str:
        if self.row_fill is None:
            raise ValueError("row_fill cannot be None")
        if self.columns is not None and self.columns < 1:
            raise ValueError("columns must be at least 1")

        def dict_get(d: Mapping, k: Any) -> Any:
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
                    raise ValueError("dict row not allowed when headers is None")
                data.append([Cell(self, dict_get(row, h)) for h in self.headers])
            else:
                data.append([Cell(self, c) for c in row])

        headers: Optional[list[Cell]]
        if self.headers is not None:
            headers = [Cell(self, h) for h in self.headers]
            columns = len(headers)
            if self.columns is not None:
                if self.columns != columns:
                    raise ValueError("len(headers) and columns do not match")
            elif self.header_fill is not None:
                columns = max(columns, max(map(len, data)) if data else 0)
                headers = to_len(headers, columns, Cell(self, self.header_fill))
            elif not headers:
                raise ValueError("headers is empty but header_fill is None")
        else:
            headers = None
            if self.columns is not None:
                columns = self.columns
            else:
                columns = max(map(len, data)) if data else 0
        data = [to_len(row, columns, Cell(self, self.row_fill)) for row in data]

        wrap_widths: list[Optional[int]]
        if isinstance(self.widths, int) or self.widths is None:
            wrap_widths = [self.widths] * columns
        else:
            wrap_widths = to_len(list(self.widths), columns, self.width_fill)
        for row in data:
            for c, w in zip(row, wrap_widths):
                c.wrap(w)

        widths = [
            max(w or 0, max(c.width for c in col))
            for w, col in zip(wrap_widths, zip(*data))
        ]
        if headers is not None:
            for h, w in zip(headers, wrap_widths):
                h.wrap(w)
            if widths:
                widths = [max(w, h.width) for (w, h) in zip(widths, headers)]
            else:
                # This happens when there are no data rows
                widths = [h.width for h in headers]

        padding = self._mkpadding(self.padding)
        if self.left_padding is None:
            left_padding = padding
        else:
            left_padding = self._mkpadding(self.left_padding)
        if self.right_padding is None:
            right_padding = padding
        else:
            right_padding = self._mkpadding(self.right_padding)

        border = self.border and first_style(self.border, self.border_style)

        if self.left_border is None:
            left_border = border
        else:
            left_border = self.left_border and first_style(
                self.left_border, border, self.border_style
            )

        if self.right_border is None:
            right_border = border
        else:
            right_border = self.right_border and first_style(
                self.right_border, border, self.border_style
            )

        if self.top_border is None:
            top_border = border
        else:
            top_border = self.top_border and first_style(
                self.top_border, border, self.border_style
            )

        if self.bottom_border is None:
            bottom_border = border
        else:
            bottom_border = self.bottom_border and first_style(
                self.bottom_border, border, self.border_style
            )

        header_border: Optional[BorderStyle]
        if self.header_border or (self.header_border is None and headers is not None):
            header_border = first_style(self.header_border, self.border_style)
        else:
            header_border = None

        column_border = self.column_border and first_style(
            self.column_border, self.border_style
        )
        row_border = self.row_border and first_style(self.row_border, self.border_style)

        align: list[str]
        if isinstance(self.align, str):
            align = [self.align] * columns
        else:
            align = to_len(list(self.align), columns, self.align_fill)

        num_spacing: list[Optional[tuple[int, int]]] = [None] * columns
        for i, a in enumerate(align):
            if "n" in a:
                predot = 0
                postdot = 0
                if headers is not None and headers[i].is_numeric:
                    if len(headers[i].lines) > 1:
                        # Number overflowed width and was wrapped
                        raise NumericWidthOverflowError()
                    pred, _, postd = headers[i].lines[0].partition(".")
                    predot = max(predot, self._len(pred))
                    postdot = max(postdot, self._len(postd))
                for row in data:
                    if row[i].is_numeric:
                        if len(row[i].lines) > 1:
                            # Number overflowed width and was wrapped
                            raise NumericWidthOverflowError()
                        pred, _, postd = row[i].lines[0].partition(".")
                        predot = max(predot, self._len(pred))
                        postdot = max(postdot, self._len(postd))
                num_spacing[i] = (predot, postdot)
                numwidth = predot
                if postdot > 0:
                    numwidth += 1 + postdot
                wwi = wrap_widths[i]
                if wwi is not None and numwidth > wwi:
                    raise NumericWidthOverflowError()
                widths[i] = max(widths[i], numwidth)

        if isinstance(self.valign, str):
            valign = [self.valign] * columns
        else:
            valign = to_len(list(self.valign), columns, self.valign_fill)

        def showrow(row: list[Cell]) -> list[str]:
            return join_cells(
                row,
                widths,
                align=align,
                valign=valign,
                col_sep=column_border.vline if column_border else "",
                left_border_line=left_border.vline if left_border else "",
                right_border_line=right_border.vline if right_border else "",
                rstrip=self.rstrip,
                left_padding=left_padding,
                right_padding=right_padding,
                num_spacing=num_spacing,
            )

        output = []
        rule_args = (
            [w + self._len(left_padding) + self._len(right_padding) for w in widths],
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
        for i, row in enumerate(data):
            if i > 0 and row_border:
                output.append(row_border.mid_rule(*rule_args))
            output.extend(showrow(row))
        if bottom_border:
            output.append(bottom_border.bot_rule(*rule_args))
        return "\n".join(output)


class Cell:
    def __init__(self, tbl: Txtble, value: Any):
        if value is None:
            value = tbl.none_str
        self.value: Any = value
        self.lines: list[str] = carry_over_color(to_lines(strify(value)))
        self.width: int = max(map(tbl._len, self.lines))
        self.table: Txtble = tbl
        self.is_numeric: bool = isinstance(value, Number) and len(self.lines) == 1

    def box(
        self,
        width: int,
        height: int,
        align: str,
        valign: str,
        num_spacing: Optional[tuple[int, int]],
    ) -> list[str]:
        if "n" in align and self.is_numeric:
            assert num_spacing is not None
            pred, dot, postd = self.lines[0].partition(".")
            pred = " " * (num_spacing[0] - self.table._len(pred)) + pred
            if not dot and num_spacing[1] > 0:
                dot = " "
            postd += " " * (num_spacing[1] - self.table._len(postd))
            self.lines[0] = pred + dot + postd
        if width == 0:
            if "n" in align and self.is_numeric:
                lines = list(map(str.rstrip, self.lines))
            else:
                lines = list(self.lines)
        else:
            lines = [self.afill(line, width, align) for line in self.lines]
        vspace = [" " * width] * (height - len(lines))
        if valign == "t":
            return lines + vspace
        elif valign == "m":
            return vspace[: len(vspace) // 2] + lines + vspace[len(vspace) // 2 :]
        elif valign == "b":
            return vspace + lines
        else:
            raise ValueError(f"{valign!r}: invalid vertical alignment specifier")

    def afill(self, s: str, width: int, align: str) -> str:
        spaces = width - self.table._len(s)
        if align in ("l", "n", "nl", "ln"):
            return s + " " * spaces
        elif align in ("c", "nc", "cn"):
            return " " * (spaces // 2) + s + " " * ((spaces + 1) // 2)
        elif align in ("r", "nr", "rn"):
            return " " * spaces + s
        else:
            raise ValueError(f"{align!r}: invalid alignment specifier")

    def wrap(self, width: Optional[int]) -> None:
        if width is None:
            return
        elif width <= 0:
            raise ValueError(f"negative column width: {width}")
        else:
            iwidth = width
        self.lines = [
            wrapped for line in self.lines for wrapped in self.table._wrap(line, iwidth)
        ]
        self.width = max(map(self.table._len, self.lines))


def join_cells(
    cells: list[Cell],
    widths: list[int],
    align: list[str],
    valign: list[str],
    col_sep: str,
    left_border_line: str,
    right_border_line: str,
    rstrip: bool,
    left_padding: str,
    right_padding: str,
    num_spacing: list[Optional[tuple[int, int]]],
) -> list[str]:
    assert 0 < len(cells) == len(widths) == len(align)
    height = max(len(c.lines) for c in cells)
    boxes = [
        c.box(w, height, a, v, n)
        for (c, w, a, v, n) in zip(cells, widths, align, valign, num_spacing)
    ]
    if not right_border_line and rstrip:
        boxes[-1] = cells[-1].box(0, height, align[-1], valign[-1], num_spacing[-1])
    return [
        left_border_line
        + left_padding
        + (right_padding + col_sep + left_padding).join(line_bits)
        + (right_padding if right_border_line or not rstrip else "")
        + right_border_line
        for line_bits in zip(*boxes)
    ]
