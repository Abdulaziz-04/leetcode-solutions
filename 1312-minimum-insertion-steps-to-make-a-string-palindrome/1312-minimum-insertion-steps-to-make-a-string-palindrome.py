class Solution:
    def minInsertions(self, s: str) -> int:
        memo={}
        n=len(s)
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            if s[l]==s[r]:
                memo[(l,r)]=dfs(l+1,r-1)
            else:
                memo[(l,r)]=1+min(dfs(l,r-1),dfs(l+1,r))
            return memo[(l,r)]

        return dfs(0,n-1)
        