class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=0
        curr_cost=0
        mx_len=curr_len=0
        for r in range(len(s)):
            cost=abs(ord(s[r])-ord(t[r]))
            if curr_cost <=maxCost:
                curr_cost+=cost
                curr_len+=1
            while curr_cost > maxCost:
                cost=abs(ord(s[l])-ord(t[l]))
                curr_cost-=cost
                curr_len-=1
                l+=1
            mx_len=max(mx_len,curr_len)
        return mx_len
        