from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        time=0
        fresh=0
        q=deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        if fresh==0:
            return 0
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if nr>=0 and nr<R and nc>=0 and nc<C and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            time+=1
        if fresh==0:
            return time
        return -1
        
                


        
        