class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        s=s.lower()
        def isValid(ch):
            return ord('a')<=ord(ch)<=ord('z') or ord('0')<=ord(ch)<=ord('9')
        while l<r:
            while l<r and not isValid(s[l]):
                l+=1
            while r>l and not isValid(s[r]):
                r-=1
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True
        