""" tests for text validators """

import pytest

from .text_validator import (
    UpperCharactersValidator,
    LowerCharactersValidator,
    DigitsValidator,
    PunctuationValidator,
    LengthValidator
)

from .text_exceptions import (
    HasUpperCharactersException,
    HasLowerCharactersException,
    HasDigitsException,
    HasPunctuationException,
    LengthException
)


def test_upper_characters_validator_positive():
    validator = UpperCharactersValidator('PasswordToTest', occurrences=3)

    assert validator.is_valid() is True


def test_upper_characters_validator_negative():
    validator = UpperCharactersValidator('PasswordToTest', occurrences=4)
    with pytest.raises(HasUpperCharactersException) as exception:
        validator.is_valid()
        assert exception.value == 'There is no valid occurrences of upper charcters \
            in validate text.'


def  test_lower_characters_validator_positive():
    validator = LowerCharactersValidator('PasswordToTest', occurrences=11)
    assert validator.is_valid() == True


def  test_lower_characters_validator_negative():
    validator = LowerCharactersValidator('PasswordToTest', occurrences=12)
    with pytest.raises(HasLowerCharactersException) as exception:
        validator.is_valid()
        assert exception.value == 'There is no valid occurrences of lower characters \
            in validate text.'


def test_punctuation_validator_positive():
    validator = PunctuationValidator('PasswordToTest!', occurrences=1)
    assert validator.is_valid() is True


def test_punctuation_validator_negative():
    validator = PunctuationValidator('PasswordToTest!', occurrences=2)
    with pytest.raises(HasPunctuationException) as exception:
        validator.is_valid()
        assert exception.value == 'There is no valid occurrences of punctuation characters \
            in validate text.'


def test_digits_validator_positive():
    validator = DigitsValidator('PasswordToTest123', occurrences=3)
    assert validator.is_valid() is True


def test_digits_validator_negative():
    validator = DigitsValidator('PasswordToTest123', occurrences=4)
    with pytest.raises(HasDigitsException) as exception:
        validator.is_valid()
        assert exception.value == 'There is no valid occurrences of digits \
            in validate text.'


def test_length_validator_positive():
    validator = LengthValidator('PasswordToTest', length=14)
    assert validator.is_valid() is True


def test_length_validator_negative():
    validator = LengthValidator('PasswordToTest', length=15)
    with pytest.raises(LengthException) as exception:
        validator.is_valid()
        assert exception.value == 'The text is to short!'
