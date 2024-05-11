class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1=sentence1.split()
        w2=sentence2.split()
        n1=len(w1)
        n2=len(w2)
        if n1>n2:
            n1,n2=n2,n1
            w1,w2=w2[:],w1[:]
        i=0
        while i<n1 and w1[i]==w2[i]:
            i+=1
        while i<n1 and w1[i]==w2[n2-n1+i]:
            i+=1
        return i==n1


            