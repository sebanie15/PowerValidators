from hashlib import sha1
from unittest.mock import DEFAULT
from requests import get
from string import ascii_lowercase, ascii_uppercase, punctuation

from .pwd_exceptions import MinLengthException
from PwdValidator.pwd_rule import PwdRule



class PwdValidator:
    """ BasicPwdValidator is a class for checking passwords according to the
        assumed rules - PwdRule ().

        The following methods are available:\n
        >> hash_pwd,\n
        >> length_is_valid,\n
        >> num_digits_is_valid,\n
        >> num_special_char_is_valid,\n
        >> num_lowercase_is_valid,\n
        >> num_uppercase_is_valid

    Returns:
        object: Object of BasicPwdValidator class
    """

    def __init__(self, rule: PwdRule = None) -> None:
        """ Initialization of BasicPwdValidator object.

        Args:
            rule (PasswordRule): PasswordRule class. Defaults to None.
        """
        # If rule is None then assign default PasswordRule to self.rule
        if rule is None:
            self.rule = PwdRule()
        else:
            self.rule = rule

    def hash_pwd(self, password: str) -> str:
        """This method returns the hash of password.
            It yused sha1 algorithm

        Args:
            password (str): password to be hashed

        Returns:
            str: hash of password
        """
        return sha1(password.encode(encoding="utf-8")).hexdigest

    def length_is_valid(self, password: str) -> bool:
        """This method check if length of password is equal or greater
            than minimum length configured in the regule.

        Args:
            password (str): password to be checked

        Returns:
            bool: True if length password is >= of minimum length
        """
        return len(password) >= self.rule.min_length_of_pwd

    def num_digits_is_valid(self, password: str) -> bool:
        """This method check if the password has a minimum number of digits.

        Args:
            password (str): password to be checked

        Returns:
            bool: True if there is a minimum number of digits in the password
        """

        counter = 0
        for char in password:
            if char.isdigit():
                counter += 1
        return counter >= self.rule.min_number_of_digits

    def num_special_char_is_valid(self, password: str) -> bool:
        """This method check if the password has a minimum number of special characters

        Args:
            password (str): password to be checked

        Returns:
            bool: True if there is a minimum number of special charackters in the password
        """
        counter = 0
        for char in password:
            if char in punctuation:
                counter += 1
        return counter >= self.rule.min_number_of_special_char

    def num_lowercase_is_valid(self, password: str) -> bool:
        """This method check if the password has a minimum number of lowercase characters.

        Args:
            password (str): password to be checked

        Returns:
            bool: True if there is a minimum number of lowercase characters in the password,
            False otherwise
        """
        counter = 0
        for char in password:
            if char in ascii_lowercase:
                counter += 1
        return counter >= self.rule.min_number_of_lowercase_char

    def num_uppercase_is_valid(self, password: str) -> bool:
        """This method check if the password has a minimum number of uppercase charcakters.

        Args:
            password (str): password to be checked

        Returns:
            bool: True if there is a minimum number of uppercase characters in the password,
            False otherwise
        """
        counter = 0
        for char in password:
            if char in ascii_uppercase:
                counter += 1
        return counter >= self.rule.min_number_of_uppercase_char

    def leakage_valid(self, password: str) -> bool:
        """_summary_

        Args:
            password (str): password to check for leaks

        Returns:
            bool: True if number of leaks is <= than the rules specified
        """
        my_hash = self.hash_pwd(password)
        response = get("https://api.pwnedpasswords.com/range/" + my_hash[:5])

        for line in response.text:
            if (
                line.split(":")[0] == my_hash
                and line.split(":")[1] > self.max_number_of_password_leak
            ):
                return False
        return True

    def valid(self, password) -> bool:
        return all([
            self.length_is_valid(password),
            self.num_digits_is_valid(password),
            self.num_special_char_is_valid(password),
            self.num_lowercase_is_valid(password),
            self.num_uppercase_is_valid(password)
        ])
