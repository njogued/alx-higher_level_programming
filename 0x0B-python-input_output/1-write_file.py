#!/usr/bin/python3

"""
Function to write a string to a text file
"""


def write_file(filename="", text=""):
    """ python3 -c 'print(__import__('module').function.__doc__)'
    """
    with open(filename, "w", encoding="utf-8") as file_1:
        return file_1.write(text)
