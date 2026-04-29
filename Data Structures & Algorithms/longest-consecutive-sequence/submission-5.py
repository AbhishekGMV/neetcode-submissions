class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLen = 0

        for n in nums:
            if (n - 1) not in nums:
                curr = 1
                while n+1 in nums:
                    curr += 1
                    n += 1
                maxLen = max(curr, maxLen)
        return maxLen
