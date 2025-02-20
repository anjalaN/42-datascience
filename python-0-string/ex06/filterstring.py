#!/usr/bin/env python3
import sys


def world_longer_than_n(s, n):
    words = s.split()  # Split string into words
    result = [word for word in words if len(word) > n]
    return result


if __name__ == "__main__":
    try:
        # Check if the number of arguments is exactly 3
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        s = sys.argv[1]  # First argument should be the string
        assert not s.isdigit(), (
            "AssertionError: the first argument must be a string"
            )
        n = int(sys.argv[2])  # Second argument should be an integer
    except (AssertionError, ValueError) as e:
        # Print the error message and exit if there's an issue
        print(e)
        sys.exit(1)
    # Use list comprehension with a lambda function for filtering
    filtered_words = list(
        filter(
            lambda word: len(word) > n, s.split()
            )
    )
    # Print the filtered and sorted words
    print(filtered_words)
