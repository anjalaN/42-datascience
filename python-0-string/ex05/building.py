#/usr/bin/env python3
import sys
import string

def main():
    try:
        # Check if the number of arguments is valid
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        
        # If no arguments are provided, prompt the user for input
        if len(sys.argv) < 2:
            user_input = input("Please enter a string: ")
        else:
            user_input = sys.argv[1]
        
        # Initialize counters for each category
        upper_case_count = 0
        lower_case_count = 0
        punctuation_count = 0
        digit_count = 0
        space_count = 0
        
        
        # Iterate over each character in the input string
        for char in user_input:
            if char.isupper():
                upper_case_count += 1
            elif char.islower():
                lower_case_count += 1
            elif char in string.punctuation:
                punctuation_count += 1
            elif char.isdigit():
                digit_count += 1
            elif char.isspace():
                space_count += 1
        #calculatte the total count number of charactors
        totalt_characters = len(user_input)

        # Display the counts for each category
        print(f"The  text contains {totalt_characters} characters:")
        print(f"{upper_case_count} Upper-case characters: ")
        print(f"{lower_case_count} Lower-case characters: ")
        print(f"{punctuation_count} Punctuation characters: ")
        print(f"{space_count} Spaces: ")
        print(f"{digit_count} Digits: ")
        

    except AssertionError as e:
        # Handle the case where more than one argument is provided
        print(e)

if __name__ == "__main__":
    main()
