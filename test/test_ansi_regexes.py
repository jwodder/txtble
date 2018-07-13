import re
import pytest
from   txtble.util import COLOR_BEGIN_RGX, COLOR_END_RGX

BEGIN_COLORS = [
    '\033[31m',
    '\033[4;1m',
    '\033[04;01m',
    '\033[4;;1m',
    '\033[0;31m',
    '\033[;31m',
]

END_COLORS = [
    '\033[m',
    '\033[0m',
    '\033[00m',
    '\033[000m',
    '\033[31;0m',
    '\033[31;m',
    '\033[;m',
    '\033[;31;m',
]

NOT_COLORS = [
    '\033[1[m',
    '\033;1m',
    u'\033[\u0661m',
]

@pytest.mark.parametrize('s', BEGIN_COLORS)
def test_color_begin_rgx(s):
    assert bool(re.match('^' + COLOR_BEGIN_RGX + '$', s))

@pytest.mark.parametrize('s', END_COLORS)
def test_color_end_rgx(s):
    assert bool(re.match('^' + COLOR_END_RGX + '$', s))

@pytest.mark.parametrize('s', NOT_COLORS + END_COLORS)
def test_bad_color_begin_rgx(s):
    assert re.match('^' + COLOR_BEGIN_RGX + '$', s) is None

@pytest.mark.parametrize('s', NOT_COLORS + BEGIN_COLORS)
def test_bad_color_end_rgx(s):
    assert re.match('^' + COLOR_END_RGX + '$', s) is None
