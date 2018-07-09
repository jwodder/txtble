import pytest
from   txtble import Txtble

@pytest.mark.parametrize('colored,plain', [
    ('\033[31mRed\033[0m', 'Red'),
    ('\033[31mRed\033[m', 'Red'),
    ('\033[3;1mIndeterminate\033[0m', 'Indeterminate'),
    ('\033[3;;1mIndeterminate\033[0m', 'Indeterminate'),
    ('\033[31mRed\033[0m and \033[32mGreen\033[0m', 'Red and Green'),
    ('An \033[4munderlined\033[m word', 'An underlined word'),
    ('Misplaced \033[0m sgr0', 'Misplaced  sgr0'),
    ('\033[32mGr\033[34mue\033[m', 'Grue'),
    ('\033[41mExtra\033[00m \033[05mzeroes\033[000m', 'Extra zeroes'),
])
def test_colored_text(colored, plain):
    tbl = Txtble(data=[[colored], [plain]])
    w = len(plain)
    assert str(tbl) == (
          '+' + '-' * w + '+\n'
        + '|' + colored + '|\n'
        + '|' + plain   + '|\n'
        + '+' + '-' * w + '+\n'
    )

def test_multiline_colors():
    tbl = Txtble([
        [
            'The \033[4mFlower\033[m Poem\n'
            'All of the \033[31mred\n'
            'flowers\033[m are very \033[01;32mbold\n'
            'green\033[0m, and the petals are \033[34mblue\033[46m\n'
            'on cyan\033[00m.  The \033[36mC\033[35mM\033[33mY\033[30mK\n'
            'of it all\033[m just \033[40;34;46;0;7mboggles\n'
            'the mind\033[0m.'
        ]
    ])
    assert str(tbl) == (
        '+------------------------------+\n'
        '|The \033[4mFlower\033[m Poem               |\n'
        '|All of the \033[31mred\033[m                |\n'
        '|\033[31mflowers\033[m are very \033[01;32mbold\033[m         |\n'
        '|\033[01;32mgreen\033[0m, and the petals are \033[34mblue\033[46m\033[m|\n'
        '|\033[34m\033[46mon cyan\033[00m.  The \033[36mC\033[35mM\033[33mY\033[30mK\033[m            |\n'
        '|\033[36m\033[35m\033[33m\033[30mof it all\033[m just \033[40;34;46;0;7mboggles\033[m        |\n'
        '|\033[40;34;46;0;7mthe mind\033[0m.                     |\n'
        '+------------------------------+'
    )
