'''
beginWord =
"hit"
endWord =
"cog"
wordList =
["hot","dot","dog","lot","log","cog"]
Stdout
defaultdict(<class 'list'>, {'*ot': ['hot', 'dot', 'lot'], 
'h*t': ['hot'], 
'ho*': ['hot'], 
'd*t': ['dot'], 
'do*': ['dot', 'dog'], 
'*og': ['dog', 'log', 'cog'], 
'd*g': ['dog'], 'l*t': ['lot'], 
'lo*': ['lot', 'log'], 
'l*g': ['log'], 
'c*g': ['cog'], 
'co*': ['cog']})
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = collections.defaultdict(list)
        #Creating adjacency list like above, using time complx O(n*m*m) where m is len(beginWord), n is len(wordList)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                temp = q.popleft()
                if temp == endWord:
                    return res
                for j in range(len(temp)):
                    pattern = temp[:j] + "*" + temp[j+1:]
                    for values in adj[pattern]:
                        if values not in visit:
                            visit.add(values)
                            q.append(values)
            res += 1
        return 0
        
