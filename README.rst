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

`GitHub <https://github.com/jwodder/txtble>`_
| `PyPI <https://pypi.org/project/txtble/>`_
| `Issues <https://github.com/jwodder/txtble/issues>`_

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

... unless you've *also* specified a ``header_fill`` to use as the the header
for extra columns::

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


API
===

``Txtble(data=(), **kwargs)``
   Create a new ``Txtble`` object.  The table's data may be passed to the
   constructor as an iterable of iterables (rows) of values; otherwise, the
   data starts out empty.  In either case, further data rows can be added via
   the ``append()`` and ``extend()`` methods.

   ``**kwargs`` are used to configure the ``Txtble`` instance; see
   "`Configuration Options <configuration_options_>`_" below.

``tbl.append(row)``
   Add an iterable of values as a new data row at the bottom of the table

``tbl.extend(rows)``
   Add an iterable of iterables of values as new data rows at the bottom of the
   table

``tbl.show()`` or ``str(tbl)``
   Convert the ``Txtble`` instance to a string showing a plain text table.
   Table cells and filler values that are not already strings are converted by
   calling `str()` on them; the exceptions are `None` values, which are
   displayed according to the ``none_str`` option (see below).  All tab
   characters are expanded to spaces before building the table.

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

``border=True``
   Whether to draw a border around the edge of the table

``column_border=True``
   Whether to draw a vertical rule between individual columns

``columns=None``
   An optional positive integer.  When set, show exactly the given number of
   columns per row, adding cells with ``row_fill`` and discarding extra cells
   as needed.  If ``headers`` is also set, its length must equal ``columns`` or
   else a `ValueError` is raised.  Setting both ``columns`` and ``headers``
   causes ``header_fill`` to be ignored.

``header_border=None``
   Whether to draw a horizontal rule above the data rows, below the header row
   (if any).  The default value of `None` means that the border will be drawn
   if & only if ``headers`` is non-`None`.

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

``none_str=''``
   The string to display in place of `None` values (Setting ``none_str=None``
   is the same as setting it to ``'None'``)

``row_border=False``
   Whether to draw a horizontal rule between data rows

``row_fill=''``
   If the rows of a table differ in number of columns, cells are added to the
   shorter rows until they all line up, and the added cells contain
   ``row_fill`` as their value.

``rstrip=True``
   When ``border=False``, setting ``rstrip=False`` will cause the last cell of
   each row to still be padded with trailing whitespace in order to reach the
   full column width.  (Normally, this whitespace is omitted when
   ``border=False`` as there is no end-of-line border to align.)  This option
   is useful if you wish to append text to one or more lines of the output and
   have it appear strictly outside the table.


Unicode in Python 2
-------------------
The following guarantees are made regarding ``txtble``'s handling of Unicode in
the fragile twilight realm that is Python 2:

- If all cell values are or stringify to ASCII-only `str` values, calling
  ``str(tbl)`` will work, and ``tbl.show()`` will return a `str`.

- If one or more cell values are `unicode` and all other cell values are or
  stringify to ASCII-only `str` values, calling ``unicode(tbl)`` will work, and
  ``tbl.show()`` will return a `unicode`.

In all other cases, you're on your own.
