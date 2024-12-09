class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        adjList=defaultdict(list)
        for i,keys in enumerate(rooms):
            adjList[i].extend(keys)
        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in adjList[node]:
                if n not in visited:
                    dfs(n)
        dfs(0)
        return len(visited)==len(rooms)
        