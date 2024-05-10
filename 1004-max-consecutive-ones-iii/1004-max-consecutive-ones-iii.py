class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Use variable length sliding window here,
        keep track of current window length and if it violates the <=k zeros 
        we increment the left pointer else the right pointer
        """
        # Define initial variables
        l=0
        l_consec=0
        zero_count=0

        for r in range(len(nums)):
            # keep track of zero count and maintain valid window
            if nums[r]==0:
                zero_count+=1
            # If invalid window, make it valid again
            while zero_count>k:
                if nums[l]==0:
                    zero_count-=1
                l+=1    
            # Check the window length
            l_consec=max(l_consec,r-l+1)
        return l_consec
                

       
        