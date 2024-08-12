class Node:
    def __init__(self,key=-1,value=-1,next=None):
        self.key=key
        self.val=value
        self.next=next

class MyHashMap:

    def __init__(self):
        self.hmap=[Node() for i in range(1000)]

    def hash(self,key):
        return key%len(self.hmap)

    def put(self, key: int, value: int) -> None:
        idx=self.hash(key)
        cur=self.hmap[idx]
        # We need to make sure we reach the end node and not end up at NULL
        while cur.next:
            if cur.next.key==key:
                cur.next.val=value
                return 
            cur=cur.next
        cur.next=Node(key,value)
        

    def get(self, key: int) -> int:
        idx=self.hash(key)
        cur=self.hmap[idx]
        while cur:
            if cur.key==key:
                return cur.val
            cur=cur.next
        return -1
        
    def remove(self, key: int) -> None:
        idx=self.hash(key)
        cur=self.hmap[idx]
        while cur and cur.next:
            if cur.next.key==key:
                cur.next=cur.next.next
            cur=cur.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)