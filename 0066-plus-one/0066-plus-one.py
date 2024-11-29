class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        i=len(digits)-1
        result=[]
        while i>=0:
            total=digits[i]+carry
            if total<=9:
                digits[i]=total
                return digits
            else:
                digits[i]=0
            i-=1
        if carry:
            digits.insert(0,1)
        return digits



        