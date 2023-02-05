#!/usr/bin/python3
'''
Base model
'''
class BaseModel():
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
    
    @property
    def name(self):
        return self.name

    @property
    def mail(self):
        return self.mail

    @name.setter
    def name(self, value):
        self.name = value

    @mail.setter
    def mail(self, value):
        self.mail = value
