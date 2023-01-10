#!/usr/bin/python3
import json
"""
Function that returns json representation of a string
"""


def to_json_string(my_obj):
    """ python3 -c 'print(__import__(filename).function.__doc__)' """
    return json.dumps(my_obj)
