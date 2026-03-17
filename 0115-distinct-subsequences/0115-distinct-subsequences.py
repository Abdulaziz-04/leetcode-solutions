class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        memo={}
        def dfs(i,j):
            if j==m:
                return 1
            if i==n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=dfs(i+1,j)
            if s[i]==t[j]:
                memo[(i,j)]+=dfs(i+1,j+1)
            return memo[(i,j)]
        return dfs(0,0)

        