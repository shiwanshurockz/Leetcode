class Solution:

    def trap(self, height: List[int]) -> int:
        MXL = [0 for i in  range(len(height))] #Max Greater to Left
        MXR = [0 for i in  range(len(height))] #Max Greater to right
        MXL[0] = height[0]
        MXR[-1] = height[-1]
        for i in range(1,len(height)):
            MXL[i] = max(MXL[i-1],height[i])
        for i in range(len(height) -2, 0, -1):
            MXR[i] = max(MXR[i+1],height[i])
        water = 0
        for i in range(len(height)):
            temp = min(MXL[i],MXR[i]) - height[i]
            if temp > 0:
                water += temp
        return water
