#!/usr/bin/env python3
def number_keys(a_dictionary):
  i = 0
  for x in a_dictionary:
    #print(key, ":", end=" ")
    #print(value)
    i = i + 1
    print(x)
  print(i)
  return len(a_dictionary)

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))