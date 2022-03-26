"""Using PWDValidator
"""

from wsgiref.validate import validator
from PwdValidator import PwdValidator, PwdFileManager, haveibeenpwned, hash_pwd


# Print iterations progress - source: stackoverflow
def print_progress_bar(
    iteration: int,
    total: int,
    prefix: str = "Progress",
    suffix: str = "Complete",
    length: int = 50
):
    """
    Call in a loop to create terminal progress bar
    Args:
        iteration (int): current iteration
        total (int) : total iterations
        prefix (str) : prefix string
        suffix (str) : suffix string
        length (str) : character length of bar
    """
    fill: str = "█"
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / total))
    filled_length = int(length * iteration // total)
    prog_bar = fill * filled_length + "-" * (length - filled_length)
    print(f"\r{prefix} |{prog_bar}| {percent}% {suffix}", end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


validator = PwdValidator()
# validator.rule.min_length_of_pwd = 10
# validator.rule.min_number_of_digits = 3

print(validator.rule)

with PwdFileManager("passwords.txt", "r") as passwords, open(
    file="safe_passwords.txt", mode="w", encoding="ascii"
) as safe_passwords:
    # counter for status bar
    counter = 0
    print_progress_bar(counter, len(passwords))
    for password in passwords:
        # check if password is valid with rules and has been leakage on haveibeenpwned
        if validator.is_valid(password) and not haveibeenpwned(password):
            safe_passwords.write(
                f" password: {password.strip():<30} is safe, hash of password is: "
                f"{hash_pwd(password)}\n"
            )
        counter += 1
        print_progress_bar(counter, len(passwords))
