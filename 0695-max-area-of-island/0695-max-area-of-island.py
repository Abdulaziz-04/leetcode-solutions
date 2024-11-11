class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        visited=set()
        maxArea=0
        def dfs(r,c):
            if r<0 or r>R-1 or c<0 or c>C-1 or (r,c) in visited or grid[r][c]==0:
                return 0
            visited.add((r,c))
            return 1+dfs(r,c-1)+dfs(r,c+1)+dfs(r-1,c)+dfs(r+1,c)

        for r in range(R):
            for c in range(C):
                if grid[r][c]==1 and (r,c) not in visited:
                    maxArea=max(maxArea,dfs(r,c))
        return maxArea
        