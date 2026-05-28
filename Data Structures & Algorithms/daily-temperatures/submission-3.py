class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0]*N
        stack = []

        for i in range(N):
            t1 = temperatures[i]

            while stack and t1 > stack[-1][0]:
                t2, idx = stack.pop()
                res[idx] = i - idx
            stack.append((t1, i))

            
        return res