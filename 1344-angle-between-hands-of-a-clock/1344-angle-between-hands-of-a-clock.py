class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mins=minutes*6
        hours=(hour%12)*30 + minutes*0.5
        diff=abs(hours-mins)
        return min(diff,360-diff)
        
        