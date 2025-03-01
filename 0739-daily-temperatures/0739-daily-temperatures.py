class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                curr_idx,temp=stack.pop()
                result[curr_idx]=i-curr_idx
            stack.append((i,t))
        return result
        