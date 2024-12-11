class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adjList=defaultdict(list)
        for i in range(len(equations)):
            n1,n2=equations[i]
            v=values[i]
            adjList[n1].append((n2,v))
            adjList[n2].append((n1,1/v))

        def bfs(q1,q2):
            visited=set()
            if q1 not in adjList or q2 not in adjList:
                return -1
            q=deque()
            q.append([q1,1])
            while q:
                curr,val=q.popleft()
                visited.add(curr)
                for n in adjList[curr]:
                    if q2==n[0]:
                        return val*n[1]
                    if n[0] not in visited:
                        q.append([n[0],val*n[1]])
                    
            return -1


        
        result=[bfs(q1,q2) for q1,q2 in queries]
        return result

        