class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r,n=0,len(nums)-1,len(nums)-1
        result=[0]*len(nums)
        while n>=0:
            if(abs(nums[l])>=abs(nums[r])):
                result[n]=nums[l]**2
                l+=1
            else:
                result[n]=nums[r]**2 
                r-=1
            n-=1    
        return result 