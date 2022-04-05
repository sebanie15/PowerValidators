"""set of Exceptions of email validators"""

from validator_base.base_exceptions import ValidatorException


class AtCharacterInMailException(ValidatorException):
    pass


class EmailLengthException(ValidatorException):
    pass


class EmailUserException(ValidatorException):
    pass


class EmailDomainException(ValidatorException):
    pass
