from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Base condition
        if len(word1)!=len(word2):
            return False
        w1=Counter(word1)
        w2=Counter(word2)
        if set(w1.keys())!=set(w2.keys()):
            return False
        # transform : re-arranges frequencies basically
        # Comparing sorted versions of frequencies deals with that
        return sorted(w1.values())==sorted(w2.values())
        
        