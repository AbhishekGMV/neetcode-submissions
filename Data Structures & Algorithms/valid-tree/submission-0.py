class Solution:
    def dfs(self, node, prev, graph, visited):
        if node in visited:
            return False

        visited.add(node)
        for neigh in graph[node]:
            if neigh == prev:
                continue
            if (not self.dfs(neigh, node, graph, visited)):
                return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        source = 0
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        prev = None
        return self.dfs(source, prev, graph, visited) and len(visited) == n