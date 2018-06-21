- Add docstrings

Features to Add
---------------
- Borders & rules:
    - Add an "hrule" class that can be passed in place of a data row to
      indicate that a horizontal rule should be added.  Its constructor should
      take optional keyword arguments for setting the box-drawing characters to
      use ('dash', 'joint', '`left_joint`', '`right_joint`', 'midjoint'?)
    - easy way to change just the column separator in non-rule rows?

- Showing, wrapping, & aligning cells:
    - separate parameters for padding on the right vs. left?
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
    - aligning numeric cells on a decimal point

- API:
    - constructing a table from a sequence of dicts whose keys match the
      table's headers
        - specifying a mapping from dict keys to headers so that they don't
          have to use the exact same strings?
    - specifying a custom function for calculating text width
    - specifying a custom function for line wrapping
        - The default wrapping function should use the specified width function
    - manipulating (editing, deleting, etc.) rows & cells that have already
      been added to the Txtble
    - Allow `header_fill` and `row_fill` to be callables that are called
      whenever a value from them is required?
    - constructing from a CSV file?

- Parameters for setting exact (and/or min/max?) number of columns
    - adding filler cells to short rows until they reach a certain number of
      columns
    - removing extra cells from long rows until they reach a certain number of
      columns
- cells that span multiple columns and/or rows
- sorting rows?
