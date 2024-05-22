class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # 2 pointer approach
        word=list(word)
        l,r=0,len(word)-1
        for r in range(len(word)):
            if word[r]==ch:
                while l<=r:
                    word[l],word[r]=word[r],word[l]
                    l+=1
                    r-=1
                return ''.join(word)
        return ''.join(word)
            
        """
        # Stack approach
        stack=[]
        result=[]
        i=0
        while i < len(word): 
            stack.append(word[i])
            if word[i]==ch:
                while stack:
                    result.append(stack.pop())
                i+=1
                while i < len(word):
                    result.append(word[i])
                    i+=1
                return ''.join(result)
            i+=1
        return word
        """
        