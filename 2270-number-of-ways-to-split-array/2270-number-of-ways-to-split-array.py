class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        prefix=[]
        postfix=[]
        pre=0
        post=sum(nums)
        splits=0
        for i in range(len(nums)):
            pre+=nums[i]
            post-=nums[i]
            prefix.append(pre)
            postfix.append(post)
        for i in range(len(prefix)-1):
            if prefix[i]>=postfix[i]:
                splits+=1
        return splits

        