class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        char_set=set()
        mx_len=0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            mx_len=max(mx_len,r-l+1)
        return mx_len
                
        