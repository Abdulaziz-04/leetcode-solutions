class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        target=sum(nums)//2
        dp=set()
        dp.add(0)
        for n in nums[::-1]:
            nextDP=set()
            for m in dp:
                nextDP.add(m+n)
                nextDP.add(m)
            dp=nextDP
            if target in dp:   
                return True
        return False
        