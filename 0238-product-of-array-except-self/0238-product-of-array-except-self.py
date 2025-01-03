class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=1
        result=[]
        for n in nums:
            result.append(pre)
            pre*=n
        post=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=post
            post*=nums[i]
        return result

        