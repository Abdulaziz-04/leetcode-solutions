class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k:
            return -1
        nums=set(nums)
        total=0
        for n in nums:
            if n>k:
                total+=1
        return total

        