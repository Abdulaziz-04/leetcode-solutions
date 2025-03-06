class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        result=[0,0]
        for i in range(n):
            for j in range(n):
                num=abs(grid[i][j])
                x=(num-1)//n
                y=(num+n-1)%n
                if grid[x][y]<0:
                    result[0]=num
                else:
                    grid[x][y]*=-1
        for i in range(n):
            for j in range(n):
                if grid[i][j]>0:
                    result[1]=i*n+j+1
                    break
        return result

        