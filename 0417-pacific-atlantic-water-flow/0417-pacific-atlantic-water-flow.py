class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C=len(heights),len(heights[0])
        pac,atl=set(),set()
        def dfs(r,c,visited,prevHeight):
            if r<0 or c<0 or r>R-1 or c>C-1 or (r,c) in visited or heights[r][c]<prevHeight: 
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        for c in range(C):
            dfs(0,c,pac,heights[0][c])
            dfs(R-1,c,atl,heights[R-1][c])
        
        for r in range(R):
            dfs(r,0,pac,heights[r][0])
            dfs(r,C-1,atl,heights[r][C-1])

        result=[]
        for r in range(R):
            for c in range(C):
                if (r,c) in pac and (r,c) in atl:
                    result.append((r,c))
        return result

        