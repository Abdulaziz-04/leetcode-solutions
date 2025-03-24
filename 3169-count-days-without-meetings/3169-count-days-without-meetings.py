class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        prev_end=0
        for s,e in meetings:
            s=max(prev_end+1,s)
            days-=max(e-s+1,0)
            prev_end=max(prev_end,e)
        return days


        