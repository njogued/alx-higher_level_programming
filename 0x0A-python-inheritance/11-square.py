#!/usr/bin/python3
"""Inheris from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class to define a square using rectangle"""

    def __init__(self, size):
        """Intialize a new square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        hxw = self.__size * self.__size
        return(hxw)

    def __str__(self):
        return("[Square] " + str(self.__size) + "/" + str(self.__size))
