from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def checkCycle(v,p):
            stack=[(v,p)]
            visited=set()
            while stack:
                curr,parent=stack.pop()
                visited.add(curr)
                for neighbor in adjList[curr]:
                    if neighbor not in visited:
                        stack.append((neighbor,curr))
                    elif neighbor!=parent:
                        return False
            return True
            
        adjList=defaultdict(list)
        for v1,v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
            if not checkCycle(v1,-1):
                return [v1,v2]
        return []
            
    
        