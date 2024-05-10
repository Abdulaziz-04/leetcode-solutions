class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=set()
        for i,f in enumerate(nums):
            for j in range(i+1,len(nums)):
                l,r=j+1,len(nums)-1
                while l<r:
                    total=f+nums[j]+nums[l]+nums[r]
                    if total<target:
                        l+=1
                    elif total>target:
                        r-=1
                    else:
                        result.add(tuple([f,nums[j],nums[l],nums[r]]))
                        l+=1
                        r-=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1
                        while nums[r]==nums[r+1] and l<r:
                            r-=1
        return list(result)
        