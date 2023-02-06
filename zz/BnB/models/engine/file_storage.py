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
        pass

    def save(self):
        '''
        Serialize the objects to JSON file (__file_path)
        '''
        pass

    def reload(self):
        '''
        Deserialize the JSON file to objects
        '''
        pass
