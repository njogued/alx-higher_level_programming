#!/usr/bin/python3
'''
Using UUID
'''
import uuid

class User(BaseModel):
    pass

id = uuid.uuid4()
print(f"The unique ID is: {id}")
