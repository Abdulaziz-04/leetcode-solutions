class Solution:
    def simplifyPath(self, path: str) -> str:
        # Ignore multiple slashes
        # Ignore the '.'
        # pop the stack if we encounter '..' i.e. build the string once we cross the slash
        # As we have to ignore the last slash, let's add it here in the start and deal with the rest
        stack=[]
        cur=''
        for c in path+'/':
            if c=='/':
                if cur=='..':
                    if stack:
                        stack.pop()
                elif cur!='' and cur!='.':
                    stack.append(cur)
                cur=""
            else:
                cur+=c
        return '/'+'/'.join(stack)

        