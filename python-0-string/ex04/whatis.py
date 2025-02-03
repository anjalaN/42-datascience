#!/usr/bin/env python3
import sys

def main():
    # Check if exactly one argument is provided
    if len(sys.argv) != 2:
        raise AssertionError("Only one argument is allowed.")

    # Extract the argument
    argument = sys.argv[1]

    try:
        # Try to convert the argument to an integer
        number = int(argument)
    except ValueError:
        # Raise an error if the argument is not an integer
        raise AssertionError("Argument must be an integer.")

    # Check if the number is odd or even
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()
