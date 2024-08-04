from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        The characters need to be repeating to find such substring
        Keep track of repeating characters using a counter
        if the current character is such a character we keep track of such character
        """
        rep_set={}
        mx_val=-1
        for i,ch in enumerate(s):
            if ch in rep_set:
                mx_val=max(mx_val,i-rep_set[ch]-1)
            else:
                rep_set[ch]=i
        return mx_val
        