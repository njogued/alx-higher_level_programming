#!/usr/bin/python3
'''Find the peak'''


def find_peak(list_of_integers):
    '''Find the peak function'''
    if not list_of_integers:
        return None
    max_value = sorted(list_of_integers)
    return max_value[-1]
