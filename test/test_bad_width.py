import pytest
from   txtble import Txtble, IndeterminateWidthError

BAD_STRING = '\x01'
ERRMSG = repr(BAD_STRING) + ': string has indeterminate width'

@pytest.mark.parametrize('s', [
    '\x0E', '\x0F',  # altcharset on/off
    '\033[17;23H',   # move cursor
    '\a',            # bell
    '\b',            # backspace
    '!\b!', '_\bx',  # overstruck printing
    '\x7F',          # delete
    '\033[H\033[J',  # clear screen
    '\033[?1049h',   # altscreen on
    '\033[?1049l',   # altscreen off
])
def test_indeterminate_cell(s):
    tbl = Txtble(
        headers=['Header', 'Header'],
        data=[['A', 'B'], [s, 'D']],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == s
    assert str(excinfo.value) == repr(s) + ': string has indeterminate width'

def test_indeterminate_header():
    tbl = Txtble(
        headers=['Header', BAD_STRING],
        data=[['A', 'B'], ['C', 'D']],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG

def test_indeterminate_header_fill():
    tbl = Txtble(
        headers=['Header'],
        header_fill=BAD_STRING,
        data=[['A', 'B'], ['C', 'D']],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG

def test_indeterminate_row_fill():
    tbl = Txtble(
        headers=['Header', 'Header'],
        data=[['A', 'B'], ['C']],
        row_fill=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG

def test_indeterminate_none_str():
    tbl = Txtble(
        headers=['Header', 'Header'],
        data=[['A', 'B'], ['C', None]],
        none_str=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG

def test_indeterminate_padding():
    tbl = Txtble(
        headers=['Header', 'Header'],
        data=[['A', 'B'], ['C', 'D']],
        padding=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
    assert str(excinfo.value) == ERRMSG
