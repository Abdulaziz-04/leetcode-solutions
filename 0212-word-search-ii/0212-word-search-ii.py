class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False

    def addWord(self,word):
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.isEnd=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)

        R,C=len(board),len(board[0])
        visited=set()
        result=set()
        def dfs(r,c,node,word):
            if r<0 or c<0 or r==R or c==C or board[r][c] not in node.children or (r,c) in visited:
                return
            visited.add((r,c))
            
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isEnd:
                result.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))
        for r in range(R):
            for c in range(C):
                dfs(r,c,root,"")
        return list(result)
            
            
        