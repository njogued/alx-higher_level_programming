#!/usr/bin/python3

"""
Function to append a string to a text file
"""


def append_write(filename="", text=""):
    """ python3 -c 'print(__import__('module').function.__doc__)'
    """
    with open(filename, "a", encoding="utf-8") as file_1:
        return file_1.write(text)
