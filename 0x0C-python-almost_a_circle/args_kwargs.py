#!/usr/bin/python3

"""function for args and kwargs"""
import sys


def main():
    sum_args = 0
    for num in range(1, len(sys.argv)):
        sum_args += int(sys.argv[num])
    print(f"Sum: {sum_args}")

def kwarg(**kwargs):
    sums = 0;
    for num in kwargs.values():
        sums += num
    print(f"Kwarg sums: {sums}")
    print(kwargs)

def arg(*args):
    sums = 0
    for num in range(len(args)):
        sums += args[num]
    print("Args sum: {}".format(sums))
    print(args)

if __name__ == "__main__":
    main()
    kwarg(men=3, women=5)
    kwarg(men=4, women=1, children=8)
    arg(3, 5)
    arg(3, 5, 7)
