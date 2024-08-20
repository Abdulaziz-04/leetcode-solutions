class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=''
        w1,w2=len(word1),len(word2)
        for i in range(min(w1,w2)):
            result+=word1[i]
            result+=word2[i]
        if w1 > w2:
            result+=word1[i+1:]
        else:
            result+=word2[i+1:]
        return result
        