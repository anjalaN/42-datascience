#!/usr/bin/env python3
def NULL_not_found(object: any) -> int:
    try:
        # Print the type of the object
        print(f"Object type: {type(object)}")

        # Check for null-like values
        if object is None:  # None type
            return 0
        elif isinstance(object, float) and object != object:  # NaN check
            return 0
        elif object == 0:  # Zero (int or float)
            return 0
        elif object == '':  # Empty string
            return 0
        elif object is False:  # Boolean False
            return 0

        # If the object doesn't match any "null" type
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
