class Node:
    def __init__(self,key,val,next=None):
        self.key=key
        self.val=val
        self.next=next

class MyHashMap(object):

    def __init__(self):
        self.map=[Node(-1,-1) for i in range(10**4)]

    def hash(self,key):
        return key%100
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        curr=self.map[self.hash(key)]
        while curr.next:
            if curr.next.key==key:
                curr.next.val=value
                return
            curr=curr.next
        curr.next=Node(key,value)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        curr=self.map[self.hash(key)]
        while curr.next:
            if curr.next.key==key:
                return curr.next.val
            curr=curr.next
        return -1
            
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        curr=self.map[self.hash(key)]
        while curr and curr.next:
            if curr.next.key==key:
                curr.next=curr.next.next
            curr=curr.next
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)