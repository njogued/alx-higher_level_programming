#!/usr/bin/python3
'''
Module contains the FileStorage class
'''
import json
class FileStorage:
    '''
    Class for json.dump and json.load
    '''
    __file_path = ""
    __objects = {}

    def all(self):
        '''
        Will return _objects dictionary
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets the obj in objects
        '''
        obj_name = f"{obj.__class.__name__}.{obj.id}"
        self.__objects[obj_name] = obj.to_dict() 

    def save(self):
        '''
        Serialize the objects to JSON file (__file_path)
        '''
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        '''
        Deserialize the JSON file to objects
        '''
        if self.__file_path:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        else:
            pass
