#!/usr/bin/env python3
def uniq_add(my_list=[]):
  #result = 0
  #set_1 = set(my_list)
  '''for i in set(my_list):
    result += i
  return result '''
  print(set(my_list))
  return (sum(set(my_list)))

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))