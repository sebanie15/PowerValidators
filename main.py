from calendar import c
from wsgiref.validate import validator
from PwdValidator import PwdValidator, PwdFileManager, haveibeenpwned, hash_pwd


# Print iterations progress - source: stackoverflow
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


validator = PwdValidator()
print(validator.rule)

with PwdFileManager("passwords.txt", "r") as passwords, open(
    "safe_passwords.txt", mode="w"
) as safe_passwords:
    # counter for status bar
    counter = 0
    printProgressBar(counter, len(passwords), prefix = 'Progress:', suffix = 'Complete', length = 100)
    for password in passwords:
        # check if password is valid with rules and has been leakage on haveibeenpwned
        if validator.is_valid(password) and haveibeenpwned(password):
            safe_passwords.write(
                f" password: {password.strip():<30} is safe, hash of password is: {hash_pwd(password)}\n"
            )
        counter += 1
        printProgressBar(counter, len(passwords), prefix = 'Progress:', suffix = 'Complete', length = 100)
