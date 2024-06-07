class Solution:
    def makeGood(self, s: str) -> str:
        # Basic approach
        stack=[]
        for i in range(len(s)):
            # keep track of previous index using stack
            # If we have a stack i.e. skip the 0th index scenario
            # Add to stack and compare last element with current element
            # Else add to stack
            if (
                stack and
                stack[-1]!=s[i] and
                stack[-1].lower()==s[i].lower()
            ):
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)


            
        