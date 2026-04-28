class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1]*N
        
        for i in range(1, N):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = [1]*N

        for j in range(N-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        res = []

        for i in range(N):
            res.append(prefix[i] * suffix[i])
        return res
            
