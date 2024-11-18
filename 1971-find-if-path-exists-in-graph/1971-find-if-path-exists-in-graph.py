class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList=defaultdict(list)
        for v1,v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        visited=set()
        def dfs(node):
            if node==destination:
                return True
            if node in visited:
                return False 
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(source)
        