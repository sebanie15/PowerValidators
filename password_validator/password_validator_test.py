""" tests for password validators"""


import pytest
from .password_validator import PasswordValidator, HaveIbeenPwned
from .password_exceptions import HaveIbeenPwnedException


def test_have_i_been_pwned_positive(requests_mock):
    data = '1692067afd8bd5522a15b912826268e5a53:1\n38ab81692067afd8bd5522a15b912826268e5a52:2'.upper()
    requests_mock.get("https://api.pwnedpasswords.com/range/38ab8", text=data)
    validator = HaveIbeenPwned('aB5hJ#$1kk09023#%#hjadADS')
    assert validator.is_valid() is True


def test_have_i_been_pwned_negative(requests_mock):
    data = ''
    requests_mock.get("https://api.pwnedpasswords.com/range/38ab8", text=data)
    validator = HaveIbeenPwned('aB5hJ#$1kk09023#%#hjadADS')
    with pytest.raises(HaveIbeenPwnedException) as exception:
        validator.is_valid()
        assert exception.value == 'The password was leaked at least once.'


def test_password_validator_positive():
    pass


def test_password_validator_negative():
    pass
