class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l,r=0,len(nums)
        while l<r:
            m=l+(r-l)//2
            if nums[m]>=0:
                r=m
            else:
                l=m+1
        z1=l
        while l<len(nums) and nums[l]==0:
            l+=1
        if z1==l:
            return max(l,len(nums)-l)
        else:
            return max(z1,len(nums)-l)
        