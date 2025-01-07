class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        freq=[0]*3
        for n in nums:
            freq[n]+=1
        i,k=0,0
        while i<len(nums):
            if freq[k]>0:
                nums[i]=k
                freq[k]-=1
                i+=1
            else:
                k+=1
        return nums
        