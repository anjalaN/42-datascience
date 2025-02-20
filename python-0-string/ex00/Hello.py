#!/usr/bin/env python3
ft_list = ["Hello", "tata!"]
ft_list[1] = "World!"

ft_tuple = ("hello", "toto!")
list = list(ft_tuple)
list[1] = "France!"
ft_tuple = tuple(list)

ft_set = {"Hello", "tutu"}
ft_set.remove("tutu")
ft_set.add("Paris!")

ft_dict = {"Hello": "titi"}
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
