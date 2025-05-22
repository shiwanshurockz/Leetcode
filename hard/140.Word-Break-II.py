class Solution(object):
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        cache = {}
        def backtrack(i):
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]
            res = []
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w not in wordDict:
                    continue
                strings = backtrack(j+1)
                if not strings:
                    continue
                for substr in strings:
                    sentence = w
                    if substr:
                        sentence += " " +substr
                    res.append(sentence)
            cache[i] = res
            return res
        return backtrack(0)
