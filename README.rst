.. image:: http://www.repostatus.org/badges/latest/active.svg
    :target: http://www.repostatus.org/#active
    :alt: Project Status: Active — The project has reached a stable, usable
          state and is being actively developed.

.. image:: https://travis-ci.org/jwodder/txtble.svg?branch=master
    :target: https://travis-ci.org/jwodder/txtble

.. image:: https://codecov.io/gh/jwodder/txtble/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jwodder/txtble

.. image:: https://img.shields.io/pypi/pyversions/txtble.svg
    :target: https://pypi.org/project/txtble/

.. image:: https://img.shields.io/github/license/jwodder/txtble.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/jwodder

`GitHub <https://github.com/jwodder/txtble>`_
| `PyPI <https://pypi.org/project/txtble/>`_
| `Issues <https://github.com/jwodder/txtble/issues>`_
| `Changelog <https://github.com/jwodder/txtble/blob/master/CHANGELOG.md>`_

.. contents::
    :backlinks: top

``txtble`` is yet another Python library for creating plain-text tables.  (All
the good names were taken, OK?)  Pass in a list of lists of strings (or other
stringable things) and get out something nice like::

    +---------+----------+------------------+
    |Month    |Birthstone|Birth Flower      |
    +---------+----------+------------------+
    |January  |Garnet    |Carnation         |
    |February |Amethyst  |Violet            |
    |March    |Aquamarine|Jonquil           |
    |April    |Diamond   |Sweetpea          |
    |May      |Emerald   |Lily Of The Valley|
    |June     |Pearl     |Rose              |
    |July     |Ruby      |Larkspur          |
    |August   |Peridot   |Gladiolus         |
    |September|Sapphire  |Aster             |
    |October  |Opal      |Calendula         |
    |November |Topaz     |Chrysanthemum     |
    |December |Turquoise |Narcissus         |
    +---------+----------+------------------+

Features:

- Rows can be passed as lists or `dict`\ s
- ANSI color aware
- Unicode fullwidth & combining character aware
- Control the horizontal (left, center, & right) and vertical (top, middle, &
  bottom) alignment of text
- Align numbers along their decimal points
- Customize characters used for drawing borders
- Toggle inter-row, inter-column, and outer borders
- Set the value used to fill out ragged rows
- Pad cells on the left & right
- Set column widths, with long lines wrapped to fit
- Configure how `None` values are displayed


Installation
============
Just use `pip <https://pip.pypa.io>`_ (You have pip, right?) to install
``txtble`` and its dependencies::

    pip install txtble


Examples
========

Construct & show a basic table::

    >>> from txtble import Txtble
    >>> # Taken from /usr/share/misc/birthtoken.gz in Ubuntu Xenial's miscfiles package:
    >>> HEADERS = ['Month', 'Birthstone', 'Birth Flower']
    >>> DATA = [
    ...     ['January',   'Garnet',     'Carnation'],
    ...     ['February',  'Amethyst',   'Violet'],
    ...     ['March',     'Aquamarine', 'Jonquil'],
    ...     ['April',     'Diamond',    'Sweetpea'],
    ...     ['May',       'Emerald',    'Lily Of The Valley'],
    ...     ['June',      'Pearl',      'Rose'],
    ...     ['July',      'Ruby',       'Larkspur'],
    ...     ['August',    'Peridot',    'Gladiolus'],
    ...     ['September', 'Sapphire',   'Aster'],
    ...     ['October',   'Opal',       'Calendula'],
    ...     ['November',  'Topaz',      'Chrysanthemum'],
    ...     ['December',  'Turquoise',  'Narcissus'],
    ... ]
    >>> tbl = Txtble(DATA, headers=HEADERS)
    >>> print(tbl)
    +---------+----------+------------------+
    |Month    |Birthstone|Birth Flower      |
    +---------+----------+------------------+
    |January  |Garnet    |Carnation         |
    |February |Amethyst  |Violet            |
    |March    |Aquamarine|Jonquil           |
    |April    |Diamond   |Sweetpea          |
    |May      |Emerald   |Lily Of The Valley|
    |June     |Pearl     |Rose              |
    |July     |Ruby      |Larkspur          |
    |August   |Peridot   |Gladiolus         |
    |September|Sapphire  |Aster             |
    |October  |Opal      |Calendula         |
    |November |Topaz     |Chrysanthemum     |
    |December |Turquoise |Narcissus         |
    +---------+----------+------------------+

