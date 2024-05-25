class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        concat_val=0
        while l<r:
            concat_val+=int(str(nums[l])+str(nums[r]))
            l+=1
            r-=1
        if len(nums)%2==1:
            concat_val+=nums[len(nums)//2]
        return concat_val

            
        