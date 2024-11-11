class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return (x**2+y**2)**0.5
        q=[]
        result=[]
        n=0
        for p in points:
            x,y=p
            heapq.heappush(q,(distance(x,y),[x,y]))
        while n!=k:
            result.append(heapq.heappop(q)[1])
            n+=1
        return result
        