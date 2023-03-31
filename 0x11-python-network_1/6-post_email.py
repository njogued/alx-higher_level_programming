#!/usr/bin/python3
'''Use requests to send POST request'''
from requests import get, post
from sys import argv

if __name__ == "__main__":
    response = post(argv[1], {'email': argv[2]})
    print(response.text)
