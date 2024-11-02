class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        result=0
        count=[0]*26
        for r in range(len(s)):
            count[ord(s[r])-ord('A')]+=1
            curr_max=max(count)
            win_len=r-l+1
            if win_len-curr_max>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
            result=max(result,r-l+1)
        return result
        