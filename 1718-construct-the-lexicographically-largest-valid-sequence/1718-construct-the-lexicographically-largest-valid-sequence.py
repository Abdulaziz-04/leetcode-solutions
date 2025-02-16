class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        curr=[0]*(2*n-1)
        used=set()

        def backtrack(i):
            if i==len(curr):
                return True

            for num in range(n,0,-1):
                if num in used:
                    continue

                if num>1 and ((i+num)>=len(curr) or curr[i+num]>0):
                    continue

                used.add(num)
                curr[i]=num
                if num>1:
                    curr[i+num]=num
                j=i+1
                while j<len(curr)  and curr[j]>0:
                    j+=1

                if backtrack(j):
                    return True

                used.remove(num)
                curr[i]=0
                if num>1:
                    curr[i+num]=0
            return False
        backtrack(0)
        return curr
        

        