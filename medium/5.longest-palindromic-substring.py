class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        #for ODD
        for i in range(len(s)):
            l = i
            r = i
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    if len(res) < r-l+1:
                        res = s[l:r+1]
                    l = l - 1
                    r = r + 1
                else:
                    break
        #for Even palindromes
        for i in range(len(s)-1):
            l = i
            r = i+1
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    if len(res) < r-l+1:
                        res = s[l:r+1]
                    l = l - 1
                    r = r + 1
                else:
                    break
        return res
