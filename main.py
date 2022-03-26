from wsgiref.validate import validator
from PwdValidator import PwdValidator, PwdFileManager, haveibeenpwned, hash_pwd
import string


validator = PwdValidator()
print(validator.rule)

with PwdFileManager("passwords.txt", "r") as passwords, open(
    "safe_passwords.txt", mode="w"
) as safe_passwords:
    for password in passwords:
        if validator.valid(password) and haveibeenpwned(password):
            safe_passwords.write(
                f" password: {password.strip():<30} is safe, hash of password is: {hash_pwd(password)}\n"
            )
