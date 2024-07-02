class Solution(object):
    def numDistinct(self, s, t):
        cache = {}
        def dfs(i,j):
            if len(t) == j:
                return 1
            if len(s) == i:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                cache[(i,j)] = dfs(i+1,j)
            return cache[(i,j)]
        return dfs(0,0)
            
        
