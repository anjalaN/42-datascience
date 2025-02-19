#!/usr/bin/env python3

# def all_thing_is_obj(object: any) -> int:
#     print(object)
# if isinstance(object, list):
#     print(f"List : {type(object)}")
# elif isinstance(object, tuple):
#     print(f"Tuple : {type(object)}")
# elif isinstance(object, set):
#     print(f"Set : {type(object)}")
# elif isinstance(object, dict):
#     print(f"Dict : {type(object)}")
# elif isinstance(object, str):
#     print(f"Brain in the kitchen : {type(object)}")
# elif object == "Toto":
#     print(f"Toto is in the kitchen: {type(object)}")
# else:
#     print("Type not found")
#     return 42

#!/usr/bin/env python3
import math

def find_ft_type(object: any) -> any:
    # Handle None explicitly
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0
    
    # Handle NaN (Not a Number) explicitly using math.isnan()
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: nan {type(object)}")
        return 0
    
    # Handle False explicitly
    elif object is False:
        print(f"Fake: False {type(object)}")
        return 0
    
    # Handle zero explicitly
    elif object == 0:
        print(f"Zero: 0 {type(object)}")
        return 0
    
    # Handle empty string
    elif object == '':
        print(f"Empty: {type(object)}")
        return 0
    
    # Handle "Brain" in the kitchen
    elif object == "Brain":
        print(f"Brain is in the kitchen : {type(object)}")
        return 0
    
    # Handle "Toto" in the kitchen
    elif object == "Toto":
        print(f"Toto is in the kitchen : {type(object)}")
        return 0
    
    # Explicitly handle lists, tuples, sets, and dicts
    elif isinstance(object, list):
        print(f"List : {type(object)}")
        return 0
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
        return 0
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
        return 0
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
        return 0
    
    # Return 1 when type is not found
    else:
        print("Type not found$")
        return 1
