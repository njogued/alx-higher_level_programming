#!/usr/bin/python3
'''
Using UUID
'''
import uuid
import json
BaseModel = __import__("basemodel").BaseModel

class User(BaseModel):
    def __init__(self, name, mail, uniq_name=None):
        self.uniq_name = uniq_name
        super().__init__(name, mail)
        self.user_id = str(uuid.uuid4())

    def to_json(self):
        users_info = {}
        info = {"name": self.name, "mail": self.mail, "account": self.uniq_name}
        users_info[self.user_id] = info
        with open("Users.json", "r") as f:
            existing = json.load(f.read())
            print(existing)
            print(type(existing))
        with open("Users.json", "a") as f:
            json.dump(users_info, f)

if __name__ == "__main__":
    u = User("Edward Njogu", "ed@gmail.com", "njogued")
    u.to_json()
    u1 = User("L Maua", "maua@gmail.com", "maua")
    u1.to_json()
