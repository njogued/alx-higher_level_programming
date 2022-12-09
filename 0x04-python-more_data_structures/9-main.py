#!/usr/bin/env python3
def multiply_by_2(a_dictionary):
  ''''new_dictionary = a_dictionary.copy()
  for key, value in new_dictionary.items():
    new_dictionary[key] = value * 2
  return new_dictionary'''

  return ({x: a_dictionary[x] * 2 for x in a_dictionary})

def print_sorted_dictionary(a_dictionary):
  for keys, values in sorted(a_dictionary.items()):
    print("{}: {}".format(keys,values))

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)