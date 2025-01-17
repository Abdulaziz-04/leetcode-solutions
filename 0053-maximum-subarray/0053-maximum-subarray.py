class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        mx_total=nums[0]
        for n in nums:
            if total<0:
                total=0
            total+=n
            mx_total=max(total,mx_total)
        return mx_total
        