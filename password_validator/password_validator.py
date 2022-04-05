"""The module contains a set of classes for password validation."""

from hashlib import sha1
import requests

from validator_base.base_validator import Validator
from text_validator import (
    UpperCharactersValidator,
    LowerCharactersValidator,
    PunctuationValidator,
    DigitsValidator,
    LengthValidator
)

from .password_exceptions import HaveIbeenPwnedException


class HaveIbeenPwned(Validator):
    """A class that checks in an external api (haveIBeenPwned) if a password has been stolen."""
    def __init__(self, password: str) -> None:
        self.password = password

    def is_valid(self) -> bool:
        """Check that the password was leaked ever.

        Returns:
            bool: True if there was no leak, otherwise raise an exception.
        """
        password_hash = sha1(self.password.encode(encoding="utf-8")).hexdigest().upper()
        response = requests.get("https://api.pwnedpasswords.com/range/" + password_hash[:5])

        for pwned_hash in response.text.splitlines():
            if password_hash[5:] == pwned_hash.split(':')[0]:
                raise HaveIbeenPwnedException('The password was leaked at least once.')
        return True


class PasswordValidator(Validator):
    """ A class that validate a password. """

    MIN_LENGTH = 8
    NUMBER_OF_UPPER_CHARACTERS = 2
    NUMBER_OF_LOWER_CHARACTERS = 2
    NUMBER_OF_DIGITS = 2
    NUMBER_OF_PUNCTUATION = 2

    def __init__(self, password: str, *args) -> None:
        """Initialization of object"""
        self.text = password
        # if rules is None:
        #     self.rules = PasswordRules()
        # else:
        #     self.rules = rules

        if args is None:
            self.validator: Validator = [
                (LengthValidator, self.MIN_LENGTH),
                (UpperCharactersValidator, self.NUMBER_OF_UPPER_CHARACTERS),
                (LowerCharactersValidator, self.NUMBER_OF_LOWER_CHARACTERS),
                (DigitsValidator, self.NUMBER_OF_DIGITS),
                (PunctuationValidator, self.NUMBER_OF_PUNCTUATION)
                # HaveIbeenPwned
            ]
        else:
            self.validator = [validator for validator in args if isinstance(validator, Validator)]

    def is_valid(self) -> bool:
        """Check that password is valid

        Returns:
            bool: True if password is valid, otherwise raise exception
        """
        for class_name in self.validator:
            validator = class_name[0](self.text, class_name[1])
            validator.is_valid()
            if validator.is_valid() is False:
                return False

        return True
