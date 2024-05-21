class Solution:
    def freqCal(self, src, dest):
        for key in src.keys():
            if dest[key] < src[key]:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        if len(t) < len(S):
            return ""
        res = float('inf')
        subs = ""
        src = {}
        dst = {}
        for i in range(len(t)):
            if t[i] not in src:
                src[t[i]] = 1
                dst[t[i]] = 0
            else:
                src[t[i]] += 1
        l,r = 0,0
        while r < len(s):
            if s[r] in dst.keys():
                dst[s[r]] += 1
            while self.freqCal(src, dst):
                if r-l+2 < res:
                    res = r-l+2
                    subs = s[l:r+1]
                if s[l] in dst.keys():
                    dst[s[l]] -= 1
                l += 1
            r += 1
        return subs
