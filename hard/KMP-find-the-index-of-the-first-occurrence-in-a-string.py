class Solution(object):
    def strStr(self, s, pattern):
        if pattern == "":
            return 0
        lps = [0] * len(pattern)
        prevLPS, i = 0, 1
        while i < len(pattern):
            if pattern[i] == pattern[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS-1]

        i = 0
        j = 0
        while i < len(s):
            if s[i] == pattern[j]:
                i, j = i+1,j+1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == len(pattern):
                return i-len(pattern)
        return -1
        
