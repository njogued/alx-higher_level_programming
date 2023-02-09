#!/usr/bin/python3
'''
Module contains the FileStorage class
'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''
    Class for json.dump and json.load
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Will return _objects dictionary
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Sets the obj in objects
        '''
        obj_name = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_name] = obj

    def save(self):
        '''
        Serialize the objects to JSON file (__file_path)
        '''
        tcid = {}
        for key, value in FileStorage.__objects.items():
            value = value.to_dict()
            tcid[key] = value

        with open(FileStorage.__file_path, "w") as f:
            json.dump(tcid, f, indent=2)

    def reload(self):
        '''
        Deserialize the JSON file to objects
        '''
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path) as f:
                    obj_dicts = json.load(f)
            except FileNotFoundError:
                pass
            if obj_dicts:
                for key, value in obj_dicts.items():
                    model = BaseModel(**(obj_dicts[key]))
                    FileStorage.__objects[key] = model
