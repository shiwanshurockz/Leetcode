class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1): #Get even length of palindromes
            L=i
            R=i+1
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    res += 1
                    L -= 1
                    R += 1
                else:
                    break
        print(res)
        for i in range(len(s)): #Get odd length of palindromes
            L=i
            R=i
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    res += 1
                    L -= 1
                    R += 1
                else:
                    break
        return res
