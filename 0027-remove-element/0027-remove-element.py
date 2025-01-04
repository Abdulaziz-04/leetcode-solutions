class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]==val and nums[r]==val:
                r-=1
            elif nums[l]==val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            else:
                l+=1
        return l
        