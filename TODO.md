- Add docstrings
- Better handling of Unicode when wrapping text:
    - Don't break across zero-width joiner, word joiner, or non-breaking space
    - Don't break in the middle of combining character sequences
        - Don't break on a space or hyphen followed by combining characters
    - Break on more than just spaces and hyphens?
    - cf. the Unicode line breaking algorithm
    - cf. `uniseg` package

Features to Add
---------------
- Borders & rules:
    - Add an "hrule" class that can be passed in place of a data row to
      indicate that a horizontal rule should be added.  Its constructor should
      take an optional `border_style` argument.
    - easy way to change just the column separator in non-rule rows?
        - Allow `column_border` to be just a string? (since only one string of
          `BorderStyle` gets used anyway)
    - easy way to change the column separator in all rows?
        - "doubling" ('|' → '||') specific vrules
    - using different column vrules in the header (and/or header rule) than in
      the data?
    - drawing left & right border vrules but no top/bottom hrules
    - drawing top & bottom border hrules but not left/right vrules
        - drawing just a top or just a bottom border hrule

- Cell alignment:
    - Add an 'n' alignment option for aligning numeric values along a decimal
      point
        - Support also controlling the alignment of string values in the same
          column
        - Support configuring how numeric values should be aligned relative to
          long string values in the same column
    - Support setting column-specific alignments with `tbl.align[i] = 'c'` even
      when `align` hasn't been previously set to a list
    - setting the alignment of individual cells (e.g., having a centered "—"
      cell in the middle of a bunch of left-aligned cells)
    - configuring vertical alignment of cells when other cells in the same row
      have more lines
    - different horizontal & vertical alignment for headers than for data
    - per-row alignments

- Cell widths and line-wrapping:
    - parameters for setting minimum & maximum column widths
    - handling of lines that are still too long (e.g., due to containing a very
      long word) after wrapping: let them overflow or expand the column to
      contain them

- Showing cells:
    - setting a function to use for stringification of all non-string cell
      values
    - customizing numeric formatting

- API:
    - constructing a table from a sequence of dicts whose keys match the
      table's headers
        - specifying a mapping from dict keys to headers so that they don't
          have to use the exact same strings?
    - manipulating (editing, deleting, etc.) rows & cells that have already
      been added to the Txtble
    - Allow `header_fill` and `row_fill` to be callables that are called
      whenever a value from them is required?
    - constructing from a CSV file?
    - Add `Txtble` subclasses with default values configured for various common
      types of text tables?
        - cf. `tabulate`'s `tablefmt`
    - querying the width of a column before showing?

- Parameters for setting exact (and/or min/max?) number of columns
    - adding filler cells to short rows until they reach a certain number of
      columns
    - removing extra cells from long rows until they reach a certain number of
      columns
- cells that span multiple columns and/or rows
- sorting rows?
