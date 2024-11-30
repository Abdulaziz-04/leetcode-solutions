class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set=set(['a','e','i','o','u'])
        s=list(s)
        l,r=0,len(s)-1
        while l<r:
            if s[l].lower() not in vowel_set:
                l+=1
            elif s[r].lower() not in vowel_set:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return ''.join(s)


        