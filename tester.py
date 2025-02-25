#!/usr/bin/env python3

import array2D

def test_slice_me():
    """
    Test the slice_me function with various test cases.
    """
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    # Test case 1
    result = array2D.slice_me(family, 0, 2)
    assert result == [[1.80, 78.4], [2.15, 102.7]], f"Test case 1 failed: {result}"

    # Test case 2
    result = array2D.slice_me(family, 1, -2)
    assert result == [[2.15, 102.7]], f"Test case 2 failed: {result}"

    print("All tests passed!")

def main():
    """
    Main function to run all tests.
    """
    try:
        test_slice_me()
    except Exception as e:
        print(f"An error occurred during testing: {e}")

if __name__ == "__main__":
    main()
