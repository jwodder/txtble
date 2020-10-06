from   functools     import wraps
from   itertools     import cycle
import re
from   typing        import Any, Callable, Iterable, List, TypeVar
from   unicodedata   import category
from   wcwidth       import wcswidth
from   .border_style import BorderStyle
from   .errors       import IndeterminateWidthError, UnterminatedColorError

LenFunc = Callable[[str], int]

T = TypeVar("T")

COLOR_BEGIN_RGX = r'\033\[(?:[0-9;]*;)?[0-9]*[1-9][0-9]*m'
COLOR_END_RGX   = r'\033\[(?:[0-9;]*;)?0*m'

def to_len(xs: List[T], length: int, fill: T) -> List[T]:
    return (xs + [fill] * length)[:length]

def to_lines(s: str) -> List[str]:
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
    for i,ln in enumerate(lines):
        l2 = ln.splitlines()
        assert len(l2) in (0,1)
        lines[i] = l2[0] if l2 else ''
    return lines

def strify(s: Any) -> str:
    if not isinstance(s, str):
        s2 = str(s)
    else:
        s2 = s
    if s2 and category(s2[0]).startswith('M'):
        s2 = ' ' + s2
    return s2.expandtabs()

def mkpadding(s: Any, len_func: LenFunc) -> str:
    if not s:
        padding = ''
    elif isinstance(s, int):
        padding = ' ' * s
    else:
        padding = strify(s)
    if len(to_lines(padding)) > 1:
        raise ValueError('padding cannot contain newlines')
    if len_func(padding) < 0:
        raise IndeterminateWidthError(padding)
    return padding

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
            COLOR_BEGIN_RGX + '(.*?)' + COLOR_END_RGX,
            lambda m: re.sub(COLOR_BEGIN_RGX, '', m.group(1)),
            s,
        )
        if re.search(COLOR_BEGIN_RGX, s2):
            raise UnterminatedColorError(s)
        return f(re.sub(COLOR_END_RGX, '', s2))
    return colored_len

strwidth: LenFunc = with_color_stripped(wcswidth)

def carry_over_color(lines: Iterable[str]) -> List[str]:
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

def wrap(
    s: str,
    width: int,
    len_func: LenFunc = strwidth,
    break_long_words: bool = True,
    break_on_hyphens: bool = True,
) -> List[str]:
    def length(ss: str) -> int:
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
                    raise AssertionError('Unreachable state reached')  # pragma: no cover
                wrapped.append(pre)
                s = post
            else:
                # Break at the first hyphen or space, if any
                m2 = re.search(break_point, s)
                if m2:
                    wrapped.append(s[:m2.end()].rstrip(' '))
                    s = s[m2.end():]
                else:
                    # `s` is just one long, unbreakable word; break out of
                    # the `for` loop
                    break
    wrapped.append(s)
    return wrapped

def breakable_units(s: str) -> List[str]:
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

def first_style(*args: Any) -> BorderStyle:
    for a in args:
        if isinstance(a, BorderStyle):
            return a
    raise TypeError('border_style must be a BorderStyle instance')
