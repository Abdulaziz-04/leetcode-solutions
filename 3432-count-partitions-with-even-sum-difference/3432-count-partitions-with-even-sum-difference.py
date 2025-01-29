class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=nums[0]
        right=sum(nums)-nums[0]
        # 2 4 6 8
        """
        left = 2
        right = 18
        loop : 1 to n:
        left-right
        left+=nums[i]
        right-=nums[i]
        """
        result=0
        for i in range(1,len(nums)):
            if abs(left-right)%2==0:
                result+=1
            left+=nums[i]
            right-=nums[i]
        return result

        