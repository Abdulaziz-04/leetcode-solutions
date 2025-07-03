class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        longest=float('inf')
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                longest=min(longest,r-l+1)
                total-=nums[l]
                l+=1
        return longest if longest!=float('inf') else 0

