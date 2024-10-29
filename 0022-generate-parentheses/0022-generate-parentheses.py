class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3 conditions for backtrack:
        """
            - if open==close==n, then we reached one combo
            - if open<n then we can add a open and backtrack 
            - if close<open and close<n, then we can add a close and backtrack
        """
        stack=[]
        result=[]
        def backtrack(open_count,close_count):
            if open_count==close_count==n:
                result.append("".join(stack))
                return
            if open_count<n:    
                stack.append("(")
                backtrack(open_count+1,close_count)
                stack.pop()
            if close_count<open_count:
                stack.append(')')
                backtrack(open_count,close_count+1)
                stack.pop()
        backtrack(0,0)        
        return result        
        