#!/usr/bin/env python

# iterator.py

_str = "formidable"

for e in _str:
   print(e, end=" ")

print()

mytuple = ("apple", "banana", "orange")
myit = iter(mytuple)

print()

it = iter(_str)
print(next(it))
print(next(it))
print(next(it))
print(list(it))

print()

print(next(myit))
print(next(myit))
print(next(myit))
