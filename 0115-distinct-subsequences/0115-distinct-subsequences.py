class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        prev=[0]*(m+1)
        prev[0]=1
        for i in range(1,n+1):
            curr=[0]*(m+1)
            for j in range(1,m+1):
                curr[j]=prev[j]
                if s[i-1]==t[j-1]:
                    curr[j]+=prev[j-1]
            prev=curr
        return prev[m]





"""
        memo={}
        def dfs(i,j):
            if j<0:
                return 1
            if i<0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=dfs(i-1,j)
            if s[i]==t[j]:
                memo[(i,j)]+=dfs(i-1,j-1)
            return memo[(i,j)]
        return dfs(n-1,m-1)
"""

        