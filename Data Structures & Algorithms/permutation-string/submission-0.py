class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1f = {}
        for ch in s1:
            s1f[ch] = s1f.get(ch, 0) + 1
        
        l = 0 
        count = 0
        s2f = {}

        for r, ch in enumerate(s2):
            s2f[ch] = s2f.get(ch, 0) + 1
            while (r-l+1) == len(s1):
                if s1f == s2f:
                    return True
                s2f[s2[l]] -= 1
                if s2f[s2[l]] == 0:
                    del s2f[s2[l]]
                l += 1
                
        return False
