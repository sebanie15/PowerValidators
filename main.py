"""Using PWDValidator
"""

from wsgiref.validate import validator
from PwdValidator import PwdValidator, PwdFileManager, haveibeenpwned, hash_pwd

from progress_bar import print_progress_bar


validator = PwdValidator()
# validator.rule.min_length_of_pwd = 10
validator.rule.min_number_of_special_char = 1

print(validator.rule)

with PwdFileManager("passwords.txt", "r") as passwords, open(
    file="safe_passwords.txt", mode="w", encoding="ascii"
) as safe_passwords:
    # counter for status bar
    counter = 0
    if len(passwords) > 0:
        

        print_progress_bar(counter, len(passwords))
        for password in passwords:
            # check if password is valid with rules and has been leakage on haveibeenpwned
            if validator.validate(password) and not haveibeenpwned(password):
                safe_passwords.write(
                    f" password: {password.strip():<30} is safe, hash of password is: "
                    f"{hash_pwd(password)}\n"
                )
            counter += 1
            print_progress_bar(counter, len(passwords))
    else:
        print('No passwords in file!')
