class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i!=j:
                    result.append(words[i])
                    break
        return result
        