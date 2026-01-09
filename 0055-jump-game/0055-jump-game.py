class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        reach=n-1
        start=0
        found=True
        while reach>0 and found:
            found=False
            for i in range(reach-1,-1,-1):
                if nums[i]+i>=reach:
                    found=True
                    reach=i
                    break
        return reach==0
