class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq_map=defaultdict(int)
        for w in word1:
            freq_map[w]+=1
        for w in word2:
            freq_map[w]-=1
        return sum(freq_map.values())==0
        