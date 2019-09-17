#!/usr/bin/python3

from prettytable import from_csv
    
with open("data.csv", "r") as fp: 
    x = from_csv(fp)

print(type(x))
x.sortby = "Population"
    
print(x)