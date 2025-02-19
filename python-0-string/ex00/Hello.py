#!/usr/bin/env python3
#list 
ft_list = ["Hello", "tata!"]
ft_list[1] = "World!"

#tuple before convertis to list for modification
ft_tuple = ("hello", "toto!")
list = list(ft_tuple)
list[1] = "France!"
ft_tuple = tuple(list)

#set
ft_set = {"Hello", "tutu"}
ft_set.remove("tutu")
ft_set.add("Paris!")

#dictionart
ft_dict = {"Hello": "titi"}
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

