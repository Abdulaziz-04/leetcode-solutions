class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i]=0
        return nums
        