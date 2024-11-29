class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
                return 1
            elif n%2==0:
                return power(x*x,n//2)
            else:
                return x*power(x*x,(n-1)//2)
        result=power(x,abs(n))
        return 1/result if n<0 else result
        
        