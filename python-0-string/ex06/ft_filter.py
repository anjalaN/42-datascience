#!/usr/bin/env python3
def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which 
    function(item) is true."""
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))


# Exemple d'utilisation
def is_odd(num):
    return num % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
result = ft_filter(is_odd, numbers)
print(list(result))
