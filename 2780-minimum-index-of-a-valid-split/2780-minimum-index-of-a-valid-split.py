from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        left=defaultdict(int)
        right=Counter(nums)
        for i in range(len(nums)):
            left[nums[i]]+=1
            right[nums[i]]-=1
            if 2*left[nums[i]]>i+1 and 2*right[nums[i]]>n-i-1:
                return i
        return -1
        