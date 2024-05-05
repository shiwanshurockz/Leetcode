class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        def solve(ans, nums, n, k):
            if n == 1:                      #Insert the leftover digit in nums array
                ans.append(str(nums[0]))
                return
            index = k//fact[n-1]            #Difine no of blocks to skip (each block size fact[n-1])
            if k % fact[n-1] == 0:          #Converting 1 based to 0 for K at the end of the block
                index -= 1
            ans.append(str(nums[index]))    #Add new character
            nums.pop(index)                 #Erase the added char from nums
            k = k - (fact[n-1]*index)       #decrease K by the no of blocks*elements in blocks skipped
            solve(ans,nums,n-1,k)
        fact = []
        fact.append(1)
        f = 1
        for i in range(1,n):
            f = f*i
            fact.append(f)
        nums = [i for i in range(1, n+1)]
        solve(ans,nums,n,k)
        return str("".join(ans))
