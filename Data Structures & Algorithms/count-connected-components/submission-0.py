class Solution:
    def dfs(self, node, graph, visited):
        if not graph[node] or visited[node]:
            return 
        visited[node] = True
        for neigh in graph[node]:
            if not visited[neigh]:
                self.dfs(neigh, graph, visited)
        

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False]*n
        count = 0
        for node in range(n):
            if not visited[node]:
                count += 1
                self.dfs(node, graph, visited)

        return count