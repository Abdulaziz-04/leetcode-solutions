class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            curr_num=abs(nums[i])
            target_idx=curr_num-1
            nums[target_idx]=-1*abs(nums[target_idx])
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        return result
        