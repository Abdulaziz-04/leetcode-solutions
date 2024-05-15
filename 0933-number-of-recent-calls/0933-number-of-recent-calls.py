from collections import deque
class RecentCounter:

    def __init__(self):
        self.RANGE=3000
        self.q=deque()
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0]<t-self.RANGE:
            self.q.popleft()
        return len(self.q)




        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)