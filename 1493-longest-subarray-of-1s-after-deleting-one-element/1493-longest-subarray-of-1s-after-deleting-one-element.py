class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Same approach as to find the longest consective ones
        # Define variables
        l=0
        zero_count=0
        l_seq=0
        for r in range(len(nums)):
            # If we find a zero we keep track of it
            if nums[r]==0:
                zero_count+=1
            # Base condition violated
            while zero_count>1:
                # Shift to a valid window
                if nums[l]==0:
                    zero_count-=1
                l+=1
            # Re-calculate size of window
            l_seq=max(l_seq,r-l)
        return l_seq
                
        