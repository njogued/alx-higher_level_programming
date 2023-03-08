class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        
        if s is None or type(s) != str:
            return None
        """
        if len(s) == 1 or numRows >= len(s) or numRows <= 1:
            return s
        lst = []
        num = numRows - 1
        for i in range(num * 2, 0, -2):
            lst.append(i)
        j = 0
        i = 0
        match = {}
        while i < len(lst) and j < len(s):
            match[str(j)] = lst[i]
            i += 1
            j += 1
            if i == len(lst):
                i = 0
        zigzag = ""
        i = 0
        while i < numRows:
            zigzag += s[i]
            value = match[str(i)] + i
            while value < len(s):
                zigzag += s[value]
                value += match[str(value)]
            i += 1
        return zigzag
