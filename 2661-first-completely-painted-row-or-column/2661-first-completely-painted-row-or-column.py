class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        R,C=len(mat),len(mat[0])
        lookup_set={}
        row_set={i : 0 for i in range(R)}
        col_set={i : 0 for i in range(C)}
        for i in range(R):
            for j in range(C):
                lookup_set[mat[i][j]]=(i,j)
        for i,n in enumerate(arr):
            r,c=lookup_set[n]
            row_set[r]+=1
            col_set[c]+=1
            if row_set[r]==C or col_set[c]==R:
                return i


        