class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ps_map={}
        sp_map={}
        words=s.split()
        if len(words)!=len(pattern):
            return False
        for p,s in zip(pattern,words):
            if p in ps_map and ps_map[p]!=s:
                return False
            if s in sp_map and sp_map[s]!=p:
                return False
            ps_map[p]=s
            sp_map[s]=p
        return True


        