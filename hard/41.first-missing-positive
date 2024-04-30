class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lenarr = len(nums)
        for i in range(lenarr):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(lenarr):
            index = abs(nums[i])-1
            if index >= 0 and index < lenarr:
                if nums[index] > 0:
                    nums[index] = (-1)*nums[index]
                elif nums[index] == 0:
                    nums[index] = -1 * (lenarr+1)

        for i in range(1,lenarr+1):
            if nums[i-1] >= 0:
                return i
        return (lenarr+1)
        
