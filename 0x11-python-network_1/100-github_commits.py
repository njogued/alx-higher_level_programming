#!/usr/bin/python3
'''Script that prints 10 commits on a repo'''
from sys import argv as v
import requests

if __name__ == "__main__":
    resp = requests.get(f"https://api.github.com/repos/{v[1]}/{v[2]}/commits")
    data = resp.json()
    counter = 0
    for entries in data:
        print(f"{entries['sha']}: {entries['commit']['author']['name']}")
        counter += 1
        if counter >= 10:
            break
