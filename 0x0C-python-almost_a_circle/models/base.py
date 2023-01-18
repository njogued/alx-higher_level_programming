#!/usr/bin/python3

'''
Module with class and init methods
'''
import json


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
    
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for i in list_objs:
                result.append(cls.to_dictionary(i))

        with open(filename, "w") as f:
            f.write(cls.to_json_string(result))
