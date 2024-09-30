class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        total=0
        def check_pair(p1,p2):
            n2=len(p2)
            n1=len(p1)
            if n2<n1:
                return False
            for i in range(len(p1)):
                if p2[i]!=p1[i]:
                    return False
            for i in range(len(p1)-1,-1,-1):
                if p2[n2-n1+i]!=p1[i]:
                    return False
            return True
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if check_pair(words[i],words[j]):
                    total+=1
        return total

        