from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap=defaultdict(list)
        for c,p in prerequisites:
            preMap[c].append(p)
        visited,cycle=set(),set()
        result=[]
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            visited.add(c)
            result.append(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return result

        