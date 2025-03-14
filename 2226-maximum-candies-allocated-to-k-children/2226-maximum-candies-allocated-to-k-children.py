class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total=sum(candies)
        if total<k:
            return 0
        l,r=1,total//k
        result=0
        while l<=r:
            m=l+(r-l)//2
            curr=0
            for c in candies:
                if c>=m:
                    curr+=c//m
                if curr>=k:
                    break
            if curr<k:
                r=m-1
            else:
                result=m
                l=m+1
        return result
