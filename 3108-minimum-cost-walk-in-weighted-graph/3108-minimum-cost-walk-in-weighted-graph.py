class UF:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x!=y:
            if self.size[x]<self.size[y]:
                self.parent[x]=y
                self.size[y]+=self.size[x]
            else:
                self.parent[y]=x
                self.size[x]+=self.size[y]
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        union_find=UF(n)
        components={}
        for u,v,w in edges:
            union_find.union(u,v)
        for u,v,w in edges:
            root=union_find.find(u)
            if root not in components:
                components[root]=w
            else:
                components[root]&=w
        result=[]
        for s,d in query:
            r1,r2=union_find.find(s),union_find.find(d)
            if r1!=r2:
                result.append(-1)
            else:
                result.append(components[r1])
        return result

        