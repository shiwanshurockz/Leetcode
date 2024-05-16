class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hMap = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hMap:
                hMap.remove(s[l])
                l += 1
            hMap.add(s[r])
            res = max(res,r-l+1)
        return res
