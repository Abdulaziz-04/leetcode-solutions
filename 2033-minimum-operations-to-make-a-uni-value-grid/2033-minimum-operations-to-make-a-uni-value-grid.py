class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        for row in grid:
            for n in row:
                if n%x!=grid[0][0]%x:
                    return -1
        grid=[n for row in grid for n in row]
        grid.sort()
        prefix=0
        total=sum(grid)
        result=float('inf')
        for i in range(len(grid)):
            left=grid[i]*i-prefix
            right=total-prefix-(grid[i]*(len(grid)-i))
            result=min(result,(left+right)//x)
            prefix+=grid[i]
        return result
            
        