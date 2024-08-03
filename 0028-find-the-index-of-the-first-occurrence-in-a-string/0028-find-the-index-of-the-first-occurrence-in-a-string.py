class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        KMP approach : 
        haystack : AAAXAAAX
        needle = AAAA
        """
        # First let's create the LPS array
        n=len(haystack)
        m=len(needle)
        lps=[0]*m
        # Initialize
        prev_lps,i=0,1
        while i < m:
            if needle[i]==needle[prev_lps]:
                lps[i]=prev_lps+1
                prev_lps+=1
                i+=1
            elif prev_lps==0:
                lps[i]=0
                i+=1
            else:
                prev_lps=lps[prev_lps-1]
        # Iteration stage
        i,j=0,0
        while i<n:
            if needle[j]==haystack[i]:
                i+=1
                j+=1
            elif j==0:
                i+=1
            else:
                j=lps[j-1]
            if j==m:
                return i-m
        return -1




        