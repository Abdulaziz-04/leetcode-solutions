class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.map={}

        

    def next(self, price: int) -> int:
        result=1
        while self.stack and price>=self.stack[-1]:
            result+=self.map[self.stack.pop()]
        self.map[price]=result
        self.stack.append(price)
        return result
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)