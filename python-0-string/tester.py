#!/usr/bin/env python3
from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

NULL_not_found(Nothing)  # Should print <class 'NoneType'> and return 0
NULL_not_found(Garlic)   # Should print <class 'float'> and return 0
NULL_not_found(Zero)     # Should print <class 'int'> and return 0
NULL_not_found(Empty)    # Should print <class 'str'> and return 0
NULL_not_found(Fake)     # Should print <class 'bool'> and return 0

print(NULL_not_found("Brian"))  # Should print <class 'str'> and return 1
