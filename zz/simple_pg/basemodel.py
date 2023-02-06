#!/usr/bin/python3
'''
Base model for HBNB project
'''
from datetime import datetime
from uuid import uuid4

class BaseModel():
    '''
    Methods: save, to_dict, __str__, __init__
    Attributes: id, created_at, updated_at
    '''
    def __init__(self):
        '''
        id - Unique ID
        created_at - Time when object is instantiated
        updated_at - Defaults to created_at when an object is instantiated
        '''
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
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Update the updated_at instance attribute
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        returns a dict of key/value pairs of the instance
        '''
        sd = self.__dict__
