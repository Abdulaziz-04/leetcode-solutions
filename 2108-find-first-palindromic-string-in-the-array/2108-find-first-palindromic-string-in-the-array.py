class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def pal_check(word):
            l,r=0,len(word)-1
            while l<r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        for word in words:
            if pal_check(word):
                return word
        return ""
        