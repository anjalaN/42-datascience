#!/usr/bin/env python3

# import sys
# 
# def morse_encode(text):
    # assert isinstance(text, str), "AssertionError: Argument must be a string"
    # NESTED_MORSE = {
        # "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        # "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
        # "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        # "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
        # "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        # "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        # "Y": "-.-- ", "Z": "--.. ",
        # "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        # "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        # "8": "---.. ", "9": "----. ",
        # " ": "/ "
    # }
    # return "".join(NESTED_MORSE[char.upper()] for char in text if char.upper() in NESTED_MORSE).strip()
# 
# if __name__ == "__main__":
    # assert len(sys.argv) == 2, "AssertionError: Wrong number of arguments"
    # print(morse_encode(sys.argv[1]))
# 

import sys

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code.strip()

# Main function to handle arguments
def main():
    if len(sys.argv) < 2:
        print("Please provide text to convert to Morse code.")
        return
    
    text = sys.argv[1]  # Get the input text from the command line
    morse = text_to_morse(text)  # Convert text to Morse code
    print(f"Text: {text}")
    print(f"Morse Code: {morse}")

if __name__ == "__main__":
    main()


# Letter	Morse Code	Letter	Morse Code
# A	.-	N	-.
# B	-...	O	---
# C	-.-.	P	.--.
# D	-..	Q	--.-
# E	.	R	.-.
# F	..-.	S	...
# G	--.	T	-
# H	....	U	..-
# I	..	V	...-
# J	.---	W	.--
# K	-.-	X	-..-
# L	.-..	Y	-.--
# M	--	Z	--..
# 
# For Numbers:
# Number	Morse Code
# 0	-----
# 1	.----
# 2	..---
# 3	...--
# 4	....-
# 5	.....
# 6	-....
# 7	--...
# 8	---..
# 9	----.
# 
# Special Characters:
# Symbol	Morse Code
# Space	/
# Period .	.-.-.-
# Comma ,	--..--
# Question ?	..--..