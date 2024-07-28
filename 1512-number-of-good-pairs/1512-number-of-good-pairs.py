class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gp=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    gp+=1
        return gp
        