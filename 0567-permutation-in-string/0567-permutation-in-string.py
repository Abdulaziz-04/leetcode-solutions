class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_count,s2_count=[0]*26,[0]*26
        matches=0
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1
            s2_count[ord(s2[i])-ord('a')]+=1
        for i in range(len(s1_count)):
            if s1_count[i]==s2_count[i]:
                matches+=1

        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            idx=ord(s2[r])-ord('a')
            s2_count[idx]+=1
            if s2_count[idx]==s1_count[idx]:
                matches+=1
            elif s1_count[idx]+1==s2_count[idx]:
                matches-=1
            idx=ord(s2[l])-ord('a')
            s2_count[idx]-=1
            if s2_count[idx]==s1_count[idx]:
                matches+=1
            elif s2_count[idx]==s1_count[idx]-1:
                matches-=1
            l+=1
        return matches==26


        