class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curSum=0
        even,odd=0,0
        result=0
        for num in arr:
            curSum+=num
            if curSum%2==0:
                result+=odd
                even+=1
            else:
                result+=even+1
                odd+=1
        return result % (10**9 + 7)
        