class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        # With O(max(s,t)) memory
        s_stack=[]
        t_stack=[]
        for ch in s:
            if ch=='#' :
                s_stack.pop()
            elif s_stack:
                s_stack.append(ch)
        for ch in t:
            if ch=='#':
                t_stack.pop()
            elif t_stack:
                t_stack.append(ch)
        return s_stack==t_stack
        """
        # With O(1) memory
        def getNext(s,i):
            skip=0
            while i>=0:
                if s[i]=='#':
                    skip+=1
                    i-=1
                elif skip>0:
                    skip-=1
                    i-=1
                else:
                    break
            return i
        l,r=len(s)-1,len(t)-1
        while l>=0 and r>=0:
            l=getNext(s,l)
            r=getNext(t,r)
            if l<0 and r<0:
                return True
            elif l<0 and r>=0:
                return False
            elif l>=0 and r<0:
                return False
            elif s[l]!=t[r]:
                return False
            l-=1
            r-=1
        if getNext(s,l)>=0:
            return False
        if getNext(t,r)>=0:
            return False
        return True
        

        
        