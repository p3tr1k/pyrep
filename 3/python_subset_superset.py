#!/usr/bin/python3

set1 = { 'a', 'b', 'c', 'd', 'e' }
set2 = { 'a', 'b', 'c' }
set3 = {'x', 'y', 'z' }

if (set2.issubset(set1)):
    print("set2 is a subset of set2")
    
if (set1.issuperset(set2)):
    print("set1 is a superset of set2")    
    
if (set2.isdisjoint(set3)):
    print("set2 and set3 have no common elements") 