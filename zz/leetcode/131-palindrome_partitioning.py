#!/usr/bin/python3

class Solution(object):
    def partition(self, s):
        parts = {}
        count = 0
        for char in range(len(s)):
            #char2 = char + 1
            for char2 in range(len(s) + 1):
                part = s[char:char2]
                if part != "":
                    count = char2 - char
                    parts[count] = part
                    print(part)
        print(parts)
        s1 = s[::-1]
        for key, value in parts.items():
            if value in s1:
                print(value)


if __name__ == "__main__":
    strn = Solution()
    strn.partition("kaomo")
