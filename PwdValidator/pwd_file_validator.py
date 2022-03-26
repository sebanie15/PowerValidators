# from .pwd_validator import PwdValidator


class PwdFileManager:
    """_summary_"""

    def __init__(self, filename, mode) -> None:
        """Initialization of PwdFileValidation object."""
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """_summary_"""
        # open and share contents of the file
        self.file = open(self.filename, self.mode)
        return self.file.readlines()

    def __exit__(self, exc_type, exc_value, trace):
        """_summary_

        Args:
            exc_type (_type_): _description_
            exc_value (_type_): _description_
            trace (_type_): _description_
        """
        # clear sources
        self.file.close()

    def __iter__(self):
        return self

    def read_password_from_file(self, filename: str = ""):
        """_summary_

        Args:
            filename (str, optional): _description_. Defaults to ''.
        """
