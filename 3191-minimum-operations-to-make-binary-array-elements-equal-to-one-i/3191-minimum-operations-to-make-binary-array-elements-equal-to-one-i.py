class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                for j in range(i,i+3):
                    nums[j]=int(not nums[j])
                result+=1
        if not nums[-1] or not nums[-2]:
            return -1
        return result
        