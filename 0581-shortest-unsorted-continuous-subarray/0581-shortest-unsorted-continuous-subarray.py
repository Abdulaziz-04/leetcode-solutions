class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_seen=-float('inf')
        l=0
        for i in range(n):
            if nums[i]<max_seen:
                l=i
            else:
                max_seen=max(nums[i],max_seen)
        r=-1
        min_seen=float('inf')
        for i in range(n-1,-1,-1):
            if nums[i]>min_seen:
                r=i
            min_seen=min(nums[i],min_seen)
        if r==-1:
            return 0
        return l-r+1
        