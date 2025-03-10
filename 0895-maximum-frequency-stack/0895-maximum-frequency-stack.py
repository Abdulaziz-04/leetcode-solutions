class FreqStack:

    def __init__(self):
        self.count=defaultdict(int)
        self.maxf=0
        self.group=defaultdict(list)
        
    def push(self, val: int) -> None:
        self.count[val]+=1
        if self.count[val]>self.maxf:
            self.maxf+=1
            self.group[self.maxf]=[]
        self.group[self.count[val]].append(val)

    def pop(self) -> int:
        val=self.group[self.maxf].pop()
        self.count[val]-=1
        if len(self.group[self.maxf])==0:
            self.maxf-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()