class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robber(nums):
            rob1,rob2=0,0
            for n in nums:
                curr=max(n+rob1,rob2)
                rob1=rob2
                rob2=curr
            return max(rob1,rob2)
        return max(robber(nums[1:]),robber(nums[:-1]))
        
