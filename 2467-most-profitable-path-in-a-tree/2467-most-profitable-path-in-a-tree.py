class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjList=defaultdict(list)
        bob_times={}
        for v1,v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        def dfs(src,prev,time):
            if src==0:
                bob_times[src]=time
                return True
            for n in adjList[src]:
                if n==prev:
                    continue
                if dfs(n,src,time+1):
                    bob_times[src]=time
                    return True
            return False
        dfs(bob,-1,0)

        q=deque([(0,-1,0,amount[0])]) # (node,parent,time,net_profit)
        result=-float('inf')
        while q:
            node,parent,time,total=q.popleft()
            for n in adjList[node]:
                if n==parent:
                    continue
                profit=amount[n]
                n_time=time+1
                if n in bob_times:
                    if n_time==bob_times[n]:
                        profit=profit//2
                    elif n_time>bob_times[n]:
                        profit=0
                q.append((n,node,time+1,profit+total))
                if len(adjList[n])==1:
                    result=max(result,total+profit)
        return result
                



        