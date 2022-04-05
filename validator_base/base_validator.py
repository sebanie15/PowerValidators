""" Abstract class of validator """

from abc import ABC, abstractmethod


class Validator(ABC):
    """Validator interface"""

    @abstractmethod
    def __init__(self, text: str) -> None:
        """A forced method for all classes that inherit from Validator class

        Args:
            text (str): text to be validated.
        """

    @abstractmethod
    def is_valid(self) -> bool:
        """A forced method for all classes that inherit from Validator classes
        This is the method that validates.

        Returns:
            bool: True if value is valid, otherwise raise exception
            
        """
