#!/usr/bin/python3

"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class BaseGeometry:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    def area(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validator function
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
