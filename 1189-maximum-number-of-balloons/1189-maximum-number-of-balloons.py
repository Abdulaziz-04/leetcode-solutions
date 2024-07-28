class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t={
            ch : 0 for ch in ['b','a','l','o','n']
        }
        for ch in text:
            if ch in t:
                t[ch]+=1
        single_letter_min=min(t['b'],t['a'],t['n'])
        double_letter_min=min(t['l'],t['o'])//2
        return min(single_letter_min,double_letter_min)

        