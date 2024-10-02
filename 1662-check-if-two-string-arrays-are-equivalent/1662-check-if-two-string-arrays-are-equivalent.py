class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Index
        w1,w2=0,0
        # Char pointer
        l=r=0
        while w1<len(word1) and w2<len(word2):
            if word1[w1][l]!=word2[w2][r]:
                return False
            l+=1
            r+=1
            if l==len(word1[w1]):
                w1+=1
                l=0
            if r==len(word2[w2]):
                w2+=1
                r=0
        if w1!=len(word1) or w2!=len(word2):
            return False
        return True

        