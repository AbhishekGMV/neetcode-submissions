class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key, val in freq.items():
            bucket[val].append(key)
            
        res = []
        for i in range(len(bucket)-1, 0, -1):
            vals = bucket[i]
            for n in vals:
                if len(res) < k:
                    res.append(n)
        return res
