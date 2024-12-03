class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mxLen=0
        l=0
        zero_count=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero_count+=1
            while zero_count>k:
                if nums[l]==0:
                    zero_count-=1
                l+=1
            mxLen=max(mxLen,r-l+1)
            print(zero_count)
        return mxLen


        