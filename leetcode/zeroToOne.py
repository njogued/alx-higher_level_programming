#!/usr/bin/python3

"""
This function takes a list with 1s at beginning
and 0s at the end. Takes in list and number of
zeros (zs)
Option 1: If zeros in list exceed zs, remove zs
zeros from the end and insert a 1 at the beginning
Option 2: If zeros are less than zs, replace last
digit one in list with a zero
Option 3: Terminate if only one zero is left in list

Return the number of passes through list to reach
option 3.

Note: Uses recursion. 
To return output: uses return keyword ie. return zeroToOne

Note: uses numlist.insertion(index, digit) to insert.
Slicing does not work for inserting non-iterables
"""


def zeroToOne(numlist, zs, count=0):
    ones = 0
    zeros = 0
    for nums in numlist:
        if nums > 0:
            ones += 1
        if nums == 0:
            zeros += 1
    if zeros >= zs:
        for popper in range(zs):
            numlist.pop()
        numlist.insert(0, 1)
        count += 1
        return zeroToOne(numlist, zs, count)
    if zeros < zs and len(numlist) != 1:
        for lastone in range(len(numlist)):
            if lastone + 1 < len(numlist) and \
                    numlist[lastone] == 1 and numlist[lastone + 1] == 0:
                numlist[lastone] = 0
            elif numlist[lastone] == 1 and lastone == len(numlist) - 1:
                numlist[lastone] = 0
        count += 1
        return zeroToOne(numlist, zs, count)
    if zeros < zs and len(numlist) == 1:
        if numlist[0] == 0:
            return count
        elif numlist[0] == 1:
            numlist[0] = 0
            return zeroToOne(numlist, zs, count)


def main():
    numlist = [1, 1, 1, 1, 0, 0]
    print("The list passed is {}".format(numlist))
    numlist = zeroToOne(numlist, 2)
    print("Output: {}".format(numlist))


main()
