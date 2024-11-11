class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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


        