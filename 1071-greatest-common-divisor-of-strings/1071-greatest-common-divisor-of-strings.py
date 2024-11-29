class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2=len(str1),len(str2)
        def is_divisible(i):
            if l1%i or l2%i:
                return False
            r1,r2=l1//i,l2//i
            return str1[:i]*r1==str1 and str1[:i]*r2==str2
        for i in range(min(l1,l2),0,-1):
            if is_divisible(i):
                return str1[:i]
        return ""
        