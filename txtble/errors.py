class IndeterminateWidthError(ValueError):
    """
    Raised when a string is reported as having negative/indeterminate width
    """

    def __init__(self, string):
        #: The string in question
        self.string = string
        super(IndeterminateWidthError, self).__init__(string)

    def __str__(self):
        return '{0.string!r}: string has indeterminate width'.format(self)


class UnterminatedColorError(ValueError):
    """
    Raised when a string contains an ANSI color escape sequence without a reset
    """

    def __init__(self, string):
        #: The string in question
        self.string = string
        super(UnterminatedColorError, self).__init__(string)

    def __str__(self):
        return '{0.string!r}: ANSI color sequence not reset'.format(self)
