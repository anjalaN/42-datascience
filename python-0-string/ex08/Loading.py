#!/usr/bin/env python3
def ft_tqdm(lst: range) -> None:
    total = len(lst)  # Get the total length of the iterable
    for i, item in enumerate(lst):
        percent = (i + 1) / total * 100  # Calculate percentage
        bar = '=' * (i + 1)  # Simple progress bar
        spaces = ' ' * (total - (i + 1))  # Remaining spaces
        # Print progress bar like tqdm
        print(f"\r[{bar}{spaces}] {percent:.2f}% ({i + 1}/{total})", end="")
        yield item  # Yield the current element
    print()  # To move to the next line after the loop is done



