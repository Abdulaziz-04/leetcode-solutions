class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        while l<r:
            if abs(nums[l])==abs(nums[r]) and nums[r]>nums[l]:
                return nums[r]
            elif abs(nums[l])>abs(nums[r]):
                l+=1
            else:
                r-=1
        return -1
        