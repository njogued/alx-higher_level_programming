#!/usr/bin/python3

def main():
    rolling = [2, 3, 4, 5, 6]
    print(rolling)
    empty = []
    add = 0
    for index in range(len(rolling)):
        if index == 0:
            add = rolling[index]
        else:
            add = rolling[index] + empty[-1]
        empty.append(add)
    print(empty)


main()
