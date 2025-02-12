class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        result=-1
        digit_mapping=[0]*82
        def digitSum(n):
            total=0
            while n:
                total+=n%10
                n=n//10
            return total
        for n in nums:
            curr_sum=digitSum(n)
            if digit_mapping[curr_sum]>0:
                result=max(result,digit_mapping[curr_sum]+n)
            digit_mapping[curr_sum]=max(digit_mapping[curr_sum],n)
        return result
