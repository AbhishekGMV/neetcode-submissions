class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = []
        visited = [[False]*n for _ in range(m)]

        def addTreasure(r,c):
            if r < 0 or c < 0 or r >= m or c >= n or visited[r][c] or grid[r][c] == -1:
                return 
            visited[r][c] = True
            q.append((r,c))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited[i][j] = True
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.pop(0)
                grid[r][c] = dist
                addTreasure(r+1,c)
                addTreasure(r,c+1)
                addTreasure(r,c-1)
                addTreasure(r-1,c)
                
            dist += 1
