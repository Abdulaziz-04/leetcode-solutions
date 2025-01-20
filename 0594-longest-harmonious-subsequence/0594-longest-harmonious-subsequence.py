from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)
        n=set(nums)
        mx_val=0
        for k in n:
            if k+1 in n:
                mx_val=max(mx_val,c[k]+c[k+1])
        return mx_val
        