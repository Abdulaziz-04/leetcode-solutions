class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        mx_consec=0
        for n in nums:
            if n-1 not in nums:
                consec=1
                t=n
                while t+1 in nums:
                    consec+=1
                    t+=1
                mx_consec=max(consec,mx_consec)
        return mx_consec
        