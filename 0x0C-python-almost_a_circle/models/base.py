#!/usr/bin/python3

'''
Module with class and init methods
'''

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor method """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        elif type(id) is int and id != None:
            self.id = id
