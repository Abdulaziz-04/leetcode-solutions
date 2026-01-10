class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)-1
        jumps=0
        reach=n
        """
        reach=1
        0+1>=1
        reach=0
        """
        while reach>0:
            for i in range(reach):
                if nums[i]+i>=reach:
                    reach=i
                    break
            jumps+=1        
        return jumps



       