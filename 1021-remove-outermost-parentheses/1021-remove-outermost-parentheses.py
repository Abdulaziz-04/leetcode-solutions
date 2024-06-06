class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        st_len=0
        result=''
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            else:
                stack.pop()
            if len(stack)==0:
                result+=s[i-st_len+1:i]
                st_len=0
                continue
            st_len+=1
        return result

        