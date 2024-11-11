from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r,c=q.popleft()
                directions=[[0,1],[1,0],[0,-1],[-1,0]]
                for dr,dc in directions:
                    tr,tc=r+dr,c+dc
                    if (tr>=0 and tr<R) and (tc>=0 and tc<C) and grid[tr][tc]=="1" and (tr,tc) not in visited:
                        q.append((tr,tc))
                        visited.add((tr,tc))
        if not grid:
            return 0
        R,C=len(grid),len(grid[0])
        visited=set()
        islands=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands
        """
        # DFS
        if not grid:
            return 0
        R,C=len(grid),len(grid[0])
        visited=set()
        islands=0
        def dfs(r,c):
            if r<0 or r>R-1 or c<0 or c>C-1 or grid[r][c]=="0" or (r,c) in visited:
                return 
            visited.add((r,c))
            dfs(r+1,c) 
            dfs(r,c-1) 
            dfs(r-1,c) 
            dfs(r,c+1)
        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1
                    dfs(r,c)
        return islands
        """


        