class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Very simple
        # Traverse in reverse
        # If we find a space, keep moving 
        # But also keep count if we don't find a space
        # If we find space again after incrementing the count
        # This means the word has ended and we can return it
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                if c>0:
                    return c
            else:
                c+=1
        return c


        