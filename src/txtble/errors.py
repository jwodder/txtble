class IndeterminateWidthError(ValueError):
    """
    Raised when a string is reported as having negative/indeterminate width
    """

    def __init__(self, string: str):
        #: The string in question
        self.string: str = string

    def __str__(self) -> str:
        return f"{self.string!r}: string has indeterminate width"


class UnterminatedColorError(ValueError):
    """
    Raised when a string contains an ANSI color escape sequence without a reset
    """

    def __init__(self, string: str):
        #: The string in question
        self.string: str = string

    def __str__(self) -> str:
        return f"{self.string!r}: ANSI color sequence not reset"


class NumericWidthOverflowError(ValueError):
    """
    Raised when applying numeric alignment to a column causes one or more cells
    to exceed the column's set width
    """

    def __str__(self) -> str:
        return "Numeric alignment overflows column width"
