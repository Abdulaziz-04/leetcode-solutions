class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for n in nums:
            count[n]+=1
        i=0
        for j in range(len(count)):
            while count[j]:
                nums[i]=j
                i+=1
                count[j]-=1
        return nums
            
        