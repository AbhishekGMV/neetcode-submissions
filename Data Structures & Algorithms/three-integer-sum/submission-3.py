class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1

            while j < k:
                pairs = (nums[i], nums[j], nums[k])
                curr = sum(pairs)
                if curr == 0:
                    res.add(pairs)
                    j += 1
                    k -= 1
                    continue
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return list(res)
