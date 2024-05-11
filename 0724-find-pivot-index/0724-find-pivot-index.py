class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Maintain prefix and postfix sum excluding the index value 
        # Compare  them at different indices 
        # If no result is found, return -1
        prefix_arr=[0]*len(nums)
        postfix_arr=[0]*len(nums)
        total=0
        for i,n in enumerate(nums):
            prefix_arr[i]=total
            total+=n
        total=0
        for i in range(len(nums)-1,-1,-1):
            postfix_arr[i]=total
            total+=nums[i]
        for i in range(len(prefix_arr)):
            if prefix_arr[i]==postfix_arr[i]:
                return i
        return -1
        
        