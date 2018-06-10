- Fill in keywords and classifiers
- Expand long description in README & docstring
- Add docstrings

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

    - Parameter for adding an hrule between every pair of rows
        - Parameter for a special hrule after the headers?
    - Parameter for putting an hrule at the top in the absence of headers or
      borders
    - Parameter for adding vertical but not horizontal borders
    - Parameter for adding horizontal but not vertical borders
    - Add an "hrule" class that can be passed in place of a data row to
      indicate that a horizontal rule should be added.  Its constructor should
      take optional keyword arguments for setting the box-drawing characters to
      use ('dash', 'joint', '`left_joint`', '`right_joint`', 'midjoint'?)
    - omitting all internal borders

- Showing, wrapping, & aligning cells:
    - Parameter for padding between vertical bars and cell contents
    - Centering & right-aligning of specified columns
    - Setting the text alignment of individual cells (e.g., having a centered
      "—" cell in the middle of a bunch of left-aligned cells)
    - parameter for setting how to show bools?
    - Parameter for setting how to handle overly large fields: let them
      overflow, truncate them, or line-wrap them
    - handling of lines that are still too long (e.g., due to containing a very
      long word) after wrapping
    - Parameters for setting minimum, maximum, and exact column widths
    - forcing all columns to have the same width?
    - setting a function to use for stringification of all non-string cell
      values

- API:
    - Add a method that simply returns the padded & folded cells as an array of
      arrays of strings rather than formatting them
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
- Producing Markdown- or reStructuredText-compatible tables
- Producing HTML tables
- Producing PDF tables with reportlab?
- parsing a text table back into a Txtble object?
