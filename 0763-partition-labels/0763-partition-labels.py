class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endMap={}
        for i,ch in enumerate(s):
            endMap[ch]=i
        end=0
        size=0
        result=[]
        end=endMap[s[0]]
        for i,ch in enumerate(s):
            if endMap[ch]>end:
                end=endMap[ch]
            size+=1
            if i==end:
                end=0
                result.append(size)
                size=0
        return result

        