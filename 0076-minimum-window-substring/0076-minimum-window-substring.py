from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        t_count,window=defaultdict(int),defaultdict(int)
        for ch in t:
            t_count[ch]+=1
        have,need=0,len(t_count)
        l=0
        res,mx_len=[-1,-1],float('inf')
        for r in range(len(s)):
            ch=s[r]
            window[ch]+=1
            if ch in t_count and t_count[ch]==window[ch]:
                have+=1
            while have ==need:
                if r-l+1 < mx_len:
                    mx_len=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in t_count and t_count[s[l]]>window[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if mx_len!=float('inf') else ""
            


        