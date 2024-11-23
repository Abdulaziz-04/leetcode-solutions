class Solution:
    def isValid(self, s: str) -> bool:
        par_map={")":"(","}":"{","]":"["}
        if len(s)==1:
            return False
        stack=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)
            elif stack and stack[-1]==par_map[ch]:
                stack.pop()
            else:
                return False
        return len(stack)==0
        