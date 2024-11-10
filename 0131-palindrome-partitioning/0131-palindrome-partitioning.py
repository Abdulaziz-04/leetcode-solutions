class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        part=[]
        def check_pal(s,i,j):
            l,r=i,j
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def dfs(i):
            if i>=len(s):
                result.append(part.copy())
                return 
            for j in range(i,len(s)):
                if check_pal(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return result
            
        