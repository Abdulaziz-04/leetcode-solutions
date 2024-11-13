from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=defaultdict(list)
        for c,p in prerequisites:
            preMap[c].append(p)
        visited=set()
        def dfs(c):
            if c in visited:
                return False
            if len(preMap[c])==0:
                return True
            visited.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            preMap[c]=[]
            visited.remove(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            


        