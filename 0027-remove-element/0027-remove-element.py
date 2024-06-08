class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Basically, we create a custom index which tracks the non-val eleemnts
        # If we find an element which is not equal to val then we can add it to the 
        # Custom index and increment k
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k

        

        