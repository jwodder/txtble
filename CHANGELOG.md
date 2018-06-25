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
