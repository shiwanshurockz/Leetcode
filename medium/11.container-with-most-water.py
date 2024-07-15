class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        while l < len(height) and r >=0 and l < r :
            water = min(height[l],height[r]) * abs(l-r)
            res = max(res,water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
