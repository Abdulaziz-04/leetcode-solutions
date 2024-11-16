class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=max(nums)
        cmax,cmin=1,1
        for n in nums:
            tmp=n*cmax
            cmax=max(n*cmax,n*cmin,n)
            cmin=min(tmp,n*cmin,n)
            result=max(result,cmax)
        return result
        