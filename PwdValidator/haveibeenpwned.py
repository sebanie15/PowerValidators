"""Module haveibeenpwned is used to check if password has leakage on
page https://haveibeenpwned.com/API/v3
"""

from hashlib import sha1
from requests import get


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
        bool: True if number of leaks is <= than the rules specified
    """
    my_hash = hash_pwd(password)
    response = get("https://api.pwnedpasswords.com/range/" + my_hash[:5])

    for line in response.text:
        if line.split(":")[0] == my_hash and line.split(":")[1] > 0:
            return False
    return True
