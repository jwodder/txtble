from __future__ import annotations
from collections.abc import Callable, Iterable
from functools import wraps
from itertools import cycle
import re
import typing as ty
from typing import Any, TypeVar
from unicodedata import category
from wcwidth import wcswidth
from .border_style import BorderStyle
from .errors import UnterminatedColorError

LenFunc = ty.Callable[[str], int]

T = TypeVar("T")

COLOR_BEGIN_RGX = r"\033\[(?:[0-9;]*;)?[0-9]*[1-9][0-9]*m"
COLOR_END_RGX = r"\033\[(?:[0-9;]*;)?0*m"


def to_len(xs: list[T], length: int, fill: T) -> list[T]:
    return (xs + [fill] * length)[:length]


def to_lines(s: str) -> list[str]:
    """
    Like `str.splitlines()`, except that an empty string results in a
    one-element list and a trailing newline results in a trailing empty string
    (and all without re-implementing Python's changing line-splitting
    algorithm).
    """
    lines = s.splitlines(True)
    if not lines:
        return [""]
    if lines[-1].splitlines() != [lines[-1]]:
        lines.append("")
    for i, ln in enumerate(lines):
        l2 = ln.splitlines()
        assert len(l2) in (0, 1)
        lines[i] = l2[0] if l2 else ""
    return lines


def strify(s: Any) -> str:
    if not isinstance(s, str):
        s2 = str(s)
    else:
        s2 = s
    if s2 and category(s2[0]).startswith("M"):
        s2 = " " + s2
    return s2.expandtabs()


def with_color_stripped(f: Callable[[str], T]) -> Callable[[str], T]:
    """
    A function decorator for applying to `len` or imitators thereof that strips
    ANSI color sequences from a string before passing it on.  If any color
    sequences are not followed by a reset sequence, an `UnterminatedColorError`
    is raised.
    """

    @wraps(f)
    def colored_len(s: str) -> T:
        s2 = re.sub(
            COLOR_BEGIN_RGX + "(.*?)" + COLOR_END_RGX,
            lambda m: re.sub(COLOR_BEGIN_RGX, "", m.group(1)),
            s,
        )
        if re.search(COLOR_BEGIN_RGX, s2):
            raise UnterminatedColorError(s)
        return f(re.sub(COLOR_END_RGX, "", s2))

    return colored_len


strwidth: LenFunc = with_color_stripped(wcswidth)


def carry_over_color(lines: Iterable[str]) -> list[str]:
    """
    Given a sequence of lines, for each line that contains a ANSI color escape
    sequence without a reset, add a reset to the end of that line and copy all
    colors in effect at the end of it to the beginning of the next line.
    """
    lines2 = []
    in_effect = ""
    for s in lines:
        s = in_effect + s
        in_effect = ""
        m = re.search(COLOR_BEGIN_RGX + "(?:(?!" + COLOR_END_RGX + ").)*$", s)
        if m:
            s += "\033[m"
            in_effect = "".join(re.findall(COLOR_BEGIN_RGX, m.group(0)))
        lines2.append(s)
    return lines2


def breakable_units(s: str) -> list[str]:
    """
    Break a string into a list of substrings, breaking at each point that it is
    permissible for `Txtble.wrap(..., break_long_words=True)` to break; i.e.,
    _not_ breaking in the middle of ANSI color escape sequences.
    """
    units = []
    for run, color in zip(
        re.split("(" + COLOR_BEGIN_RGX + "|" + COLOR_END_RGX + ")", s),
        cycle([False, True]),
    ):
        if color:
            units.append(run)
        else:
            ### TODO: Keep combining characters together
            units.extend(run)
    return units


def first_style(*args: Any) -> BorderStyle:
    for a in args:
        if isinstance(a, BorderStyle):
            return a
    raise TypeError("border_style must be a BorderStyle instance")
