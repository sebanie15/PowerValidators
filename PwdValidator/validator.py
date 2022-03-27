"""

"""

from abc import ABC, abstractmethod


class ValidatorInterface(ABC):

    @abstractmethod
    def validate(self, value) -> bool:
        """This is required method to validation

        Args:
            value (_type_): value to validate

        Returns:
            bool: True if value is valid, False otherwise.
        """
