class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left=Node(-1,-1)
        self.right=Node(-1,-1)
        self.left.next,self.right.prev=self.right,self.left

    def insert(self,node):
        p,n=self.right.prev,self.right
        p.next=node
        n.prev=node
        node.next=n
        node.prev=p

    def remove(self,node):
        p,n=node.prev,node.next
        p.next,n.prev=n,p
        

    def get(self, key: int) -> int:
        if key in self.cache:
            curr_node=self.cache[key]
            self.remove(curr_node)
            self.insert(curr_node)
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)