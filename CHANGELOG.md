v0.12.1 (2023-10-10)
--------------------
- Support Python 3.9 through 3.12
- Drop support for Python 3.6
- Add type annotations to tests
- Fix mypy's type inference for `headers`

v0.12.0 (2020-10-07)
--------------------
- Support Python 3.8
- Drop support for Python 2, Python 3.4, and Python 3.5
- Update wcwidth requirement to `~= 0.2.0`
- Drop six requirement
- Add type annotations
- Setting `len_func` to `None` now causes the option's default value to be used

v0.11.1 (2019-05-29)
--------------------
- Loosen `attrs` version requirement

v0.11.0 (2018-11-15)
--------------------
- Added numeric alignment

v0.10.0 (2018-09-10)
--------------------
- Added `valign` and `valign_fill` options

v0.9.0 (2017-07-28)
-------------------
- Table rows can now be represented by `dict`s that map header names to cell
  values
- Added a `dict_fill` option for handling missing keys in `dict` rows

v0.8.0 (2017-07-24)
-------------------
- Added `left_border`, `right_border`, `top_border`, and `bottom_border`
  options

v0.7.0 (2017-07-18)
-------------------
- Added a `len_func` option, allowing the user to specify a custom function for
  calculating text width
- Added a `with_color_stripped` function decorator for use by custom
  `len_func`s
- Added `widths` and `width_fill` options for wrapping columns to fixed widths
- Added `break_long_words` and `break_on_hyphens` options for controlling text
  wrapping
- Added a `wrap_func` option, allowing the user to specify a custom function
  for wrapping text

v0.6.0 (2018-07-11)
-------------------
- Added ANSI color escape sequence support

v0.5.0 (2018-07-06)
-------------------
- Added `align` and `align_fill` options

v0.4.0 (2018-07-01)
-------------------
- Added `left_padding` and `right_padding` options

v0.3.0 (2018-06-25)
-------------------
- Table cell values that begin with a combining character will now have a space
  prepended
- Added a `padding` option
- Strings with indeterminate widths now cause an `IndeterminateWidthError` to
  be raised
- `'\f'` and `'\v'` are now always treated as line separators, even inside
  `str` objects in Python 2

v0.2.0 (2018-06-16)
-------------------
- Custom borders:
    - Added a `BorderStyle` class and several predefined instances for
      describing the strings to use for drawing borders
    - Added a `border_style` option for setting the default style for all of a
      table's borders
    - `border`, `column_border`, `header_border`, and `row_border` can now be
      set to `BorderStyle` instances to set their individual styles

v0.1.0 (2018-06-14)
-------------------
Initial release
