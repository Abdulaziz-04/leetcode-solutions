class Solution:
    def minOperations(self, s: str) -> int:
        flip=0
        ops1=0
        for ch in s:
            if int(ch)!=flip:
                ops1+=1
            flip=int(not flip)
        flip=1
        ops2=0
        for ch in s:
            if int(ch)!=flip:
                ops2+=1
            flip=int(not flip)
        return min(ops1,ops2)
        