import heapq
class MedianFinder:

    def __init__(self):
        # left side : maxHeap
        # right side : minHeap
        self.maxHeap,self.minHeap=[],[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num)
        # value criteria
        if self.minHeap and self.maxHeap and (-1*self.maxHeap[0])>self.minHeap[0]:
            val=-1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,val)
        # uneven size
        if len(self.minHeap)>len(self.maxHeap)+1:
            val=heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-val)
        if len(self.maxHeap)>len(self.minHeap)+1:
            val=-1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,val)

    def findMedian(self) -> float:
        if len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        if len(self.maxHeap)>len(self.minHeap):
            return -1*self.maxHeap[0]
        return (self.minHeap[0]+(-1*self.maxHeap[0]))/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()