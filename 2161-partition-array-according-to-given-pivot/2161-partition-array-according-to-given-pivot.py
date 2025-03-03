class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i,j=0,len(nums)-1
        i2,j2=0,len(nums)-1
        result=[0]*len(nums)
        while j>=0:
            if nums[i]<pivot:
                result[i2]=nums[i]
                i2+=1
            if nums[j]>pivot:
                result[j2]=nums[j]
                j2-=1
            i+=1
            j-=1
        for k in range(i2,j2+1):
            result[k]=pivot
        return result
        