class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxSell = float('-inf')

        for p in prices:
            minBuy = min(p, minBuy)
            maxSell = max(maxSell, p-minBuy)
        return maxSell