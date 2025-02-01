class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=sum(nums)
        valid = 0

        for i in range(len(nums)):
            right-=nums[i] 
            print(left,right)
            if nums[i]==0 and left==right:
                valid+=2
            elif nums[i]==0 and abs(right-left)==1:
                valid+=1
            left+=nums[i]
        return valid


        