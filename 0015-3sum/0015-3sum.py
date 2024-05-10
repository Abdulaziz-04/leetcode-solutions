class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the numbers
        nums.sort()
        result=[]
        # pivot one point and two pointer the other two
        for i,f in enumerate(nums):
            # Already encountered number
            if i>0 and f==nums[i-1]:
                continue
            # 2 pointer basic approach
            l,r=i+1,len(nums)-1
            while l<r:
                total=f+nums[l]+nums[r]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    result.append([f,nums[l],nums[r]])
                    # Avoid repeating numbers for sorted array
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return result


        