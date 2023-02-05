#!/usr/bin/python3
'''
Base model
'''
class BaseModel():
    def __init__(self, name, mail):
        self._name = name
        self._mail = mail
    
    @property
    def name(self):
        return self._name

    @property
    def mail(self):
        return self._mail

    @name.setter
    def name(self, value):
        self._name = value

    @mail.setter
    def mail(self, value):
        self._mail = value
