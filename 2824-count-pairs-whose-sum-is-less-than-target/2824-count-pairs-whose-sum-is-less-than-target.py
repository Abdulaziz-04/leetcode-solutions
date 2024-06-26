class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        pairs=0
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]+nums[r]>=target:
                r-=1
            else:
                pairs+=(r-l)
                l+=1
        return pairs
        