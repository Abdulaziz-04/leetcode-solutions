class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq=defaultdict(int)
        l=0
        good=0
        for r in range(len(s)):
            freq[s[r]]+=1
            if r-l+1>3:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            if r-l+1==3 and len(freq)==3:
                good+=1
        return good

                

        