class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        result=0
        for w in words:
            i=0
            while i<len(pref):
                if i>=len(w) or w[i]!=pref[i]:
                    break
                i+=1
            if i==len(pref):
                result+=1
        return result

                

        