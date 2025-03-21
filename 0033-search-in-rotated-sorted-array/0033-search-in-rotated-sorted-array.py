class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]>=nums[l]:
                if target>nums[m] or target<nums[l]:
                    l=m+1
                else:
                    r=m-1
            else:
                if target>nums[r] or target<nums[m]:
                    r=m-1
                else:
                    l=m+1
        return -1
        