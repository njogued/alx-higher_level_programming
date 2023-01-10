#!/usr/bin/python3

"""
Function that reads a file
"""


def read_file(filename=""):
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    with open(filename, "r") as file_1:
        print(file_1.read(), end="")
