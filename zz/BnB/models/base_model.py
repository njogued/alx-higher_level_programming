#!/usr/bin/python3
'''
Base model for HBNB project
'''
from datetime import datetime
import json
from uuid import uuid4

class BaseModel():
    '''
    Methods: save, to_dict, __str__, __init__
    Attributes: id, created_at, updated_at
    '''
    def __init__(self, *args, **kwargs):
        '''
        id - Unique ID
        created_at - Time when object is instantiated
        updated_at - Defaults to created_at when an object is instantiated
        '''
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                '''
                if key == "created_at" or key == "updated_at":
                    datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                '''
                setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        '''
        strftime("%A %d %B %Y at %H:%M:%S")
        '''

    def __str__(self):
        '''
        return a string representation of the class
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Update the updated_at instance attribute
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        returns a dict of key/value pairs of the instance
        '''
        dict_rep = {}
        dict_rep["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        dict_rep.update(self.__dict__)
        return dict_rep
