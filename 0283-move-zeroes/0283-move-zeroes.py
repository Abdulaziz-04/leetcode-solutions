class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Simple Idea
        """
        l=0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[l]=nums[r]
                l+=1
        for i in range(l,len(nums)):
            nums[i]=0
        return nums
        