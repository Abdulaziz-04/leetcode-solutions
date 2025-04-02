class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left=nums[0]
        result=0
        for i in range(1,len(nums)):
            if nums[i]>left:
                left=nums[i]
            for j in range(i+1,len(nums)):
                result=max(result,(left-nums[i])*nums[j])
        return result

        