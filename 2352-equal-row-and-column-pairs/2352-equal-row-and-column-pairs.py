from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result=0
        row_set=defaultdict(int)
        for i in range(len(grid)):
            row_set[tuple(grid[i])]+=1
        for i in range(len(grid)):
            col=[]
            for j in range(len(grid[0])):
                col.append(grid[j][i])
            if tuple(col) in row_set:
                result+=row_set[tuple(col)]
        return result

        