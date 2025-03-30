class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result=[]
        interval_map={}
        for i,ch in enumerate(s):
            interval_map[ch]=i
        end,size=0,0
        for i,ch in enumerate(s):
            size+=1
            end=max(interval_map[ch],end)
            if i==end:
                result.append(size)
                size=0
        return result


        