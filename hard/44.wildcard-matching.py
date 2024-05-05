class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        DP = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        DP[0][0] = True

        #Below case for s="aa",p="*"
        for j in range(1,len(p)+1):
            if (DP[0][j-1] == True and p[j-1] == '*'):
                DP[0][j] = True
            else:
                DP[0][j] = False
        for i in range(1,len(s)+1):
            for j in range(1, len(p)+1):
                if (s[i-1] == p[j-1]) or (p[j-1] == "?"):
                    DP[i][j] = DP[i-1][j-1]
                elif p[j-1] == "*":
                    DP[i][j] = DP[i-1][j] or DP[i][j-1]
                else:
                    DP[i][j] = False
        return DP[len(s)][len(p)]
