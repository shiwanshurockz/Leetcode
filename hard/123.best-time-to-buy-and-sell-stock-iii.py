class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        left = [0]*n
        right = [0]*n
        Lmin = prices[0]
        #Filling left array, for 1st transaction
        for i in range(1,n):
            left[i] = max(left[i-1], prices[i] - Lmin)
            Lmin = min(Lmin,prices[i])
        #Right array for second transaction against time
        Rmax = prices[n-1]
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1], Rmax - prices[i])
            Rmax = max(Rmax,prices[i])
        profit = right[0]
        for i in range(1,n):
            profit = max(profit, left[i-1]+right[i])
        return profit

        
