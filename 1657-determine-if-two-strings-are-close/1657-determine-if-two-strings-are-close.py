class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False
        if set(word1)!=set(word2):
            return False
        f1=defaultdict(int)
        f2=defaultdict(int)
        for w in word1:
            f1[w]+=1
        for w in word2:
            f2[w]+=1
        return sorted(f1.values())==sorted(f2.values())
        