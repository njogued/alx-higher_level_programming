#!/usr/bin/python3
'''Use requests to send POST request'''
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get(argv[1], params={'email': argv[2]})
    print(response.text)
