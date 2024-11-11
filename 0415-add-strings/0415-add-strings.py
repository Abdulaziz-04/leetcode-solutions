class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]
        n1=len(num1)
        n2=len(num2)
        mlen=max(n1,n2)
        i=0
        carry=0
        result=""
        while i<mlen:
            if i<n1:
                c1=int(num1[i])
            else:
                c1=0
            if i<n2:
                c2=int(num2[i])
            else:
                c2=0
            total=c1+c2+carry
            carry=total//10
            result+=str(total%10)
            i+=1
        if carry:
            result+=str(carry)
        return result[::-1]
        



            

        