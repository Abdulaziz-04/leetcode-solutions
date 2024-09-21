class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest_seq=0
        for n in nums:
            if n-1 not in num_set:
                l=0
                while n+l in num_set:
                    l+=1
                longest_seq=max(longest_seq,l)
        return longest_seq
        