class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum=[0]
        prefix=0
        for n in nums:
            prefix+=n
            prefix_sum.append(prefix)
        max_pos=max(prefix_sum)
        min_neg=min(prefix_sum)
        return max_pos+abs(min_neg)
            
        