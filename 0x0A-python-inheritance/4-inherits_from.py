#!/usr/bin/python3

"""
Checks if the object is an instance of a subclass
"""


def inherits_from(obj, a_class):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
