class DetectSquares:

    def __init__(self):
        self.point_map={}

    def add(self, point: List[int]) -> None:
        self.point_map[tuple(point)]=1+self.point_map.get(tuple(point),0)

    def count(self, point: List[int]) -> int:
        result=0
        px,py=point
        for point in self.point_map.keys():
            x,y=point
            if abs(px-x)!=abs(py-y) or x==px or y==py:
                continue
            result+=self.point_map.get((px,y),0) * self.point_map.get((x,py),0)*self.point_map.get((x,y),0)
        return result
            

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)