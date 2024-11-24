class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base Case
        if t=="": return ""

        # Variables
        window,t_count=defaultdict(int),defaultdict(int)
        result,mxLen=[-1,-1],float('inf')
        l=0

        for ch in t:
            t_count[ch]+=1
        have,need=0,len(t_count)
        for r in range(len(s)):
            window[s[r]]+=1
            if s[r] in t_count and window[s[r]]==t_count[s[r]]:
                have+=1
            while have==need:
                if r-l+1<mxLen:
                    mxLen=r-l+1
                    result=[l,r]
                window[s[l]]-=1
                if s[l] in t_count and window[s[l]]<t_count[s[l]]:
                    have-=1
                l+=1
        l,r=result
        return s[l:r+1] if mxLen!=float('inf') else ""

        