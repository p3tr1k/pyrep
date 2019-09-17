#!/usr/bin/python3

# read_csv3.py

import csv

f = open('values.csv', 'r')

with f:

    reader = csv.DictReader(f)
    f1, f2, f3 = reader.fieldnames
    for row in reader:
        print(row[f1], row[f2], row[f3])