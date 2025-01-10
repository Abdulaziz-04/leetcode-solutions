from collections import Counter
class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        freq2=defaultdict(int)
        freq1=defaultdict(int)
        for w2 in words2:
            curr_freq={}
            for ch in w2:
                curr_freq[ch]=1+curr_freq.get(ch,0)
                freq2[ch]=max(freq2[ch],curr_freq[ch])
            
        result=[]
        for w1 in words1:
            f1=Counter(w1)
            is_subset=True
            for ch,f in freq2.items():
                if f1[ch]<f:
                    is_subset=False
                    break
            if is_subset:
                result.append(w1)

        return result
            

        