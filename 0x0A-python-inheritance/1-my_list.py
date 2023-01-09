#!/usr/bin/python3

"""
Function that inherits from list, sorts, and prints
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
