import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        queries=[(n,i) for i,n in enumerate(queries)]
        queries.sort()
        result=[0]*len(queries)
        R,C=len(grid),len(grid[0])
        min_heap=[(grid[0][0],0,0)]
        visited=set([(0,0)])
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        points=0
        for limit,idx in queries:
            while min_heap and min_heap[0][0]<limit:
                val,r,c=heapq.heappop(min_heap)
                points+=1
                for dr,dc in dirs:
                    nr,nc=r+dr,c+dc
                    if nr>=0 and nr<R and nc>=0 and nc<C and (nr,nc) not in visited:
                        heapq.heappush(min_heap,(grid[nr][nc],nr,nc))
                        visited.add((nr,nc))
            result[idx]=points
        return result
            

        