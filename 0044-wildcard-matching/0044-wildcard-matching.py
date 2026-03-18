class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m=len(s),len(p)
        dp=[[False]*(m+1) for i in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            dp[i][0]=False
        for j in range(1,m+1):
            flag=True
            for k in range(1,j+1):
                if p[k-1]!='*':
                    flag=False
                    break
            dp[0][j]=flag
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
        return dp[n][m]


        """
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i<0 and j<0:
                return True
            if i>0 and j<0:
                return False
            if i<0:
                for k in range(j,-1,-1):
                    if p[k]!='*':
                        return False
                return True
            memo[(i,j)]=False
            if s[i]==p[j] or p[j]=='?':
                memo[(i,j)]=dfs(i-1,j-1)
            if p[j]=='*':
                memo[(i,j)]=dfs(i-1,j) or dfs(i,j-1)
            return memo[(i,j)]

        return dfs(n-1,m-1)
        """
            
        