class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        l,r=0,0
        mode=0 if s[0]==' ' else 1

        while(r<len(s)):
            if mode==1 and s[r]==' ':
                words.append(s[l:r])
                l=r
                mode=0
            elif mode==0 and s[r]!=' ':
                l=r
                mode=1
            r+=1
        
        if (s[l:r].isalnum()):
            words.append(s[l:r])
        
        return ' '.join(words[::-1])
        