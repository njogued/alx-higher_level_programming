#!/usr/bin/python3

"""
Module with append after function that\
searches a for a string and appends text\
after the line
"""


def append_after(filename="", search_string="", new_string=""):
    """python3 -c 'print(__import__(Module).function.__doc__)'"""
    text = ""
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line.strip()
            if search_string in line:
                line = line + new_string
            text += line
            print(line)
    with open(filename, "w") as f:
        f.write(text)
