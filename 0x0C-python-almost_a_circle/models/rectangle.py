#!/usr/bin/python3

"""
Rectangle class inheriting from square class
"""
import sys
sys.path.append("..")
Base = __import__("base").Base


class Rectangle(Base):
    """The class inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init the instances using the class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
