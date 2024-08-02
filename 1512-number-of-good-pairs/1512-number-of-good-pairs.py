from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        n^2 complexity
        gp=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    gp+=1
        return gp
        """
        """
        Hashmap approach
        count=Counter(nums)
        result=0
        for v in count.values():
            result+=(v*(v-1))//2
        return result
        """
        count={}
        result=0
        for n in nums:
            if n in count:
                result+=count[n]
                count[n]+=1
            else:
                count[n]=1
        return result
        