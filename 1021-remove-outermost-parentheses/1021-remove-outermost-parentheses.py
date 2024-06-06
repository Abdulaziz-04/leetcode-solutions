class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=''
        open_count=0
        for i in s:
            if i=='(':
                open_count+=1
                if open_count>1:
                    result+=i
            else:
                open_count-=1
                if open_count>0:
                    result+=i
        return result

        