class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0]*N

        for i in range(N):
            days = 0
            for j in range(i+1, N):
                days += 1
                if temperatures[j] > temperatures[i]:
                    res[i] = days
                    break
        return res
