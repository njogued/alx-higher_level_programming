#!/usr/bin/python3

"""
python3 -c 'print(__import__("my_module").__doc__)')
Function that inherits from list, sorts, and prints
"""


class MyList(list):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    def print_sorted(self):
        """python3 -c 'print(__import__("my_module").\
            my_function.__doc__)'\
            python3 -c 'print(__import__("my_module").\
                MyClass.my_function.__doc__)')"""
        print(sorted(self))
