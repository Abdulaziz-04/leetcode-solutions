class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(oc,cc,curr):
            if oc==n and cc==n:
                result.append(''.join(curr.copy()))
                return
            if cc>oc or oc>n or cc>n:
                return
            curr.append('(')
            backtrack(oc+1,cc,curr)
            curr.pop()
            curr.append(')')
            backtrack(oc,cc+1,curr)
            curr.pop()
        backtrack(0,0,[])
        return result
        