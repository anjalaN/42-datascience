#!/usr/bin/env python3

import sys
import string


def count_characters(input_str):
    """
    Count the number of characters in each category in the input string.

    :param input_str: The input string to analyze.
    :return: A dictionary containing the counts for each category.
    """
    counts = {
        "upper_case": 0,
        "lower_case": 0,
        "punctuation": 0,
        "digit": 0,
        "space": 0
    }
    for char in input_str:
        if char.isupper():
            counts["upper_case"] += 1
        elif char.islower():
            counts["lower_case"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1
        elif char.isdigit():
            counts["digit"] += 1
        elif char.isspace():
            counts["space"] += 1

    return counts


def display_counts(input_str):
    """
    Display the counts for each character category in the input string.

    :param input_str: The input string to analyze.
    """
    counts = count_characters(input_str)
    total_characters = len(input_str)

    print(f"The text contains {total_characters} characters:")
    print(f"{counts['upper_case']} Upper-case characters")
    print(f"{counts['lower_case']} Lower-case characters")
    print(f"{counts['punctuation']} Punctuation characters")
    print(f"{counts['space']} Spaces")
    print(f"{counts['digit']} Digits")


def main():
    """
    Main function to handle user input and display character counts.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) < 2:
            user_input = input("Please enter a string: ")
        else:
            user_input = sys.argv[1]
        display_counts(user_input)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
