#!/usr/bin/python3
"""
Save to json
"""
import json


def save_to_json_file(my_obj, filename):
    """python3 -c 'print(__import__(module).method.__doc__)'"""
    json_obj = json.dumps(my_obj)
    with open(filename, "w") as f1:
        f1.write(json_obj)
