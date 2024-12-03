class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count=0
        l=0
        mxLen=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero_count+=1
            while zero_count>1:
                if nums[l]==0:
                    zero_count-=1
                l+=1
            mxLen=max(mxLen,r-l)
        return mxLen
        