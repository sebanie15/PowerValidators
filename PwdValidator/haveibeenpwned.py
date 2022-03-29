"""Module haveibeenpwned is used to check if password has leakage on
page https://haveibeenpwned.com/API/v3
"""

from hashlib import sha1
from requests import get
from .pwd_exceptions import HaveIbeenPwnedException


def hash_pwd(password: str) -> str:
    """This method returns the hash of password.
        It yused sha1 algorithm

    Args:
        password (str): password to be hashed

    Returns:
        str: hash of password
    """
    return sha1(password.encode(encoding="utf-8")).hexdigest()


def haveibeenpwned(password: str) -> bool:
    """_summary_

    Args:
        password (str): password to check for leaks

    Returns:
        bool: False if there was no leak, otherwise True
    """
    my_hash = sha1(password.encode(encoding="utf-8")).hexdigest().upper()
    response = get("https://api.pwnedpasswords.com/range/" + my_hash[:5])

    for line in response.text.splitlines():
        if my_hash[5:] == line.split(':')[0]:
            return True
    return False
