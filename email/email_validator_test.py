from pytest import raises

from .email_validator import (
    LengthEmailValidator,
    HasAtCharacterValidator,
    EmailHasUserValidator,
    EmailHasDomainValidator,
    EmailValidator
)


from .email_exceptions import (
    AtCharacterInMailException,
    EmailLengthException, 
    EmailUserException,
    EmailDomainException
)


def test_length_of_email_validator_positive():
    validator = LengthEmailValidator('test@email.pl')
    assert validator.is_valid() is True


def test_length_of_email_validator_negative():
    validator = LengthEmailValidator('t'*250 +'@email.pl')
    with raises(EmailLengthException) as exception:
        validator.is_valid()
        assert exception.value == 'Email is too long.'


def test_at_character_in_email_positive():
    validator = HasAtCharacterValidator('test@email.com')
    assert validator.is_valid() is True


def test_at_character_in_email_negative():
    validator = HasAtCharacterValidator('testemail.com')
    with raises(AtCharacterInMailException) as exception:
        validator.is_valid()
        assert exception.value == 'Email does not contain an "@" character!'


def test_email_user_validator_positive():
    validator = EmailHasUserValidator('test@email.com')
    assert validator.is_valid() is True


def test_email_user_validator_negative():
    validator = EmailHasUserValidator('testemail.com')
    with raises(EmailUserException) as exception:
        validator.is_valid()
        assert exception.value == 'Email does not contain a user name!'

    validator = EmailHasUserValidator('@testemail.com')
    with raises(EmailUserException) as exception:
        validator.is_valid()
        assert exception.value == 'Email does not contain a user name!'


def test_email_domain_validator_positive():
    validator = EmailHasDomainValidator('test@email.com')
    assert validator.is_valid() is True


def test_email_domain_validator_negative():
    validator = EmailHasDomainValidator('testemail.co@m')
    with raises(EmailDomainException) as exception:
        validator.is_valid()
        assert exception.value == 'Email does not contain a domain!'

    validator = EmailHasDomainValidator('testemail.com')
    with raises(EmailDomainException) as exception:
        validator.is_valid()
        assert exception.value == 'Email does not contain a domain!'


def test_email_validator_positive():
    validator = EmailValidator('test@email.com')
    assert validator.is_valid() is True


# def test_email_validator_negative():
#     validator = EmailValidator('@testemail.com')
#     assert validator.is_valid() is False
