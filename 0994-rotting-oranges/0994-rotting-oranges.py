class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q=deque()
        visited=set()
        fresh=0
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
                    visited.add((i,j))
        
        time=0
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                cx,cy=q.popleft()
                for dx,dy in directions:
                    nx,ny=cx+dx,cy+dy
                    if nx>=0 and nx<r and ny>=0 and ny<c and grid[nx][ny]==1 and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))
                        fresh-=1
            time+=1
        return time if fresh<=0 else -1


        
        