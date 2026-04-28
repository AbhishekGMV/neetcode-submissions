class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                curr *= nums[j]
            res[i] = curr
        return res