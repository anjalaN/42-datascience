
from typing import Iterable


def ft_tqdm(lst: Iterable) -> Iterable:
    total = len(lst)
    count = 0
    for item in lst:
        count += 1
        # Calculate the progress percentage
        percent = (count / total) * 100
        # Create a progress bar (a string of '=' characters)
        bar_length = 40  # Bar length in characters
        bar_fill = '=' * int(bar_length * percent // 100)
        bar_empty = ' ' * (bar_length - int(bar_length * percent // 100))
        bar = bar_fill + bar_empty

        # Print the progress bar on the same line
        print(f'\r|{bar}| {percent:.2f}% {count}/{total}', end='', flush=True)
        yield item  # Yield each item so it can be iterated over
    print()  # To move to a new line after the progress bar completes
