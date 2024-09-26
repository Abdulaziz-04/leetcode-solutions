class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_map=defaultdict(int)
        for rect in rectangles:
            ratio_map[rect[0]/rect[1]]+=1
        result=0
        for v in ratio_map.values():
            result+=(v*(v-1))//2
        return result
        