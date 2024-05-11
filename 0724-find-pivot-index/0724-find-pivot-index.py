class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Maintain prefix and postfix sum excluding the index value 
        # Compare  them at different indices 
        # If no result is found, return -1
        # O(1) space solution will be to update pre and post directly on go
        # O(n) is to keep arrays for pre and post calculation
        pre,post=0,sum(nums)
        for i,n in enumerate(nums):
            post-=n
            if pre==post:
                return i
            pre+=n
        return -1
        
        