- Expand long description in README & docstring
- Add docstrings
- Handle strings for which `wcswidth()` returns a negative number (e.g.,
  anything with an ANSI escape sequence)
- Handle strings that are just/start with combining characters with nothing to
  combine with (Prepend a space?)
- Make `to_lines()` also split on `'\v'` and `'\f'` when working with `str`
  objects in Python 2?

Features to Add
---------------
- Borders & rules:
    - Setting the strings to use for column separators, hrules, joints,
      corners, etc.
    - Unicode output with box-drawing characters:

            ASCII         - | + + + + + + + + +
            Light         ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
            Heavy         ━ ┃ ┏ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋
            Double        ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
            Dots          ⋯ ⋮ · · · · · · · · ·

    - Parameter for a special hrule after the headers?
    - Add an "hrule" class that can be passed in place of a data row to
      indicate that a horizontal rule should be added.  Its constructor should
      take optional keyword arguments for setting the box-drawing characters to
      use ('dash', 'joint', '`left_joint`', '`right_joint`', 'midjoint'?)
    - easy way to change just the column separator in non-rule rows?

- Showing, wrapping, & aligning cells:
    - Parameter for padding between vertical bars and cell contents
    - Centering & right-aligning of specified columns
    - Setting the text alignment of individual cells (e.g., having a centered
      "—" cell in the middle of a bunch of left-aligned cells)
    - Parameter for setting how to handle overly large fields: let them
      overflow, truncate them, or line-wrap them
    - handling of lines that are still too long (e.g., due to containing a very
      long word) after wrapping
    - Parameters for setting minimum, maximum, and exact column widths
    - setting a function to use for stringification of all non-string cell
      values

- API:
    - constructing a table from a sequence of dicts or objects with
      elements/attributes that match the table's headers
    - specifying a custom function for calculating text width
    - specifying a custom function for line wrapping
        - The default wrapping function should use the specified width function
    - manipulating (editing, deleting, etc.) rows & cells that have already
      been added to the Txtble
    - Allow `header_fill` and `row_fill` to be callables that are called
      whenever a value from them is required?

- Parameters for setting exact (and/or min/max?) number of columns
    - adding filler cells to short rows until they reach a certain number of
      columns
    - removing extra cells from long rows until they reach a certain number of
      columns
- cells that span multiple columns and/or rows
