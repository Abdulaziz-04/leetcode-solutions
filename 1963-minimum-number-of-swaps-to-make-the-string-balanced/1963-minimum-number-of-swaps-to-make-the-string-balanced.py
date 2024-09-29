class Solution:
    def minSwaps(self, s: str) -> int:
        max_bracs=0
        close_bracs=0
        for brac in s:
            if brac==']':
                close_bracs+=1
            else:
                close_bracs-=1
            max_bracs=max(max_bracs,close_bracs)
        return (max_bracs+1)//2

        