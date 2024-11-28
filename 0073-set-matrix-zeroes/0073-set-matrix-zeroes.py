class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        visited=set()
        def dfs(i,j):
            for k in range(c):
                if matrix[i][k]!=0 and (i,k) not in visited:
                    visited.add((i,k))
            for k in range(r):
                if matrix[k][j]!=0 and (k,j) not in visited:
                    visited.add((k,j))

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    dfs(i,j)
        for i in range(r):
            for j in range(c):
                if (i,j) in visited:
                    matrix[i][j]=0
        return matrix
        
        