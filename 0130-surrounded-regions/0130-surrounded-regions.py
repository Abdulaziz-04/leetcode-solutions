class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R,C=len(board),len(board[0])
        visited=set()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c):
            if r<0 or r>=R or c<0 or c>=C or (r,c) in visited or board[r][c]!='O':
                return
            visited.add((r,c))
            board[r][c]='T'
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                dfs(nr,nc)
        for r in range(R):
            for c in range(C):
                if board[r][c]=='O' and r==0 or r==R-1 or c==0 or c==C-1:
                    dfs(r,c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c]=='O':
                    board[r][c]='X'
        
        for r in range(R):
            for c in range(C):
                if board[r][c]=='T':
                    board[r][c]='O'
            
        