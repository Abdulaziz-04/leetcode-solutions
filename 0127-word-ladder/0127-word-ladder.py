from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjList=defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                adjList[pattern].append(word)
        q=deque([beginWord]) 
        visited=set([beginWord])
        result=1
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                if curr==endWord:
                    return result
                for j in range(len(curr)):
                    pattern=curr[:j]+"*"+curr[j+1:]
                    for neighbor in adjList[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            result+=1
        return 0

        