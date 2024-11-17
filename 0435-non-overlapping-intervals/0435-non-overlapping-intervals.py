class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        total=0
        stack=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<stack[-1][1]:
                total+=1
                stack[-1][1]=min(intervals[i][1],stack[-1][1])
            else:
                stack.append(intervals[i])
        return total

        