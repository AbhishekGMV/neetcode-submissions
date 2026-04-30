class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = len(nums) - 1

            while j < k:
                pairs = (nums[i], nums[j], nums[k])
                curr = sum(pairs)
                if curr == 0:
                    res.append(pairs)
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    
                    while j < k and nums[k+1] == nums[k]:
                        k -= 1
                    continue
                elif curr < 0:
                    j += 1
                else:
                    k -= 1

        return res
