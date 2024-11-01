class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Keep this example in mind : [4,5,6,0,1,2]
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            # left sorted portion
            elif nums[m]>=nums[l]:
                # Can find smaller number on either side problem
                if target<nums[l] or target >nums[m]: 
                    l=m+1
                else:
                    r=m-1
            # right sorted portion
            else:
                # Can find greater number on either side problem
                if target<nums[m] or target>nums[r]:
                    r=m-1
                else:
                    l=m+1
        return -1


        