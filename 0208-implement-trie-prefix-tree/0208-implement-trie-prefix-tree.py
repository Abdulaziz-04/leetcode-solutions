class Node:
    def __init__(self):
        self.children={}
        self.isEnd=False
class Trie:

    def __init__(self):
        self.node=Node()
        
    def insert(self, word: str) -> None:
        curr=self.node
        for c in word:
            if c not in curr.children:  
                curr.children[c]=Node()
            curr=curr.children[c]
        curr.isEnd=True

    def search(self, word: str) -> bool:
        curr=self.node
        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curr=self.node
        for p in prefix:
            if p not in curr.children:
                return False
            curr=curr.children[p]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)