from PwdValidator import PwdValidator, PwdFileManager, haveibeenpwned, hash_pwd
import string


valid = PwdValidator()
print(valid.rule)

with PwdFileManager('passwords.txt', 'r') as passwords, open('save_passwords.txt', mode='w') as save_passwords:
    for password in passwords:
        if valid.valid(password) and haveibeenpwned(password):
            save_passwords.write(
                f' password: {password.strip():<30} is safe, hash of password is: {hash_pwd(password)}\n')
