class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result=0
        col_set={}
        for i in range(len(grid)):
            col=[]
            for j in range(len(grid)):
                col.append(grid[j][i])
            col=tuple(col)
            col_set[col]=col_set.get(col,0)+1
        for row in grid:
            if tuple(row) in col_set:
                result+=col_set[tuple(row)]
        return result


        