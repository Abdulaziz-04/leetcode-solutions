class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Total length of the array
        N=len(code)
        # Final result
        result=[0]*N
        # Loop through N+k, as we update either l-1 or r+1 pointer
        l=0
        curr_sum=0
        for r in range(N+abs(k)):
            # Add to sum with circulation
            curr_sum+=code[r%N]
            # If we exceed window limit
            # Remove left value, add mod to avoid out of bounds
            if r-l+1>abs(k):
                curr_sum-=code[l%N]
                l=(l+1)%N

            # If we reach window limit
            if r-l+1==abs(k):
                # If <0 then replace l-1 with sum
                if k<0:
                    result[(r+1)%N]=curr_sum
                # if >0 then replace r+1 with sum
                elif k>0:
                    result[(l-1)%N]=curr_sum
            # If k==0, default initialization will handle the output
        return result

        