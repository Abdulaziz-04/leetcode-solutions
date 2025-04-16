class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq={}
        n=len(nums)
        l=0
        total=0
        good=0
        for r in range(n):
            if nums[r] in freq:
                good+=freq[nums[r]]
                freq[nums[r]]+=1
            else:
                freq[nums[r]]=1
            while good>=k:
                total+=n-r
                freq[nums[l]]-=1
                good-=freq[nums[l]]
                l+=1
        return total
            
       