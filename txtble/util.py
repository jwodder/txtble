import re
from   unicodedata import category
from   six         import PY2, integer_types, string_types, text_type, wraps
from   wcwidth     import wcswidth
from   .errors     import IndeterminateWidthError, UnterminatedColorError

COLOR_BEGIN_RGX = r'\033\[(?:[0-9;]*;)?[0-9]*[1-9][0-9]*m'
COLOR_END_RGX   = r'\033\[(?:[0-9;]*;)?0*m'

def join_cells(cells, widths, align, col_sep, border, rstrip, left_padding,
               right_padding):
    assert 0 < len(cells) == len(widths) == len(align)
    height = max(len(c.lines) for c in cells)
    boxes = [c.box(w, height, a) for (c,w,a) in zip(cells, widths, align)]
    if not border and rstrip:
        boxes[-1] = cells[-1].box(0, height, align[-1])
    return [
        border + left_padding
            + (right_padding + col_sep + left_padding).join(line_bits)
            + (right_padding if border or not rstrip else '') + border
        for line_bits in zip(*boxes)
    ]

def to_len(xs, length, fill):
    return (xs + [fill] * length)[:length]

def to_lines(s):
    """
    Like `str.splitlines()`, except that an empty string results in a
    one-element list and a trailing newline results in a trailing empty string
    (and all without re-implementing Python's changing line-splitting
    algorithm).

    >>> to_lines('')
    ['']
    >>> to_lines('\\n')
    ['', '']
    >>> to_lines('foo')
    ['foo']
    >>> to_lines('foo\\n')
    ['foo', '']
    >>> to_lines('foo\\nbar')
    ['foo', 'bar']
    >>> to_lines('foo\\fbar')
    ['foo', 'bar']
    >>> to_lines('foo\\vbar')
    ['foo', 'bar']
    """
    lines = s.splitlines(True)
    if not lines:
        return ['']
    if lines[-1].splitlines() != [lines[-1]]:
        lines.append('')
    for i,l in enumerate(lines):
        l2 = l.splitlines()
        assert len(l2) in (0,1)
        lines[i] = l2[0] if l2 else ''
    if PY2 and isinstance(s, str):
        # Manually split on \f and \v
        lines = [
            lf for l in lines
               for lv in l.split('\v')
               for lf in lv.split('\f')
        ]
    return lines

def strify(s):
    if not isinstance(s, string_types):
        s = str(s)
    if s and isinstance(s, text_type) and category(s[0]).startswith('M'):
        s = ' ' + s
    return s.expandtabs()

def mkpadding(s, len_func):
    if not s:
        padding = ''
    elif isinstance(s, integer_types):
        padding = ' ' * s
    else:
        padding = strify(s)
    if len_func(padding) < 0:
        raise IndeterminateWidthError(padding)
    if len(to_lines(padding)) > 1:
        raise ValueError('padding cannot contain newlines')
    return padding

def color_aware(f):
    """
    A function decorator for applying to `len` or imitators thereof that strips
    ANSI color sequences from a string before passing it on.  If any color
    sequences are not followed by a reset sequence, an `UnterminatedColorError`
    is raised.
    """
    @wraps(f)
    def colored_len(s):
        s2 = re.sub(
            COLOR_BEGIN_RGX + '(.*?)' + COLOR_END_RGX,
            lambda m: re.sub(COLOR_BEGIN_RGX, '', m.group(1)),
            s,
        )
        if re.search(COLOR_BEGIN_RGX, s2):
            raise UnterminatedColorError(s)
        return f(re.sub(COLOR_END_RGX, '', s2))
    return colored_len

strwidth = color_aware(wcswidth)

def carry_over_color(lines):
    """
    Given a sequence of lines, for each line that contains a ANSI color escape
    sequence without a reset, add a reset to the end of that line and copy all
    colors in effect at the end of it to the beginning of the next line.
    """
    lines2 = []
    in_effect = ''
    for s in lines:
        s = in_effect + s
        in_effect = ''
        m = re.search(COLOR_BEGIN_RGX + '(?:(?!' + COLOR_END_RGX + ').)*$', s)
        if m:
            s += '\033[m'
            in_effect = ''.join(re.findall(COLOR_BEGIN_RGX, m.group(0)))
        lines2.append(s)
    return lines2
