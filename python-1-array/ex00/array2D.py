#!/usr/bin/env python3
import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice the 2D array based on the provided start and end indices.

    Parameters:
    family (list[list[int | float]]): 2D array to be sliced.
    start (int): Starting index for slicing.
    end (int): Ending index for slicing.

    Returns:
    list[list[int | float]]: Sliced 2D array.
    """
    try:
        family_array = np.array(family)  # Convert the list to a NumPy array
        print(f"My shape is : {family_array.shape}")  # Print the shape of the array
        sliced_array = family_array[start:end]   # Slice array using start and end indices
        print(f"My new shape is : {sliced_array.shape}")
        return sliced_array.tolist()  # Convert the sliced array back to a list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    """
    Main function to run example usage and handle exceptions.
    """
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(f"An error occurred during the main execution: {e}")

if __name__ == "__main__":
    main()
