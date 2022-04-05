""" The module contains a set of classes for email validation."""

from validator_base import Validator
from .email_exceptions import (
    AtCharacterInMailException,
    EmailLengthException, 
    EmailUserException,
    EmailDomainException
)
from text_validator import LengthValidator



class LengthEmailValidator(Validator):
    """ Class of length email validator"""

    # max length of email address is 255 characters
    MAX_EMAIL_LENGTH = 255

    def __init__(self, email: str) -> None:
        """ Initialization of LengthEmailValidator """
        self.email = email

    def is_valid(self) -> bool:
        """Check if length of the email adress is not too long.

        Raises:
            EmailLengthException: Exception if email is too long

        Returns:
            bool: True if length of the email adress is ok.
        """
        if len(self.email) <= self.MAX_EMAIL_LENGTH:
            return True

        raise EmailLengthException('Email is too long.')


class HasAtCharacterValidator(Validator):
    """ Class of has '@' character validator """
    def __init__(self, email: str) -> None:
        """ Initialization of object of HasAtCharacterValidator """
        self.email = email

    def is_valid(self) -> bool:
        """Check if an email adress contain '@' character.

        Raises:
            AtCharacterInMailException: Exception that email does not contain '@' character

        Returns:
            bool: True if there is an '@' character in the email
        """
        if '@' in self.email:
            return True

        raise AtCharacterInMailException('Email does not contain an "@" character!')


class EmailHasUserValidator(Validator):
    """ Class of email has an user validator"""

    def __init__(self, email: str) -> None:
        """Initialization of an object"""
        self.email = email

    def is_valid(self) -> bool:
        """Check that the email has a user part

        Raises:
            EmailUserException: Exception if email does not contain a user part

        Returns:
            bool: True if there is a user part in the email
        """
        parts = self.email.split('@')
        if len(parts) > 1 and len(parts[0]) > 0:
            return True
        
        raise EmailUserException('Email does not contain a user name!')
    

class EmailHasDomainValidator(Validator):
    """ A class of an email domain validator"""

    def __init__(self, email: str) -> None:
        """Initialization of object"""
        self.email = email

    def is_valid(self) -> bool:
        """Check that the email has a domain part

        Raises:
            EmailDomainException: Exception if email does not contain domain part

        Returns:
            bool: True if the email has a domain part
        """
        parts = self.email.split('@')
        if len(parts) > 1 and len(parts[1]) > 1:
            return True  
        raise EmailDomainException('Email does not contain a domain!')


class EmailValidator(Validator):
    """A class of an email validator"""

    def __init__(self, email: str) -> None:
        """Initialization of object """
        self.email = email
        self.validators = [
            HasAtCharacterValidator,
            LengthEmailValidator,
            EmailHasUserValidator,
            EmailHasDomainValidator
        ]

    def is_valid(self) -> bool:
        """Check that the email is valid

        Returns:
            bool: True if an email is valid
        """
        for class_name in self.validators:
            validator = class_name(self.email)
            if validator.is_valid() is False:
                return False

        return True
