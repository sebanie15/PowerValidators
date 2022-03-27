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
