class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        for ch in s:
            stack.append(ch)
            part_found=True
            if len(stack)>=len(part):
                k=1
                for i in range(len(part)-1,-1,-1):
                    if part[i]!=stack[-k]:
                        part_found=False
                        break
                    k+=1
                if part_found:
                    for i in range(len(part)-1,-1,-1):
                        stack.pop()
        return "".join(stack)
        