#!/usr/bin/python3
'''Send request email as parameter'''
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
from sys import argv as v

if __name__ == "__main__":
    url = v[1]
    mail = v[2]
    email = {"email" : mail}
    data = urlencode(email)
    req = Request(url, data)
    with urlopen(req) as response:
        body = response.read()
        print(body)
