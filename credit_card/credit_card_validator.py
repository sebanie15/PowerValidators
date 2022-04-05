"""
Credit card validation - how to do it?
Nowadays - a standard payment card is defined by ISO IEC_7812 standards. So according to the ISO standard, length
credit card number is 16 digits. It is validated by the so-called Luhn's algorithm. Therefore, similar to the PESEL 
algorithm, at the end of the sequence of numbers there is a check digit. With its help, it is also possible to calculate
the IMEI number visible on cell phones.
Example of a credit card number: 6123 2462 0532 2891:
    6 - Economy Domain Identifier - informs about the field accompanied by the card number:
        1,2 - airlines,
        3 - travel and entertainment,
        4, 5 - banking, finance,
        6 - trade, banking,
        7 - oil industry,
        8 - telecommunications,
        9 - to be determined by standardization bodies,
    123 24 - Publisher Identification Number, e.g. MasterCard, Visa,
    62 0532 289 - Personal Account Identifier, an individual number assigned to a specific personal account,
    1 - check digit
The number is validated by doubling the digits in the even places in the card number.
The number 9 is subtracted from products greater than 9. All digits are added up in sequence - including those on
odd positions. To the obtained number, add such a digit that the result is a multiple of 10.
The added number is a check digit.
source: https://www.czerwona-skarbonka.pl/walidator-danych-walidacja-pesel-regon-nip-krok-po-kroku/
"""

from validator_base import Validator
from text_validator import DigitsValidator

from .credit_card_exceptions import CreditCardException


class CreditCardValidator(Validator):
    """class summary"""

    CC_NUMBER_LENGTH = 16 

    def __init__(self, cc_number: str):
        self.cc_number = cc_number

    def checksum(self) -> int:
        """the function calculates a checksum for the credit card
        Args:
            cc_number: int
        Returns:
            int
        """
        odd_digits = [int(odd_digit) for odd_digit in self.cc_number[1:-1:2]]
        even_digits = [
            int(even_digit) * 2 if int(even_digit) * 2 <= 9 else int(even_digit) * 2 - 9
            for even_digit in str(self.cc_number)[:-1:2]
        ]
        sum_of_digits = sum(odd_digits) + sum(even_digits)

        return 10 - (sum_of_digits % 10)

    def is_valid(self) -> bool:
        """the function checks if the card number has 16 characters and if the check sum \
            is consistent with the sum digit in the card number

        Returns:
            bool
        """
        if DigitsValidator(self.cc_number, occurrences=self.CC_NUMBER_LENGTH).is_valid():
            checksum_number = int(self.cc_number[-1])
            if checksum_number == self.checksum(self.cc_number):
                return True
        
        raise CreditCardException()
