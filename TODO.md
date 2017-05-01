- Support Python 3

Features to Add
---------------
- Parameters for setting minimum, maximum, and exact column widths
    - Parameter for setting how to handle overly large fields: let them
      overflow, truncate them, or line-wrap them
- Parameters for setting exact (and/or min/max?) number of columns
- Unicode output with box-drawing characters:

        ASCII         - | + + + + + + + + +
        Light         ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
        Heavy         ━ ┃ ┏ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋
        Double        ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
        Dots          ⋯ ⋮ · · · · · · · · ·

- Setting the strings to use for column separators, hrules, joints, corners,
  etc.
- Parameter for adding an hrule between every pair of rows
    - Parameter for a special hrule after the headers?
- Parameter for putting an hrule at the top in the absence of headers or
  borders
- Parameter for padding between vertical bars and cell contents
- Parameter for adding vertical but not horizontal borders
- Parameter for adding horizontal but not vertical borders
- Centering & right-aligning of specified columns
- Add a method that simply returns the padded & folded cells as an array of
  arrays of strings rather than formatting them
- cells that span multiple columns and/or rows
- constructing a table from a sequence of dicts or objects with
  elements/attributes that match the table's headers
- Add an "hrule" class that can be passed in place of a data row to indicate
  that a horizontal rule should be added.  Its constructor should take
  optional keyword arguments for setting the box-drawing characters to use
  ('dash', 'joint', '`left_joint`', '`right_joint`', 'midjoint'?)
- parameter for setting how to display `None`s
- parameter for setting how to show bools?
- parameter for producing Markdown- or reStructuredText-compatible tables
- parameter for producing HTML tables
- parsing a text table back into a Tabulator object?
- transposition
- handling of Unicode characters with non-unit width
