class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        leaves = []
        edgeMap = {}
        for src, edg in adj.items():
            if len(edg) == 1:
                leaves.append(src)
            edgeMap[src] = len(edg)
        
        while leaves:
            if n <= 2:
                return leaves
            for i in range(len(leaves)):
                temp = leaves.pop(0)
                n -= 1
                for nei in adj[temp]:
                    edgeMap[nei] -= 1
                    if edgeMap[nei] == 1:
                        leaves.append(nei)
