class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s)%2==1:
            return False

        lock_stack=[]
        unlock_stack=[]
        for i in range(len(s)):
            if locked[i]=='0':
                unlock_stack.append(i)
            elif s[i]=='(':
                lock_stack.append(i)
            else:
                if lock_stack:
                    lock_stack.pop()
                elif unlock_stack:
                    unlock_stack.pop()
                else:
                    return False

        while lock_stack and unlock_stack and lock_stack[-1]<unlock_stack[-1]:
            lock_stack.pop()
            unlock_stack.pop()
        if lock_stack:
            return False
        return True
                

        