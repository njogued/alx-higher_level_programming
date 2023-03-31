#!/usr/bin/python3
'''Print the header in the output'''
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get(argv[1])
    print(response.headers['X-Request-Id'])
