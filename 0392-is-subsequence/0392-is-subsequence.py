class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        s_idx=0
        for t_idx in range(len(t)): 
            if t[t_idx]==s[s_idx]:
                s_idx+=1
            if s_idx == len(s):
                return True
        return False

        