from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for n in c.values():
            if n%2==1:
                return False
        return True
        