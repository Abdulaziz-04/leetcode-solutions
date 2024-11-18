class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mval,cval=nums[0],0
        for n in nums:
            if cval<0:
                cval=0
            cval+=n
            mval=max(mval,cval)
        return mval
        