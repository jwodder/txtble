import pytest
from   txtble import Txtble, IndeterminateWidthError

BAD_STRING = '\033[31mRed\033[0m'

def test_indeterminate_cell():
    tbl = Txtble(
        headers=['Header', 'Header'],
        data=[['A', 'B'], [BAD_STRING, 'D']],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING

def test_indeterminate_header():
    tbl = Txtble(
        headers=['Header', BAD_STRING],
        data=[['A', 'B'], ['C', 'D']],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING

def test_indeterminate_header_fill():
    tbl = Txtble(
        headers=['Header'],
        header_fill=BAD_STRING,
        data=[['A', 'B'], ['C', 'D']],
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING

def test_indeterminate_row_fill():
    tbl = Txtble(
        headers=['Header', 'Header'],
        data=[['A', 'B'], ['C']],
        row_fill=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING

def test_indeterminate_none_str():
    tbl = Txtble(
        headers=['Header', 'Header'],
        data=[['A', 'B'], ['C', None]],
        none_str=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING

def test_indeterminate_padding():
    tbl = Txtble(
        headers=['Header', 'Header'],
        data=[['A', 'B'], ['C', 'D']],
        padding=BAD_STRING,
    )
    with pytest.raises(IndeterminateWidthError) as excinfo:
        str(tbl)
    assert excinfo.value.string == BAD_STRING
