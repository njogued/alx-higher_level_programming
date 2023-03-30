#!/usr/bin/python3
'''Find the peak'''

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    for current in range(len(list_of_integers) - 1):
        nxt = current + 1
        prev = current - 1
        if current == 0 and list_of_integers[current] > list_of_integers[nxt]:
            return list_of_integers[current]
        elif current != 0 and current != len(list_of_integers) - 1 and list_of_integers[current] > list_of_integers[nxt] and list_of_integers[current] > list_of_integers[prev]:
            return list_of_integers[current]
        elif current == len(list_of_integers) - 1 and list_of_integers[-1] > list_of_integers[-2]:
            return list_of_integers[-1]
        else:
            return list_of_integers[0]
