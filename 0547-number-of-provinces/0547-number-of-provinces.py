from collections import defaultdict
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        components=0
        adjList=defaultdict(list)
        for i,con_data in enumerate(isConnected):
            for j,c in enumerate(con_data):
                if c==1:
                    adjList[i+1].append(j+1)

        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in adjList[node]:
                if n not in visited:
                    dfs(n)
        
        comp=0
        for node in adjList.keys():
            if node not in visited:
                dfs(node)
                comp+=1
        return comp

            

        
            
        