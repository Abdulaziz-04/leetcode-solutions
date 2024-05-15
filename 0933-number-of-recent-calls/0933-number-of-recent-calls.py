class RecentCounter:

    def __init__(self):
        self.RANGE=3000
        self.call_counter=[]
        

    def ping(self, t: int) -> int:
        calls=0
        self.call_counter.append(t)
        l_range=t-self.RANGE
        r_range=t
        for c in self.call_counter:
            if c>=l_range and c<=r_range:
                calls+=1
        return calls




        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)