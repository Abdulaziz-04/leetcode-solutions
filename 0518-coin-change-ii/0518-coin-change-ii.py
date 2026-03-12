class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n)]
        for a in range(amount+1):
            if a%coins[0]==0:
                dp[0][a]=1
        for i in range(1,n):
            for a in range(amount+1):
                dp[i][a]+=dp[i-1][a]
                if a-coins[i]>=0:
                    dp[i][a]+=dp[i][a-coins[i]]
        return dp[n-1][amount]




"""
        memo={}
        def dfs(i,a):
            if i==0:
                if a==0 or a%coins[i]==0:
                    return 1
                return 0
            memo[(i,a)]=dfs(i-1,a)
            if a-coins[i]>=0:
                memo[(i,a)]+=dfs(i,a-coins[i])
            return memo[(i,a)]
        return dfs(len(coins)-1,amount)
"""
        