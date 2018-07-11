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
