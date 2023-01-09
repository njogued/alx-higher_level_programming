#!/usr/bin/python3

"""
Function that inherits from list, sorts, and prints
"""


class MyList(list):
    def __init__(self, iterable=[]):
        """Constructor"""
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
