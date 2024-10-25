class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=set(['+','-','*','/'])
        for token in tokens:
            if token in operations:
                n2=stack.pop()
                n1=stack.pop()
                if token =='+':
                    stack.append(n1+n2)
                elif token=='-':    
                    stack.append(n1-n2)
                elif token=='*':    
                    stack.append(n1*n2)
                elif token=='/':    
                    stack.append(int(float(n1)/n2))
            else:        
                stack.append(int(token))
        return stack[-1]        


        
        