class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,k-1
        mn_diff=float('inf')
        while r < len(nums):
            mn_diff=min(nums[r]-nums[l],mn_diff)
            l+=1
            r+=1
        return mn_diff

        