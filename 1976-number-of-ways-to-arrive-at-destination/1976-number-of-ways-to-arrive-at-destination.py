class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list=defaultdict(list)
        for u,v,w in roads:
            adj_list[u].append((v,w))
            adj_list[v].append((u,w))
        min_heap=[(0,0)]
        path_cost=[float('inf')]*n
        path_count=[0]*n
        path_count[0]=1
        MOD=10**9+7
        while min_heap:
            curr_cost,curr_node=heapq.heappop(min_heap)
            for nei,nei_cost in adj_list[curr_node]:
                if curr_cost+nei_cost<path_cost[nei]:
                    path_cost[nei]=curr_cost+nei_cost
                    path_count[nei]=path_count[curr_node]
                    heapq.heappush(min_heap,(curr_cost+nei_cost,nei))
                elif curr_cost+nei_cost==path_cost[nei]:
                    path_count[nei]=(path_count[curr_node]+path_count[nei])%MOD
        return path_count[n-1]

        