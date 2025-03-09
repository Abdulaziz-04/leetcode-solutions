class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k-1):
            colors.append(colors[i])
        result=0
        l=0
        for r in range(1,len(colors)):
            if colors[r]==colors[r-1]:
                l=r
                continue
            if r-l+1==k:
                result+=1
                l+=1
        return result
        