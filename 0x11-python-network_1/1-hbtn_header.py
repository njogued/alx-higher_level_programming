#!/usr/bin/python3
'''Print the X-Request-Id variable in the response header'''
from urllib.request import urlopen
from sys import argv as v


if __name__ == "__main__":
    with urlopen(v[1]) as location:
        headers = location.headers
        print(headers["X-Request-Id"])
