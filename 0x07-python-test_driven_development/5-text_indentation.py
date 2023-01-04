#!/usr/bin/python3
'''
text indentation function
'''

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in range(len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print(text[i], end="")
                print("\n")
            else:
                print(text[i], end="")
