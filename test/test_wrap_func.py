import pytest
from   txtble      import Txtble, IndeterminateWidthError
from   txtble.util import strwidth

LONG_STRING = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit'

@pytest.mark.parametrize('break_long', [True, False])
@pytest.mark.parametrize('hyph_break', [True, False])
@pytest.mark.parametrize('len_func', [strwidth, len])
def test_wrap_func(mocker, break_long, hyph_break, len_func):
    wrap_func = mocker.Mock(return_value=['Mocked'])
    tbl = Txtble(
        [[LONG_STRING], ['Too short']],
        break_long_words = break_long,
        break_on_hyphens = hyph_break,
        len_func         = len_func,
        widths           = [20],
        wrap_func        = wrap_func,
    )
    assert str(tbl) == (
        '+--------------------+\n'
        '|Mocked              |\n'
        '|Too short           |\n'
        '+--------------------+'
    )
    wrap_func.assert_called_once_with(LONG_STRING, 20)

def test_wrap_func_multiline(mocker):
    wrap_func = mocker.Mock(return_value=['Mocked'])
    tbl = Txtble(
        [['Lorem ipsum\n' + LONG_STRING]],
        widths    = [20],
        wrap_func = wrap_func,
    )
    assert str(tbl) == (
        '+--------------------+\n'
        '|Lorem ipsum         |\n'
        '|Mocked              |\n'
        '+--------------------+'
    )
    wrap_func.assert_called_once_with(LONG_STRING, 20)

def test_split_wrap_func():
    tbl = Txtble([[LONG_STRING]], widths=[20], wrap_func=lambda s,w: s.split())
    assert str(tbl) == (
        '+--------------------+\n'
        '|Lorem               |\n'
        '|ipsum               |\n'
        '|dolor               |\n'
        '|sit                 |\n'
        '|amet,               |\n'
        '|consectetur         |\n'
        '|adipisicing         |\n'
        '|elit                |\n'
        '+--------------------+'
    )

@pytest.mark.parametrize('break_long', [True, False])
@pytest.mark.parametrize('hyph_break', [True, False])
def test_nonbreaking_wrap_func(break_long, hyph_break):
    tbl = Txtble(
        [[LONG_STRING]],
        break_long_words = break_long,
        break_on_hyphens = hyph_break,
        widths           = [20],
        wrap_func        = lambda s,w: [s],
    )
    assert str(tbl) == (
        '+--------------------------------------------------------+\n'
        '|Lorem ipsum dolor sit amet, consectetur adipisicing elit|\n'
        '+--------------------------------------------------------+'
    )

@pytest.mark.parametrize('break_long', [True, False])
@pytest.mark.parametrize('hyph_break', [True, False])
def test_nonbreaking_wrap_func_hyphenated(break_long, hyph_break):
    tbl = Txtble(
        [['Lorem-ipsum-dolor-sit-amet, consectetur-adipisicing-elit']],
        break_long_words = break_long,
        break_on_hyphens = hyph_break,
        widths           = [20],
        wrap_func        = lambda s,w: [s],
    )
    assert str(tbl) == (
        '+--------------------------------------------------------+\n'
        '|Lorem-ipsum-dolor-sit-amet, consectetur-adipisicing-elit|\n'
        '+--------------------------------------------------------+'
    )

@pytest.mark.parametrize('wrapped', [
    'Embedded\nnewline',
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
def test_indeterminate_width_wrap_func(wrapped):
    tbl = Txtble([[LONG_STRING]], widths=[20], wrap_func=lambda s,w: [wrapped])
    with pytest.raises(IndeterminateWidthError):
        str(tbl)

def test_wrap_func_tabbed_string(mocker):
    wrap_func = mocker.Mock(return_value=['Mocked'])
    tbl = Txtble(
        [['\tLorem\tipsum\tdolor\tsit\tamet\t']],
        widths    = [20],
        wrap_func = wrap_func,
    )
    assert str(tbl) == (
        '+--------------------+\n'
        '|Mocked              |\n'
        '+--------------------+'
    )
    wrap_func.assert_called_once_with(
        '\tLorem\tipsum\tdolor\tsit\tamet\t'.expandtabs(),
        20,
    )

def test_tabbing_wrap_func():
    tbl = Txtble(
        [['Lorem ipsum dolor sit amet']],
        widths    = [20],
        wrap_func = lambda s,w: [s.replace(' ', '\t')],
    )
    assert str(tbl) == (
        '+------------------------------------+\n'
        '|Lorem   ipsum   dolor   sit     amet|\n'
        '+------------------------------------+'
    )

@pytest.mark.parametrize('widths', [None, [None], [None, 20]])
def test_wrap_func_not_called(mocker, widths):
    wrap_func = mocker.stub()
    tbl = Txtble([[LONG_STRING]], widths=widths, wrap_func=wrap_func)
    assert str(tbl) == (
        '+--------------------------------------------------------+\n'
        '|Lorem ipsum dolor sit amet, consectetur adipisicing elit|\n'
        '+--------------------------------------------------------+'
    )
    assert not wrap_func.called

def test_split_running_color():
    tbl = Txtble(
        [
            [
                '\033[31mLorem'
                ' \033[32mipsum'
                ' \033[33mdolor'
                ' \033[34msit \033[35mamet,'
                ' \033[36mconsectetur'
                ' \033[41madipisicing'
                ' \033[42melit\033[m'
            ]
        ],
        widths    = [20],
        wrap_func = lambda s,w: s.split(),
    )
    assert str(tbl) == (
        '+--------------------+\n'
        '|\033[31mLorem\033[m               |\n'
        '|\033[31m\033[32mipsum\033[m               |\n'
        '|\033[31m\033[32m\033[33mdolor\033[m               |\n'
        '|\033[31m\033[32m\033[33m\033[34msit\033[m                 |\n'
        '|\033[31m\033[32m\033[33m\033[34m\033[35mamet,\033[m               |\n'
        '|\033[31m\033[32m\033[33m\033[34m\033[35m\033[36mconsectetur\033[m         |\n'
        '|\033[31m\033[32m\033[33m\033[34m\033[35m\033[36m\033[41madipisicing\033[m         |\n'
        '|\033[31m\033[32m\033[33m\033[34m\033[35m\033[36m\033[41m\033[42melit\033[m                |\n'
        '+--------------------+'
    )
