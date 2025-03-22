class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n):
            visited=set()
            stack=[n]
            while stack:
                curr=stack.pop()
                visited.add(curr)
                for nei in adjList[curr]:
                    if nei not in visited:
                        stack.append(nei)
            return visited
        
        visit=set()
        adjList=defaultdict(list)
        components={}
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        result=0
        for node in range(n):
            if node in visit:
                continue
            components=dfs(node)
            flag=True
            for v in components:
                visit.add(v)
                if len(components)-1!=len(adjList[v]):
                    flag=False
                    break
            if flag:
                result+=1
        return result
            

        
    
        
        
        
        