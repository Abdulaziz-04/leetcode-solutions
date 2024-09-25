class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum={0:1}
        result=0
        total=0
        for n in nums:
            total+=n
            if total-k in prefix_sum:
                result+=prefix_sum[total-k]
            prefix_sum[total]=1+prefix_sum.get(total,0)
        return result
        