#!/usr/bin/env python3
import math


def NULL_not_found(object: any) -> any:
    # handling None explicitly
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0
    # handle Nan (not a number) explicitly using math.isnan()
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: nan {type(object)}")
        return 0
    # Handle false explicitly
    elif object is False:
        print(f"Fake: False {type(object)}")
        return 0
    # handle zero explicitly
    elif object == 0:
        print(f"Zero: 0 {type(object)}")
        return 0
    # handle empty
    elif object == '':
        print(f"Empty: {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
