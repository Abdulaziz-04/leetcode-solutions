class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set(['a','e','i','o','u','A','E','I','O','U'])
        target=[]
        for l in s:
            if l in vowels:
                target.append(l)
        i=len(target)-1
        result=''
        for l in s:
            if l in vowels:
                result+=target[i]
                i-=1
            else:
                result+=l
        return result
        

        