class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # Add or remove element from window
        def updateWindow(bits,x,change):
            for i in range(32):
                if (x>>i) & 1:
                    bits[i]+=change
        
        def getNum(bits):
            result=0
            for i in range(32):
                if bits[i]:
                    result|=1 << i
            return result
        
        n=len(nums)
        result=n+1
        bits=[0]*32
        l=0
        for r in range(n):
            # Insert
            updateWindow(bits,nums[r],1)
            while l<=r and getNum(bits)>=k:
                result=min(result,r-l+1)
                updateWindow(bits,nums[l],-1)
                l+=1
        return result if result!=n+1 else -1
        