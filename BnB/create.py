#!/usr/bin/python3

import sys

text = sys.argv[1]
if '_' in text:
    new_text = text.replace('_', ' ')
print(new_text)
