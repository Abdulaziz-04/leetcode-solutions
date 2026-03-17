class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        if n % 2 == 0:
            return self.myPow(x*x,n/2)
        else:
            return x * self.myPow(x, n-1)
        """
        power even
        2**8= 2*2*2*2...
        2*2 2*2 2*2 2*2
        4
        4**4
        16**2
        32**1
        f(n//2, x*x)

        2**9
        x*f(n-1,x)
        2 * f(8,2)
        2**8*2
        """