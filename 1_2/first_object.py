#!/usr/bin/env python

# first_object.py

class Obdlznik:

    def __init__(self, a=2, b=1):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b

    def set_a(self,a):
        self.a = a
    
    def set_b(self,b):
        self.b = b

    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b

o = Obdlznik()
o.set_a(4)
o.set_b(3)


print(f"Obdlznik so stranou a = {o.get_a()} a b = {o.get_b()} je {o.area()}.")
