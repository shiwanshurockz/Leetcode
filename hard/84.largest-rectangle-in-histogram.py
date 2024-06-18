class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        def helperCode(arr,NSL,end):
            stack = []
            for i in range(n):
                if len(stack) == 0:
                    NSL.append(end)
                elif arr[i] > stack[-1][0]:
                    NSL.append(stack[-1][1])
                else:
                    while len(stack) > 0:
                        if arr[i] > stack[-1][0]:
                            break
                        stack.pop(-1),"Popped",end
                    if len(stack) == 0:
                        NSL.append(end)
                    else:
                        NSL.append(stack[-1][1])
                stack.append([arr[i],i])
            return NSL
        NSL = []
        NSR = []
        NSL = helperCode(heights,NSL,-1)
        NSR = helperCode(heights[::-1],NSR,n)[::-1]
        for i in range(n):
            if NSR[i] != n:
                NSR[i] = n - NSR[i] - 1
        res = 0
        for i in range(n):
            res = max(res,(NSR[i] - NSL[i] - 1)*heights[i])
        return res
