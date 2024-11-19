from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize==1:
            return False
        handFreq=Counter(hand)
        minHeap=list(handFreq.keys())
        heapq.heapify(minHeap)
        while minHeap:
            n=minHeap[0]
            for h in range(n,n+groupSize):
                if h not in minHeap:
                    return False
                handFreq[h]-=1
                if handFreq[h]==0:
                    if h!=minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
        