#!/usr/bin/python3
"""
Module with from_json_string function
"""
import json


def from_json_string(my_str):
    """python3 -c 'print(__import__(module).function.__doc__)'"""
    return json.loads(my_str)
