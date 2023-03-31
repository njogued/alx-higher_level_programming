#!/usr/bin/python3
'''A script that sends a request to a URL and displays response'''
from urllib import request, error
from sys import argv as v

if __name__ == "__main__":
    try:
        with request.urlopen(v[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print(f'Error code: {e.status}')
