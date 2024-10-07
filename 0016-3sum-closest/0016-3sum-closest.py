class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float('inf')
        result=0
        for i,f in enumerate(nums):
            l,r=i+1,len(nums)-1
            while l<r:
                total=nums[l]+nums[r]+f
                if total==target:
                    return target
                elif total<target:
                    l+=1
                else:
                    r-=1
                if abs(total-target)<diff:
                    diff=abs(total-target)
                    result=total
        return result

        