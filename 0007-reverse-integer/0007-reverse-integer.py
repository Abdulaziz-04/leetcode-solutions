class Solution:
    def reverse(self, x: int) -> int:
        t=abs(x)
        result=0
        while t!=0:
            digit=t%10
            t=t//10
            result=result*10+digit
        if result<-2**31 or result>2**31-1:
            return 0
        if x<0:
            return -1*result
        else:
            return result
        