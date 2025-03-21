class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=defaultdict(int)
        l=0
        result=0
        for r in range(len(s)):
            count[s[r]]+=1
            while len(count)==3:
                result+=len(s)-r
                count[s[l]]-=1
                if count[s[l]]==0:
                    count.pop(s[l])
                l+=1
        return result
        