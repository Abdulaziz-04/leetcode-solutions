class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs=[(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs=sorted(pairs,key=lambda x : x[1],reverse=True)
        n1_sum=0
        heap=[]
        score=0
        for n1,n2 in pairs:
            n1_sum+=n1
            heapq.heappush(heap,n1)
            if len(heap)>k:
                p=heapq.heappop(heap)
                n1_sum-=p
            if len(heap)==k:
                score=max(score,n1_sum*n2)
        return score

                
        