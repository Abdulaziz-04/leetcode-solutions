class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pDiag=set()
        nDiag=set()
        result=[]
        board=[["."]*n for i in range(n)]

        def dfs(r):
            if r>=n:
                copy=["".join(r) for r in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or r+c in pDiag or r-c in nDiag:
                    continue
                col.add(c)
                pDiag.add(r+c)
                nDiag.add(r-c)
                board[r][c]="Q"
                dfs(r+1)
                col.remove(c)
                pDiag.remove(r+c)
                nDiag.remove(r-c)
                board[r][c]="."
        dfs(0)
        return result


        