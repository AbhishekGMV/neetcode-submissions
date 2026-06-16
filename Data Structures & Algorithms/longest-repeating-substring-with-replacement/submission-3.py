class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        maxf = 0
        freq = defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] += 1

            maxf = max(maxf, freq[s[r]])
            
            while ((r-l+1) - maxf) > k:
                freq[s[l]] -= 1
                l += 1
            # window is valid by the end of while loop, can update longest outside loop 
            longest = max(longest, r-l+1)
        return longest 