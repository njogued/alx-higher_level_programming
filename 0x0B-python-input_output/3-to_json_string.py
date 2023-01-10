#!/usr/bin/python3
"""
Function that returns json representation of a string
"""
import json


def to_json_string(my_obj):
    """ python3 -c 'print(__import__(filename).function.__doc__)' """
    return json.dumps(my_obj)
