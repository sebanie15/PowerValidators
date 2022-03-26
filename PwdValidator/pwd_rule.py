
from .pwd_exceptions import MinLengthException


class PwdRule:
    """_summary_

    Returns:
        _type_: _description_
    """

    DEFAULT_MIN_LENGTH = 8
    DEFAULT_MIN_NUM_OF_DIGITS = 2
    DEFAULT_MIN_NUM_OF_PUNCTUATION = 2
    DEFAULT_MIN_NUM_OF_LOWERCASE = 2
    DEFAULT_MIN_NUM_OF_UPPERCASE = 2
    DEFAULT_MAX_LEAKAGE = 0

    def __init__(
        self,
        min_length_of_pwd: int = DEFAULT_MIN_LENGTH,
        min_number_of_digits: int = DEFAULT_MIN_NUM_OF_DIGITS,
        min_number_of_special_char: int = DEFAULT_MIN_NUM_OF_PUNCTUATION,
        min_number_of_lowercase_chars: int = DEFAULT_MIN_NUM_OF_LOWERCASE,
        min_number_of_uppercase_chars: int = DEFAULT_MIN_NUM_OF_UPPERCASE,
        max_number_of_password_leak: int = DEFAULT_MAX_LEAKAGE,
    ):
        """_summary_

        Args:
            min_length_of_pwd (int): _description_. Defaults to DEFAULT_MIN_NUM_OF_UPPERCASE.
            min_number_of_digits (int): _description_. Defaults to DEFAULT_MIN_NUM_OF_DIGITS.
            min_number_of_special_char (int): _description_. Defaults to DEFAULT_MIN_NUM_OF_PUNCTUATION.
            min_number_of_lowercase_chars (int): _description_. Defaults to DEFAULT_MIN_NUM_OF_LOWERCASE.
            min_number_of_uppercase_chars (int): _description_. Defaults to DEFAULT_MIN_NUM_OF_UPPERCASE.
            max_number_of_password_leak (int): _description_. Defaults to DEFAULT_MAX_LEAKAGE.
        """
        # self._min_length_of_pwd = min_length_of_pwd
        self._min_number_of_digits = self.DEFAULT_MIN_NUM_OF_DIGITS
        self._min_number_of_special_char = self.DEFAULT_MIN_NUM_OF_PUNCTUATION
        self._min_number_of_lowercase = self.DEFAULT_MIN_NUM_OF_LOWERCASE
        self._min_number_of_uppercase = self.DEFAULT_MIN_NUM_OF_UPPERCASE

        self.min_length_of_pwd = min_length_of_pwd

        if self._min_number_of_digits != min_number_of_digits:
            self.min_number_of_digits = min_number_of_digits
        if self._min_number_of_special_char != min_number_of_special_char:
            self.min_number_of_special_char = min_number_of_special_char
        if self._min_number_of_lowercase != min_number_of_lowercase_chars:
            self.min_number_of_lowercase_char = min_number_of_lowercase_chars
        if self._min_number_of_uppercase != min_number_of_uppercase_chars:
            self.min_number_of_upercase_char = min_number_of_uppercase_chars

        self._max_number_of_password_leak = max_number_of_password_leak

    @property
    def rules(self) -> dict:
        return {
            'minimum length of password': self._min_length_of_pwd,
            'minimum number of digits': self._min_number_of_digits,
            'minimum number of special characters': self._min_number_of_special_char,
            'minimum number of lowercase': self._min_number_of_lowercase,
            'minimum number of uppercase': self._min_number_of_uppercase
        }

    def __str__(self):
        return f'PwdRule: {self.rules}'

    def __repr__(self):
        return f'PwdRule: {self.rules}'

    def __sum_of_criteria_length(self) -> int:
        """ This method sum the numbers of every criteria of the password rule

        Returns:
            int: sum of criteria
        """
        if self.__set_min_numbers_of_digits is None:
            print('nie ma jeszcze min digits')
        return (
            self._min_number_of_digits
            + self._min_number_of_special_char
            + self._min_number_of_lowercase
            + self._min_number_of_uppercase
        )

    def set_attr(self, name, value):
        """_summary_

        Args:
            name (str): atribute name
            value (int): value to be set

        Raises:
            MinLengthException: _description_
        """
        difference = value - self.__getattribute__(name)
        if self.__getattribute__(name) < self.__sum_of_criteria_length() + difference:
            raise MinLengthException
        self.__setattribute__(name, value)      

    @property
    def min_length_of_pwd(self) -> int:
        """ Value of the property that specifies the minimum password length.

        Returns:
            int: _description_
        """
        return self._min_length_of_pwd

    @min_length_of_pwd.setter
    def min_length_of_pwd(self, value: int):
        """ Setter to specify the minimum length of password.

        Args:
            value (int): minimum length of password to be set
        """
        # self.__set_min_length(value)
        if value < self.DEFAULT_MIN_LENGTH:
            self._min_length_of_pwd = self.DEFAULT_MIN_LENGTH
            raise MinLengthException
        self._min_length_of_pwd = value

    @property
    def min_number_of_digits(self) -> int:
        """ Value to the property that specifies the minimum number of digits
            in the password.

        Returns:
            int: Minimum number of digits in the password.
        """
        return self._min_number_of_digits

    @min_number_of_digits.setter
    def min_number_of_digits(self, value: int):
        """ Setter to specify the minimum number of digits in the password.

        Args:
            value (int): Minimum number of digits in the password to be set.
        """
        self.set_attr('_min_length_of_pwd', value)

    @property
    def min_number_of_special_char(self) -> int:
        """ Value of the property that specifies the minimum number of special
            characters (punctuation) in the password.

        Returns:
            int: Minimum number of special characters in the password.
        """
        return self._min_number_of_special_char

    @min_number_of_special_char.setter
    def min_number_of_special_char(self, value: int):
        """ Setter to specify the minimum number of special characters in the password

        Args:
            value (int): Minimum number of special characters  in the password to be set.
        """
        self.set_attr('_min_number_of_special_char', value)

    @property
    def min_number_of_lowercase_char(self) -> int:
        """ Return value of the property that specifies the minimum number of
            lowercase characters in the password.

        Returns:
            int: Minimum number of lowercase characters
        """
        return self._min_number_of_lowercase

    @min_number_of_lowercase_char.setter
    def min_number_of_lowercase_char(self, value: int):
        """ Setter to specify the minimum number of lowercase characters in the password.

        Args:
            value (int): Minimum number of lowercase characters in the password to be set.
        """
        self.set_attr('_min_number_of_lowercase', value)

    @property
    def min_number_of_uppercase_char(self) -> int:
        """ Return value of the property that specifies the minimum number of
            uppercase characters in the password.

        Returns:
            int: Minimum number of uppercase characters in the password.
        """
        return self._min_number_of_uppercase

    @min_number_of_uppercase_char.setter
    def min_number_of_uppercase_char(self, value: int):
        """ Setter to specify the minimum number of uppercase characters in the password.

        Args:
            value (int): Minimu number of uppercase characters in the password.
        """
        self.set_attr('_min_number_of_upercase', value)
