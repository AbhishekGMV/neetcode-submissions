class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for key, val in freq.items():
            heapq.heappush(heap, [-val, key])

        res = []
        while k > 0:
            a = heapq.heappop(heap)[1]
            res.append(a)
            k -= 1
        return res


