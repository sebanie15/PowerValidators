"""The module contains a set of classes of text validation """

from validator_base.base_validator import Validator

from .text_exceptions import (
    HasUpperCharactersException,
    HasLowerCharactersException,
    HasDigitsException,
    HasPunctuationException,
    LengthException
)


class UpperCharactersValidator(Validator):
    """A class, the task of which is to check whether the text contains an appropriate number of upper characters."""
    def __init__(self, text: str, occurrences: int = 1) -> None:
        """Initialization of object"""
        self.text = text
        self.occurrences = occurrences

    def is_valid(self) -> bool:
        """Check that there are enough upper characters in the text

        Raises:
            HasUpperCharactersException: Not enough upper characters exception

        Returns:
            bool: True if there are enough upper characters in the text
        """
        counter = 0
        for char in self.text:
            if char.isupper():
                counter += 1
        if counter >= self.occurrences:
            return True
        raise HasUpperCharactersException('There is no valid occurrences of upper charcters \
            in validate text.')


class LowerCharactersValidator(Validator):
    """A class, the task of which is to check whether the text contains an appropriate\
        number of lower characters."""
    def __init__(self, text: str, occurrences: int = 1) -> None:
        """Initialization of object"""
        self.text = text
        self.occurrences = occurrences

    def is_valid(self) -> bool:
        """Check that there are enough lower characters in the text.

        Raises:
            HasLowerCharactersException: Not enough lower characters exception

        Returns:
            bool: True if there are enough lower characters in the text
        """
        counter = 0
        for char in self.text:
            if char.islower():
                counter += 1
        if counter >= self.occurrences:
            return True
        raise HasLowerCharactersException('There is no valid occurrences of lower characters \
            in validate text.')


class DigitsValidator(Validator):
    """A class, the task of which is to check whether the text contains an appropriate\
        number of digits characters."""
    def __init__(self, text: str, occurrences: int = 1) -> None:
        """Initialization of object"""
        self.text = text
        self.occurrences = occurrences

    def is_valid(self) -> bool:
        """Check that there are enough digits in the text.

        Raises:
            HasDigitsException: Not enough digits exception

        Returns:
            bool: True if there is enough digits in the text
        """
        counter = 0
        for char in self.text:
            if char.isdigit():
                counter += 1
        if counter >= self.occurrences:
            return True
        raise HasDigitsException('There is no valid occurrences of digits in validate text.')


class PunctuationValidator(Validator):
    """A class, the task of which is to check whether the text contains an appropriate\
        number of special characters (punctuation)."""
    def __init__(self, text: str, occurrences: int = 1) -> None:
        """Initialization of object"""
        self.text = text
        self.occurrences = occurrences

    def is_valid(self) -> bool:
        """Check that there are enough occurrences of punctuation.

        Raises:
            HasPunctuationException: Not enough occurrences of punctuation

        Returns:
            bool: True if there is enough occurrences of punctuation
        """
        counter = 0
        for char in self.text:
            if not char.isalnum():
                counter += 1
        if counter >= self.occurrences:
            return True
        raise HasPunctuationException('There is no valid occurrences of punctuation characters \
            in validate text.')


class LengthValidator(Validator):
    """A class that checks if the length of text is greater than or equal to the required length."""
    def __init__(self, text: str, length: int = 1, equal: bool = False) -> None:
        """Initialization of object"""
        self.text = text
        self.length = length
        self.equal = equal

    def is_valid(self) -> bool:
        """CHeck the length of text to be validated

        Raises:
            LengthException: The length of the text is to short

        Returns:
            bool: True if length is enough
        """
        if not self.equal:
            if len(self.text) >= self.length:
                return True
        else:
            if len(self.text) == self.length:
                return True
                
        raise LengthException('The text is to short!')
