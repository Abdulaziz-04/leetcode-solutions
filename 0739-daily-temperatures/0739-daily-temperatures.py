class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                current_idx,current_t=stack.pop()
                result[current_idx]=i-current_idx
            stack.append((i,t))
        return result
           
        