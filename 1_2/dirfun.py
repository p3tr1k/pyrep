#!/usr/bin/env python

# """
# This is dirfun module 
# """

from empty import Dog, Cat

class Monkey:
    pass

dog = Dog()
cat = Cat()
monkey = Monkey()

# version = 1.0

# names = ["Paul", "Frank", "Jessica", "Thomas", "Katherine"]

# def show_names():
  
#    for i in names:
#       print(i)

print(dog.__module__)
print(cat.__module__)
print(monkey.__module__)