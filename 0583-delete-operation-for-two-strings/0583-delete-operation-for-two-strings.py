class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)
        memo={}
        def dfs(i,j):
            if i==0 or j==0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i]==word2[j]:
                memo[(i,j)]=1+dfs(i-1,j-1)
            else:
                memo[(i,j)]=max(dfs(i-1,j),dfs(i,j-1))
            return memo[(i,j)]
            
        return n+m-2*dfs(n-1,m-1)