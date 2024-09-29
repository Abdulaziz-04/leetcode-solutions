class Solution:
    def maxProduct(self, s: str) -> int:
        N=len(s)
        pali_map={} # Bit_mask : length
        for mask in range(1,1<<N):
            subseq=""
            for i in range(N):
                if mask & (1<<i):
                    subseq+=s[i]
            if subseq==subseq[::-1]:
                pali_map[mask]=len(subseq)
        max_prod=0
        for m1 in pali_map:
            for m2 in pali_map:
                if m1&m2==0:
                    max_prod=max(max_prod,pali_map[m1]*pali_map[m2])
        return max_prod

        