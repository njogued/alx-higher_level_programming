#!/usr/bin/env python3
def search_replace(my_list, search, replace):
  #new_new_list = []
  #for item in my_list:
   # if item == search:
    #  new_new_list.append(replace)
    #elif item != search:
     # new_new_list.append(item)
  #return(new_new_list)
  return [replace if item == search else item for item in my_list]

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)