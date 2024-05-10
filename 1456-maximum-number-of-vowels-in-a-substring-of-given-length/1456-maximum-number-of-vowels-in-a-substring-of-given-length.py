class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Define vowels
        vowels='aeiou'
        # Keep track of current vowel count in initial string
        curr_vc=0
        for l in s[:k]:
            if l in vowels:
                curr_vc+=1
        
        # Keep track of max vowel count
        mx_vc=curr_vc
        for i in range(k,len(s)):
            if s[i] in vowels:
                curr_vc+=1
            if s[i-k] in vowels:
                curr_vc-=1
            mx_vc=max(curr_vc,mx_vc)
            # Max possible scenario
            if mx_vc==k:
                return k
        return mx_vc
        