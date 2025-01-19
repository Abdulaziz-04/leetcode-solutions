import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        R,C=len(heightMap),len(heightMap[0])
        heap=[]
        for i in range(R):
            for j in range(C):
                if i==0 or i==R-1 or j==0 or j==C-1:
                    heapq.heappush(heap,(heightMap[i][j],i,j))
                    heightMap[i][j]=-1

        result=0
        max_h=-1
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        while heap:
            curr_h,r,c=heapq.heappop(heap)
            max_h=max(max_h,curr_h)
            result+=max_h-curr_h
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=R or nc>=C or heightMap[nr][nc]==-1:
                    continue
                heapq.heappush(heap,(heightMap[nr][nc],nr,nc))
                heightMap[nr][nc]=-1
        return result
                

        