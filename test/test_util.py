from __future__ import annotations
import pytest
from txtble.util import to_lines


@pytest.mark.parametrize(
    "s,lines",
    [
        ("", [""]),
        ("\n", ["", ""]),
        ("foo", ["foo"]),
        ("foo\n", ["foo", ""]),
        ("foo\nbar", ["foo", "bar"]),
        ("foo\fbar", ["foo", "bar"]),
        ("foo\vbar", ["foo", "bar"]),
    ],
)
def test_to_lines(s: str, lines: list[str]) -> None:
    assert to_lines(s) == lines
