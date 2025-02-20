#!/usr/bin/env python3
import sys

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "c": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"

}


# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = []
    for char in text.upper():  # Convert text to uppercase for matching Morse
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            raise AssertionError(
                f"the arguments are bad: invalid character '{char}'"
            )  # Invalid character
    return " ".join(morse_code)


# Main function to handle arguments
def main():
    if len(sys.argv) != 2:  # Check if there is exactly 1 argument
        raise AssertionError("the arguments are bad")
    text = sys.argv[1]  # Get the input text from the command line
    # Convert text to Morse code
    try:
        morse = text_to_morse(text)
        print(f"Text: {text}")
        print(f"Morse Code: {morse}")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
