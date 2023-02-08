#!/usr/bin/python3

import random

if __name__ == "__main__":
	ls = ["Ed", "Njogu"]
	length = len(ls) - 1
	names = dict(enumerate(ls))
	select = random.randint(0, length)
	print(f"Selected name is: {names[select]}")
