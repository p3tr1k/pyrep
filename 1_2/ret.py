#!/usr/bin/env python

"""
The ret.py script shows how to work with
functions in Python.
Author: Jan Bodnar
ZetCode, 2019
"""


def show_module_name():

    print(__doc__)


def get_module_file():

    return __file__


a = show_module_name()
b = get_module_file()

print(a, b)