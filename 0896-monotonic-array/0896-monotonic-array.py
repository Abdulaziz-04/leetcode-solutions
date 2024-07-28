class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i=0
        while i<len(nums)-1 and nums[i]<=nums[i+1]:
            i+=1
        decreasing=i==len(nums)-1
        i=0
        while i<len(nums)-1 and nums[i]>=nums[i+1]:
            i+=1
        increasing=i==len(nums)-1
        return decreasing or increasing

        