class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree=[0]*n
        for v1,v2 in edges:
            in_degree[v2]+=1
        team=0
        count=0
        for i in range(len(in_degree)):
            if in_degree[i]==0:
                team=i
                count+=1
        return team if count==1 else -1
        