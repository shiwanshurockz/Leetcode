class Solution:
    def numTrees(self, n: int) -> int:
        # numTrees[4] = numTrees[0] * numTrees[3] +
        #               numTrees[1] * numTrees[2] +
        #               numTrees[2] * numTrees[1] +
        #               numTrees[3] * numTrees[0] +
        numOfTrees = [1] * (n+1)
        
        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root-1
                right = nodes-root
                total += numOfTrees[left] * numOfTrees[right]
            numOfTrees[nodes] = total
        return numOfTrees[n]
        
