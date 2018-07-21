from   itertools     import cycle
import re
from   unicodedata   import category
from   six           import PY2, integer_types, string_types, text_type, wraps
from   wcwidth       import wcswidth
from   .border_style import BorderStyle
from   .errors       import IndeterminateWidthError, UnterminatedColorError

COLOR_BEGIN_RGX = r'\033\[(?:[0-9;]*;)?[0-9]*[1-9][0-9]*m'
COLOR_END_RGX   = r'\033\[(?:[0-9;]*;)?0*m'

def join_cells(cells, widths, align, col_sep, left_border_line,
               right_border_line, rstrip, left_padding, right_padding):
    assert 0 < len(cells) == len(widths) == len(align)
    height = max(len(c.lines) for c in cells)
    boxes = [c.box(w, height, a) for (c,w,a) in zip(cells, widths, align)]
    if not right_border_line and rstrip:
        boxes[-1] = cells[-1].box(0, height, align[-1])
    return [
        left_border_line + left_padding
            + (right_padding + col_sep + left_padding).join(line_bits)
            + (right_padding if right_border_line or not rstrip else '')
            + right_border_line
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

def with_color_stripped(f):
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

strwidth = with_color_stripped(wcswidth)

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

def wrap(s, width, len_func=strwidth, break_long_words=True,
                                      break_on_hyphens=True):
    def length(ss):
        try:
            return len_func(ss)
        except UnterminatedColorError:
            # Appending sgr0 unconditionally is the wrong thing to do when
            # len_func is set to, say, the builtin `len`.
            return len_func(ss + '\033[m')
    if not s:
        return [s]
    wrapped = []
    break_point = r'-| +' if break_on_hyphens else r' +'
    while length(s) > width:
        for m in reversed(list(re.finditer(break_point, s))):
            pre = s[:m.end()].rstrip(' ')
            post = s[m.end():]
            assert not re.search(r'\033[^m]*$', pre), \
                'Space or hyphen inside ANSI sequence'
                ### XXX: Problem: What if a custom len_func accepts ESC not
                ### followed by 'm'?
            if 0 <= length(pre) <= width:
                wrapped.append(pre)
                s = post
                break
        else:
            if break_long_words:
                # Do a binary search on valid breakpoints until we find the
                # longest initial substring shorter than `width`
                units = breakable_units(s)
                low = 0
                high = len(units)
                while low < high:
                    i = (low + high) // 2
                    pre = ''.join(units[:i])
                    post = ''.join(units[i:])
                    w = length(pre)
                    if w < 0:
                        raise IndeterminateWidthError(s)
                    elif w < width:
                        if length(''.join(units[:i+1])) > width:
                            break
                        else:
                            low = i+1
                    elif w == width:
                        break
                    else:
                        assert w > width
                        high = i
                else:
                    assert False  # pragma: no cover
                wrapped.append(pre)
                s = post
            else:
                # Break at the first hyphen or space, if any
                m = re.search(break_point, s)
                if m:
                    wrapped.append(s[:m.end()].rstrip(' '))
                    s = s[m.end():]
                else:
                    # `s` is just one long, unbreakable word; break out of
                    # the `for` loop
                    break
    wrapped.append(s)
    return wrapped

def breakable_units(s):
    """
    Break a string into a list of substrings, breaking at each point that it is
    permissible for `wrap(..., break_long_words=True)` to break; i.e., _not_
    breaking in the middle of ANSI color escape sequences.
    """
    units = []
    for run, color in zip(
        re.split('(' + COLOR_BEGIN_RGX + '|' + COLOR_END_RGX + ')', s),
        cycle([False, True]),
    ):
        if color:
            units.append(run)
        else:
            ### TODO: Keep combining characters together
            units.extend(run)
    return units

def first_style(*args):
    for a in args:
        if isinstance(a, BorderStyle):
            return a
    raise TypeError('border_style must be a BorderStyle instance')
