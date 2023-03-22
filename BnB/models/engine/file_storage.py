#!/usr/bin/python3
'''
Module contains the FileStorage class
'''
import json


class FileStorage:
    '''
    Class for json.dump and json.load
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return FileStorage.__objects
        cls_objs = {}
        for k, v in FileStorage.__objects.items():
            if cls.__name__ in k:
                cls_objs[k] = v
        return cls_objs

    def new(self, obj):
        '''Sets the obj in objects'''
        obj_name = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_name] = obj

    def save(self):
        '''Serialize the objects to JSON file (__file_path)'''
        tcid = {}
        for key, value in FileStorage.__objects.items():
            value = value.to_dict()
            tcid[key] = value

        with open(FileStorage.__file_path, "w") as f:
            json.dump(tcid, f, sort_keys=True, indent=2)

    def reload(self):
        '''Deserialize the JSON file to objects'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        all_models = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path) as f:
                    obj_dicts = json.load(f)
                    for key, value in obj_dicts.items():
                        mod_name = all_models[value["__class__"]]
                        model = mod_name(**(obj_dicts[key]))
                        FileStorage.__objects[key] = model
            except FileNotFoundError:
                pass

        

    def delete(self, obj=None):
        """Delete an object"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            del FileStorage.__objects[key]
            self.save()
        else:
            pass
