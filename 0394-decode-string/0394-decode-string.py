class Solution:
    def decodeString(self, s: str) -> str:
        # Keep track of closing bracket
        stack=[]
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                curr_s=''
                while stack[-1]!='[':
                    # maintain order
                    curr_s=stack.pop()+curr_s
                stack.pop()
                num=''
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(int(num)*curr_s)
        return ''.join(stack)
            
        