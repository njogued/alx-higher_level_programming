#!/usr/bin/python3
'''A script that sends a request to a URL and displays response'''
from urllib import request, error
from sys import argv as v

if __name__ == "__main__":
    try:
        with request.urlopen(v[1]) as response:
            print(response.body)
    except error.HTTPError as e:
        print(e)
