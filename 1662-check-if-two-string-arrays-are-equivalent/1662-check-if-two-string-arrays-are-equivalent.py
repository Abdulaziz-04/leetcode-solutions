class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1,w2="",""
        for w in word1:
            w1+=w
        for w in word2:
            w2+=w
        l,r=0,0
        if len(w1)!=len(w2):
            return False
        while l<len(w1) and r<len(w2):
            if w1[l]!=w2[r]:
                return False
            l+=1
            r+=1
        return True
        