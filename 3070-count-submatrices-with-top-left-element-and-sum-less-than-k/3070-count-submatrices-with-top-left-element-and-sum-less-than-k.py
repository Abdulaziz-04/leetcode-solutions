class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n,m=len(grid),len(grid[0])
        cols=[0]*m
        total=0
        for i in range(len(grid)):
            row_sum=0
            for j in range(len(grid[0])):
                cols[j]+=grid[i][j]
                row_sum+=cols[j]
                if row_sum<=k:
                    total+=1
        return total

        