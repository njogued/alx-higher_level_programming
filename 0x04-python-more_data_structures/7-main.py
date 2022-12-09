#!/usr/bin/env python3
def update_dictionary(a_dictionary, key, value):
  a_dictionary[key] = value
  return a_dictionary

def print_sorted_dictionary(a_dictionary):
  for keys, values in sorted(a_dictionary.items()):
    print("{}: {}".format(keys,values))
    
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)