The table can also be constructed like this::

    >>> tbl = Txtble(headers=HEADERS)
    >>> tbl.extend(DATA)

Or like this::

    >>> tbl = Txtble(headers=HEADERS)
    >>> for row in DATA:
    ...     tbl.append(row)

Or even like this::

    >>> tbl = Txtble(DATA)
    >>> tbl.headers = HEADERS

The rows of the table can be lists of values (as seen above) or `dict`\ s that
map header names to values::

    >>> tbl = Txtble(
    ...     headers = ["Red", "Green", "Blue"],
    ...     data    = [
    ...         {"Red": "Ruby", "Green": "Emerald", "Blue": "Sapphire"},
    ...         {"Red": "Fire", "Green": "Earth",   "Blue": "Water"},
    ...     ],
    ... )
    >>> print(tbl)
    +----+-------+--------+
    |Red |Green  |Blue    |
    +----+-------+--------+
    |Ruby|Emerald|Sapphire|
    |Fire|Earth  |Water   |
    +----+-------+--------+

Missing `dict` keys can be filled in with the ``dict_fill`` option (Without it,
you'd get a `KeyError` here)::

    >>> tbl = Txtble(
    ...     headers = ["Red", "Green", "Blue"],
    ...     data    = [
    ...         {"Red": "Ruby", "Green": "Emerald", "Blue": "Sapphire"},
    ...         {"Red": "Fire", "Green": "Earth",   "Blue": "Water"},
    ...         {"Red": "Hot",                      "Blue": "Cold"},
    ...     ],
    ...     dict_fill = 'UNKNOWN',
    ... )
    >>> print(tbl)
    +----+-------+--------+
    |Red |Green  |Blue    |
    +----+-------+--------+
    |Ruby|Emerald|Sapphire|
    |Fire|Earth  |Water   |
    |Hot |UNKNOWN|Cold    |
    +----+-------+--------+

The number of columns is automatically set to the length of the longest row::

    >>> tbl = Txtble([
    ...     ['1', '1'],
    ...     ['Z_6', '1', 'x', 'x^2', 'x^3', 'x^4', 'x^5'],
    ...     ['S_3', '1', 'a', 'b', 'aba', 'ba', 'ab'],
    ...     ['Z_4', '1', 'x', 'x^2', 'x^3'],
    ...     ['V_4', '1', 'a', 'b', 'ab'],
    ... ])
    >>> print(tbl)
    +---+-+-+---+---+---+---+
    |1  |1| |   |   |   |   |
    |Z_6|1|x|x^2|x^3|x^4|x^5|
    |S_3|1|a|b  |aba|ba |ab |
    |Z_4|1|x|x^2|x^3|   |   |
    |V_4|1|a|b  |ab |   |   |
    +---+-+-+---+---+---+---+

... unless you've specified a header row, which puts a limit on the number of
columns::

    >>> tbl.headers = ['Group', 'Elements']
    >>> print(tbl)
    +-----+--------+
    |Group|Elements|
    +-----+--------+
    |1    |1       |
    |Z_6  |1       |
    |S_3  |1       |
    |Z_4  |1       |
    |V_4  |1       |
    +-----+--------+

... unless you've *also* specified a ``header_fill`` to use as the header for
extra columns::

    >>> tbl.header_fill = 'Extra!'
    >>> print(tbl)
    +-----+--------+------+------+------+------+------+
    |Group|Elements|Extra!|Extra!|Extra!|Extra!|Extra!|
    +-----+--------+------+------+------+------+------+
    |1    |1       |      |      |      |      |      |
    |Z_6  |1       |x     |x^2   |x^3   |x^4   |x^5   |
    |S_3  |1       |a     |b     |aba   |ba    |ab    |
    |Z_4  |1       |x     |x^2   |x^3   |      |      |
    |V_4  |1       |a     |b     |ab    |      |      |
    +-----+--------+------+------+------+------+------+

You can set the widths of columns; long lines will be wrapped to fit::

    >>> tbl = Txtble(
    ...     headers=['Short Text', 'Long Text'],
    ...     data=[
    ...         [
    ...             'Hi there!',
    ...             'Lorem ipsum dolor sit amet, consectetur adipisicing elit',
    ...         ]
    ...     ],
    ...     widths=[20, 20],
    ... )
    >>> print(tbl)
    +--------------------+--------------------+
    |Short Text          |Long Text           |
    +--------------------+--------------------+
    |Hi there!           |Lorem ipsum dolor   |
    |                    |sit amet,           |
    |                    |consectetur         |
    |                    |adipisicing elit    |
    +--------------------+--------------------+

You can align column text to the left, right, or center::

    >>> tbl = Txtble(DATA, headers=HEADERS, align=['r', 'c', 'l'])
    >>> print(tbl)
    +---------+----------+------------------+
    |    Month|Birthstone|Birth Flower      |
    +---------+----------+------------------+
    |  January|  Garnet  |Carnation         |
    | February| Amethyst |Violet            |
    |    March|Aquamarine|Jonquil           |
    |    April| Diamond  |Sweetpea          |
    |      May| Emerald  |Lily Of The Valley|
    |     June|  Pearl   |Rose              |
    |     July|   Ruby   |Larkspur          |
    |   August| Peridot  |Gladiolus         |
    |September| Sapphire |Aster             |
    |  October|   Opal   |Calendula         |
    | November|  Topaz   |Chrysanthemum     |
    | December|Turquoise |Narcissus         |
    +---------+----------+------------------+

Numbers in the same column can be aligned on their decimal point with the
``'n'`` alignment::

    >>> tbl = Txtble(
    ...     headers=['Thing', 'Value'],
    ...     data=[
    ...         ['Foo', 12345],
    ...         ['Bar', 1234.5],
    ...         ['Baz', 123.45],
    ...         ['Quux', 12.345],
    ...         ['Glarch', 1.2345],
    ...         ['Gnusto', .12345],
    ...     ],
    ...     align=['l', 'n'],
    ... )
    >>> print(tbl)
    +------+-----------+
    |Thing |Value      |
    +------+-----------+
    |Foo   |12345      |
    |Bar   | 1234.5    |
    |Baz   |  123.45   |
    |Quux  |   12.345  |
    |Glarch|    1.2345 |
    |Gnusto|    0.12345|
    +------+-----------+

Unicode works too, even fullwidth characters and combining characters::

    >>> tbl = Txtble(
    ...     headers=['Wide', 'Accented'],
    ...     data=[
    ...         [
    ...             u'\uFF37\uFF49\uFF44\uFF45',
    ...             u'A\u0301c\u0301c\u0301e\u0301n\u0301t\u0301e\u0301d\u0301',
    ...         ]
    ...     ]
    ... )
    >>> print(tbl.show())
    +--------+--------+
    |Wide    |Accented|
    +--------+--------+
    |Ｗｉｄｅ|Áććéńt́éd́|
    +--------+--------+

You can configure the borders and make them fancy::

    >>> from txtble import ASCII_EQ_BORDERS
    >>> tbl = Txtble(
    ...     DATA,
    ...     headers       = HEADERS,
    ...     header_border = ASCII_EQ_BORDERS,
    ...     row_border    = True,
    ... )
    >>> print(tbl)
    +---------+----------+------------------+
    |Month    |Birthstone|Birth Flower      |
    +=========+==========+==================+
    |January  |Garnet    |Carnation         |
    +---------+----------+------------------+
    |February |Amethyst  |Violet            |
    +---------+----------+------------------+
    |March    |Aquamarine|Jonquil           |
    +---------+----------+------------------+
    |April    |Diamond   |Sweetpea          |
    +---------+----------+------------------+
    |May      |Emerald   |Lily Of The Valley|
    +---------+----------+------------------+
    |June     |Pearl     |Rose              |
    +---------+----------+------------------+
    |July     |Ruby      |Larkspur          |
    +---------+----------+------------------+
    |August   |Peridot   |Gladiolus         |
    +---------+----------+------------------+
    |September|Sapphire  |Aster             |
    +---------+----------+------------------+
    |October  |Opal      |Calendula         |
    +---------+----------+------------------+
    |November |Topaz     |Chrysanthemum     |
    +---------+----------+------------------+
    |December |Turquoise |Narcissus         |
    +---------+----------+------------------+

... or *very* fancy::

    >>> from txtble import DOUBLE_BORDERS
    >>> tbl = Txtble(DATA, headers=HEADERS, border_style=DOUBLE_BORDERS)
    >>> print(tbl.show())
    ╔═════════╦══════════╦══════════════════╗
    ║Month    ║Birthstone║Birth Flower      ║
    ╠═════════╬══════════╬══════════════════╣
    ║January  ║Garnet    ║Carnation         ║
    ║February ║Amethyst  ║Violet            ║
    ║March    ║Aquamarine║Jonquil           ║
    ║April    ║Diamond   ║Sweetpea          ║
    ║May      ║Emerald   ║Lily Of The Valley║
    ║June     ║Pearl     ║Rose              ║
    ║July     ║Ruby      ║Larkspur          ║
    ║August   ║Peridot   ║Gladiolus         ║
    ║September║Sapphire  ║Aster             ║
    ║October  ║Opal      ║Calendula         ║
    ║November ║Topaz     ║Chrysanthemum     ║
    ║December ║Turquoise ║Narcissus         ║
    ╚═════════╩══════════╩══════════════════╝

See the following documentation for more information:


API
===

``Txtble``
----------

``Txtble(data=(), **kwargs)``
   Create a new ``Txtble`` object.  The table's data may be passed to the
   constructor as an iterable of rows of values, where each row is either an
   iterable of cell values or a mapping from header names to cell values;
   otherwise, the data starts out empty.  In either case, further data rows can
   be added via the ``append()`` and ``extend()`` methods.

   ``**kwargs`` are used to configure the ``Txtble`` instance; see
   "`Configuration Options <configuration_options_>`_" below.

``tbl.append(row)``
   Add a new data row at the bottom of the table.  ``row`` can be either an
   iterable of cell values or a mapping from header names to cell values.

``tbl.extend(rows)``
   Add zero or more new data rows at the bottom of the table

``tbl.show()`` or ``str(tbl)``
   Convert the ``Txtble`` instance to a string showing a plain text table.
   Table cells and filler values that are not already strings are converted by
   calling `str()` on them; the exceptions are `None` values, which are
   displayed according to the ``none_str`` option (see below).  All tab
   characters are expanded to spaces before building the table.  If any of the
   resulting strings have indeterminate width (i.e., if ``wcwidth.wcswidth()``
   returns a negative number for any of them), an ``IndeterminateWidthError``
   (a subclass of `ValueError`) is raised.

   Note that the resulting string will likely contain one or more embedded
   newlines, but (outside of some very odd cases) it will not end with a
   newline.  This means that you can do ``print(tbl)`` and there won't be a
   blank line added at the end.

   In Python 2, ``unicode(tbl)`` is like ``str(tbl)``, except it produces a
   `unicode` value.  This is necessary if one or more table cells are
   `unicode`.


.. _configuration_options:

Configuration Options
---------------------
These options can be set either as keywords passed to the ``Txtble``
constructor or as attributes on a ``Txtble`` instance::

    tbl = Txtble(data, border=False)
    # Same as:
    tbl = Txtble(data)
    tbl.border = False

``align=()``
   A sequence of alignment specifiers indicating how the contents of each
   column, in order, should be horizontally aligned.  The alignment specifiers
   are ``'l'`` (left alignment), ``'c'`` (centered alignment), and ``'r'``
   (right alignment).  ``align`` may optionally be set to a single alignment
   specifier to cause all columns to be aligned in that way.

   An alignment specifier may optionally include ``'n'`` to cause all numbers
   in the relevant column to be aligned on their decimal point; the ``'l'``,
   ``'c'``, or ``'r'`` then determines how the "block" of numbers is aligned as
   a whole (This is generally only relevant if the column also contains a
   string value longer than any of the numbers).  An alignment specifier of
   just ``'n'`` is equivalent to ``'ln'`` or ``'nl'``.

``align_fill='l'``
   If there are more columns than there are entries in ``align``, the extra
   columns will have their alignment set to ``align_fill``.

``border=True``
   Whether to draw a border around the edge of the table.  ``border`` may
   optionally be set to a ``BorderStyle`` instance to set the characters used
   for drawing the border around the edge of the table.  Individual edges can
   be toggled or stylized by setting the ``bottom_border``, ``left_border``,
   ``right_border``, and ``top_border`` options.

``border_style=ASCII_BORDERS``
   A ``BorderStyle`` instance specifying the characters to use for drawing all
   of the table's borders & rules.  The border style can be overridden for
   individual borders by setting their respective options (``border``,
   ``column_border``, etc.) to ``BorderStyle`` instances.  See "`BorderStyle
   <borderstyle_>`_" below for more information.

``bottom_border=None``
   Whether to draw a border along the bottom edge of the table.  The default
   value of `None` means to inherit the value set for ``border``.
   ``bottom_border`` may optionally be set to a ``BorderStyle`` instance to set
   the characters used for drawing the border along the bottom edge.

``break_long_words=True``
   Whether to force a line break in the middle of a word if said word is too
   long for the column's width

``break_on_hyphens=True``
   Whether to break on hyphens in addition to whitespace when wrapping text

``column_border=True``
   Whether to draw a vertical rule between individual columns.
   ``column_border`` may optionally be set to a ``BorderStyle`` instance to set
   the characters used for drawing the vertical rules between columns.

``columns=None``
   An optional positive integer.  When set, show exactly the given number of
   columns per row, adding cells with ``row_fill`` and discarding extra cells
   as needed.  If ``headers`` is also set, its length must equal ``columns`` or
   else a `ValueError` is raised.  Setting both ``columns`` and ``headers``
   causes ``header_fill`` to be ignored.

``dict_fill``
   If a header name does not appear as a key in a `dict`/mapping row, the value
   of ``dict_fill`` will be used for the corresponding cell value.  If
   ``dict_fill`` is not set, a missing key will cause a ``KeyError`` to be
   raised.

``header_border=None``
   Whether to draw a horizontal rule above the data rows, below the header row
   (if any).  The default value of `None` means that the border will be drawn
   if & only if ``headers`` is non-`None`.  ``header_border`` may optionally be
   set to a ``BorderStyle`` instance to set the characters used for drawing the
   horizontal rule above the data rows.

   If ``headers`` is `None` and ``top_border`` is set to a true value (or
   inherits a true value from ``border``), the header border will not be drawn.

``header_fill=None``
   When ``headers`` is non-`None` and ``columns`` is `None`, this option
   determines how rows with more columns than there are headers are handled.
   When ``header_fill=None``, any extra columns are discarded from long rows.
   For all other values, the header row will be extended to the length of the
   longest data row, and the new header cells will contain the ``header_fill``
   value.

``headers=None``
   An optional list of cell values to display in a row at the top of the table.
   Setting this option also implicitly sets a minimum number of columns per
   row; see ``header_fill`` for allowing extra columns.

   If ``headers`` is set to an empty list, ``header_fill`` must be set to a
   non-`None` value or else a `ValueError` will be raised upon trying to render
   the ``Txtble``.

``left_border=None``
   Whether to draw a border along the left edge of the table.  The default
   value of `None` means to inherit the value set for ``border``.
   ``left_border`` may optionally be set to a ``BorderStyle`` instance to set
   the characters used for drawing the border along the left edge.

``left_padding=None``
   Padding to insert on the left of every table cell.  This can be either an
   integer (to insert that many space characters) or a string.  If a string, it
   may not contain any newlines.  The default value of `None` means to inherit
   the value set for ``padding``.

``len_func``
   The function to use for calculating how many terminal cells wide a string
   is; it should take one string argument and return a width.  Returning a
   negative width causes ``Txtble`` to raise an ``IndeterminateWidthError``.
   The default value is ``with_color_stripped(wcwidth.wcswidth)`` (See "`Other
   <other_>`_" below).

``none_str=''``
   The string to display in place of `None` values (Setting ``none_str=None``
   is the same as setting it to ``'None'``)

``padding=0``
   Padding to insert on the left & right of every table cell.  This can be
   either an integer (to insert that many space characters) or a string.  If a
   string, it may not contain any newlines.  Padding for the left and right of
   table cells can be specified separately via the ``left_padding`` and
   ``right_padding`` options.

``right_border=None``
   Whether to draw a border along the right edge of the table.  The default
   value of `None` means to inherit the value set for ``border``.
   ``right_border`` may optionally be set to a ``BorderStyle`` instance to set
   the characters used for drawing the border along the right edge.

``right_padding=None``
   Padding to insert on the right of every table cell.  This can be either an
   integer (to insert that many space characters) or a string.  If a string, it
   may not contain any newlines.  The default value of `None` means to inherit
   the value set for ``padding``.

``row_border=False``
   Whether to draw horizontal rules between data rows.  ``row_border`` may
   optionally be set to a ``BorderStyle`` instance to set the characters used
   for drawing the horizontal rules between data rows.

``row_fill=''``
   If the rows of a table differ in number of columns, cells are added to the
   shorter rows until they all line up, and the added cells contain
   ``row_fill`` as their value.

``rstrip=True``
   When ``border=False``, setting ``rstrip=False`` will cause the last cell of
   each row to still be padded with trailing whitespace and ``padding`` in
   order to reach the full column width.  (Normally, this whitespace and
   ``padding`` is omitted when ``border=False`` as there is no end-of-line
   border to align.)  This option is useful if you wish to append text to one
   or more lines of the output and have it appear strictly outside the table.

``top_border=None``
   Whether to draw a border along the top edge of the table.  The default value
   of `None` means to inherit the value set for ``border``.  ``top_border`` may
   optionally be set to a ``BorderStyle`` instance to set the characters used
   for drawing the border along the top edge.

``valign=()``
   A sequence of vertical alignment specifiers indicating how the contents of
   each column, in order, should be vertically aligned.  The vertical alignment
   specifiers are ``'t'`` (top alignment), ``'m'`` (middle alignment), and
   ``'b'`` (bottom alignment).  ``valign`` may optionally be set to a single
   vertical alignment specifier to cause all columns to be vertically aligned
   in that way.

``valign_fill='t'``
   If there are more columns than there are entries in ``valign``, the extra
   columns will have their vertical alignment set to ``valign_fill``.

``width_fill=None``
   If there are more columns than there are entries in ``widths``, the extra
   columns will have their widths set to ``width_fill``.

``widths=()``
   A sequence of integers specifying the width of each column, in order.  Lines
   wider than the given width will be wrapped; the wrapping can be configured
   via the ``break_long_words`` and ``break_on_hyphens`` options.  A width of
   `None` disables wrapping for that column and causes the column's width to be
   set to the width of the longest line.  ``widths`` may optionally be set to a
   single width to cause all columns to be that wide.

``wrap_func``
   The function to use for wrapping long lines; it should take a string and a
   width and return an iterable of strings.  The default value is a custom
   function that properly handles fullwidth characters, ANSI color escape
   sequences, etc.; if your table contains such strings, any user-supplied
   ``wrap_func`` must be able to handle them as well.  When ``wrap_func`` is
   set to a user-supplied value, the ``break_long_words`` and
   ``break_on_hyphens`` options are ignored.


.. _borderstyle:

``BorderStyle``
---------------
The ``BorderStyle`` class is a `namedtuple` listing the strings to use for
drawing a table's borders & rules.  Its attributes are:

.. csv-table::
    :header: Attribute,Description,Example

    ``hline``,horizontal line,─
    ``vline``,vertical line,│
    ``ulcorner``,upper-left box corner,┌
    ``urcorner``,upper-right box corner,┐
    ``llcorner``,lower-left box corner,└
    ``lrcorner``,lower-right box corner,┘
    ``vrtee``,tee pointing right,├
    ``vltee``,tee pointing left,┤
    ``dhtee``,tee pointing down,┬
    ``uhtee``,tee pointing up,┴
    ``plus``,cross/four-way joint,┼

``txtble`` provides the following predefined ``BorderStyle`` instances:

``ASCII_BORDERS``
   The default border style.  Draws borders using only the ASCII characters
   ``-``, ``|``, and ``+``::

       +-+-+
       |A|B|
       +-+-+
       |C|D|
       +-+-+

``ASCII_EQ_BORDERS``
   Like ``ASCII_BORDERS``, but uses ``=`` in place of ``-``::

       +=+=+
       |A|B|
       +=+=+
       |C|D|
       +=+=+

``LIGHT_BORDERS``
   Uses the light box drawing characters::

       ┌─┬─┐
       |A|B|
       ├─┼─┤
       |C|D|
       └─┴─┘

``HEAVY_BORDERS``
   Uses the heavy box drawing characters::

       ┏━┳━┓
       ┃A┃B┃
       ┣━╋━┫
       ┃C┃D┃
       ┗━┻━┛

``DOUBLE_BORDERS``
   Uses the double box drawing characters::

       ╔═╦═╗
       ║A║B║
       ╠═╬═╣
       ║C║D║
       ╚═╩═╝

``DOT_BORDERS``
   Uses ``⋯``, ``⋮``, and ``·``::

       ·⋯·⋯·
       ⋮A⋮B⋮
       ·⋯·⋯·
       ⋮C⋮D⋮
       ·⋯·⋯·

If you define your own custom instances of ``BorderStyle``, they must adhere to
the following rules:

- The ``hline`` string must be exactly one terminal column wide (the same width
  as a space character).
- All strings other than ``hline`` must be the same width.
- No string may contain a newline.


.. _other:

Other
-----

``IndeterminateWidthError``
   Subclass of ``ValueError``.  Raised when a string is reported as having
   negative/indeterminate width.  (For the default ``len_func``, this happens
   when the string contains a DEL or a C0 or C1 control character other than a
   tab, newline, or ANSI color escape sequence.)  The string in question is
   available as the exception's ``string`` attribute.

``NumericWidthOverflowError``
   Subclass of ``ValueError``.  Raised when a column has a non-`None` width,
   the column's ``align`` value contains ``'n'``, and aligning the numbers in
   the column along their decimal points would cause one or more cells to
   exceed the column's width.

``UnterminatedColorError``
   Subclass of ``ValueError``.  Raised by ``with_color_stripped`` upon
   encountering an ANSI color escape sequence that is not eventually terminated
   by a reset/sgr0 sequence.  The string in question is available as the
   exception's ``string`` attribute.

``with_color_stripped``
   A function decorator for applying to ``len`` or imitators thereof that
   strips ANSI color sequences from a single string argument before passing it
   on.  If any color sequences are not followed by a reset sequence, an
   ``UnterminatedColorError`` is raised.


Unicode in Python 2
-------------------
The following guarantees are made regarding ``txtble``'s handling of Unicode in
the fragile twilight realm that is Python 2:

- If all table elements (table cells, ``*_fill`` options, ``none_str``, border
  style strings, etc.) are or stringify to ASCII-only `str` values, calling
  ``str(tbl)`` will work, and ``tbl.show()`` will return a `str`.

- If one or more table elements are `unicode` and all other cell values are or
  stringify to ASCII-only `str` values, calling ``unicode(tbl)`` will work, and
  ``tbl.show()`` will return a `unicode`.

In all other cases, you're on your own.
