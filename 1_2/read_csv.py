#!/usr/bin/python3

import csv

f = open('numbers.csv', 'r')

mysum = 0
with f:

    reader = csv.reader(f,delimiter="|")

    for row in reader:
        for e in row:
            mysum += int(e)

print(mysum)