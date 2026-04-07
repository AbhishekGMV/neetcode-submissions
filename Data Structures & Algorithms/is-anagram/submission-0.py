class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sf = {}
        tf = {}

        if len(s) != len(t):
            return False

        for c in s:
            sf[c] = sf.get(c, 0) + 1
        
        for c in t:
            tf[c] = tf.get(c, 0) + 1

        
        for c, f in tf.items():
            if c not in sf or sf[c] != f:
                return False
        return True
        