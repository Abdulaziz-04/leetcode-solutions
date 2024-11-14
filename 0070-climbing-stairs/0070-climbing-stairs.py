class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n,cache):
            if n in cache:
                return cache[n]
            if n<=0:
                return 0
            cache[n]=dp(n-1,cache)+dp(n-2,cache)
            return cache[n]
        cache={1:1,2:2}
        return dp(n,cache)

        