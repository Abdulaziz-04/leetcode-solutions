class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def calculateSum(i,k,invert=False):
            c=0
            total=0
            if k<0:
                k=abs(k)
                invert=not invert
            if invert:
                j=i-1
                while c!=k:
                    if j==-1:
                        j=len(code)-1
                    total+=code[j]
                    j-=1
                    c+=1
            else:
                j=i+1
                while c!=k:
                    if j==len(code):
                        j=0
                    total+=code[j]
                    j+=1
                    c+=1
            return total
        result=[]
        for i,c in enumerate(code):
            if c>0:
                result.append(calculateSum(i,k,False))
            elif c<0:
                result.append(calculateSum(i,k,True))
            else:
                result.append(0)
        return result

            

