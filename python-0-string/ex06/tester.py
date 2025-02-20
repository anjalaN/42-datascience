#!/usr/bin/env python3
# from ft_filter import ft_filter
# original = filter.__doc__
# copy = ft_filter.__doc__
# print(copy)
# print(original)
# print(original == copy)

from ft_filter import ft_filter

original = filter.__doc__.strip()
copy = ft_filter.__doc__.strip()

print(copy)
print(original)
print(original == copy)

