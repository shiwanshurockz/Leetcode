class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            res = ""
            jumps = (numRows-1)*2
            for i in range(numRows):
                curr = i
                while curr < len(s):
                    res = res + str(s[curr])
                    if i > 0 and i < numRows-1 and curr + jumps - (2*i) < len(s):
                        res = res + str(s[curr + jumps - (2*i)])
                    curr += jumps
        return res
