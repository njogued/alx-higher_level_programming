#!/usr/bin/python3
"""
Module with load from json file
"""
import json


def load_from_json_file(filename):
    """python3 -c 'print(__import__(Module).method.__doc__)'"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
