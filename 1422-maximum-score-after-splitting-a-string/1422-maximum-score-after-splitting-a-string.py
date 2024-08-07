class Solution:
    def maxScore(self, s: str) -> int:
        r=s.count('1')
        l=0
        i=0
        mx_score=r-1
        while i<len(s)-1:
            if s[i]=='0':
                l+=1
            else:
                r-=1
            mx_score=max(mx_score,l+r)
            i+=1
        return mx_score
            
        