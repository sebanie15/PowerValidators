""" Set of text exceptions """

from validator_base.base_exceptions import ValidatorException


class HasUpperCharactersException(ValidatorException):
    """returned if validation of upper characters in the text is not True"""
    pass


class HasLowerCharactersException(ValidatorException):
    """returned if validation of lower characters in the text is not True"""
    pass


class HasDigitsException(ValidatorException):
    """returned if validation of digits in the text is not True"""
    pass


class HasPunctuationException(ValidatorException):
    """returned if validation of punctuation in the text is not True"""
    pass


class LengthException(ValidatorException):
    """returned if validation of length of the text is not True"""
    pass
