class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C=len(board),len(board[0])
        path=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            no_bounds=r<0 or r>=R or c<0 or c>=C
            path_check=(r,c) in path
            if no_bounds or word[i]!=board[r][c] or path_check: 
                return False
            path.add((r,c))
            result=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return result
        for r in range(R):
            for c in range(C):
                if dfs(r,c,0):
                    return True
        return False

        