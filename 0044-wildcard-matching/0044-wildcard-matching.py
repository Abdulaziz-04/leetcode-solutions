class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m=len(s),len(p)
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i<0 and j<0:
                return True
            if i>=0 and j<0:
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
            
        