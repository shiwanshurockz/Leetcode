class Solution(object):
    #Below fuction will return Nearest smaller element to the left
    def helperCode(self,arr,NSL,end,n):
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
    def maximalRectangle(self, arr):
        maxres = 0
        array = [0]*len(arr[0])
        for j in range(len(arr)):
            for i in range(len(arr[0])):
                if int(arr[j][i]) != 0:
                    array[i] += int(arr[j][i])
                else:
                    array[i] = 0
            NSL = []
            NSR = []
            n = len(arr[0])
            NSL = self.helperCode(array,NSL,-1,n)
            NSR = self.helperCode(array[::-1],NSR,n,n)[::-1]
            for i in range(n):
                if NSR[i] != n:
                    NSR[i] = n - NSR[i] - 1
            res = 0
            for i in range(n):
                res = max(res,(NSR[i] - NSL[i] - 1)*array[i])
            maxres = max(maxres,res)
        return maxres
            
