class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       maxSeq, currSeq = 0, 0

       for x in nums:
        if x-1 not in nums:
            currSeq = 0
            while x in nums:
                currSeq += 1
                x += 1
            maxSeq = max(maxSeq, currSeq)
            
       return maxSeq 
    