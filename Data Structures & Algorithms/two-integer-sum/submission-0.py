class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            n = nums[i]
            match = target - n
            if match in seen:
                return [seen[match], i]
            seen[n] = i
        return [-1, -1]