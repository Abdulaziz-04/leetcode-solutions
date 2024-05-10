class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Keep track of max sum, as division is by k for any case
        total=mx_sum=sum(nums[:k])
        for i in range(k,len(nums)):
            # Add the new element
            total+=nums[i]
            # Delete the old one
            total-=nums[i-k]
            # Get the max
            mx_sum=max(total,mx_sum)
        # Return average
        return mx_sum/k
            
        