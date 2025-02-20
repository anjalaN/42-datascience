#!/usr/bin/env python3

class myClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"hell, {self.name}"


my_object = myClass('johan')
my_object.name = 'anjala'

print(my_object.name)
setattr(my_object, 'name', 'niro')
print(my_object.greet())
