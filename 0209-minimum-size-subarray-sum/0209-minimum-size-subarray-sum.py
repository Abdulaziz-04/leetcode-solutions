class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        mn_len=float('inf')
        l=0
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                mn_len=min(mn_len,r-l+1)
                total-=nums[l]
                l+=1
        return 0 if mn_len==float('inf') else mn_len
        