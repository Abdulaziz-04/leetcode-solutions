from collections import Counter
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq=Counter(s)
        result=0
        for f in freq.values():
            if f%2==0:
                result+=2
            else:
                result+=1
        return result

        