class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        n=len(costs)
        head_workers=costs[:candidates]
        tail_workers=costs[max(candidates,n-candidates):]
        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)
        next_head=candidates
        next_tail=n-candidates-1
        total_cost=0
        while k:
            if not tail_workers or head_workers and head_workers[0]<=tail_workers[0]:
               total_cost+=heapq.heappop(head_workers)
               if next_head<=next_tail:
                    heapq.heappush(head_workers,costs[next_head])
                    next_head+=1
            else:
                total_cost+=heapq.heappop(tail_workers)
                if next_head<=next_tail:
                    heapq.heappush(tail_workers,costs[next_tail])
                    next_tail-=1
            k-=1
        return total_cost

        
        