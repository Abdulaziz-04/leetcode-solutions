class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        for i in range(1,n):
            for j in range(i+1,n):
                n1=num[:i]
                n2=num[i:j]
                if (n1[0]=='0' and len(n1)>1) or (n2[0]=='0' and len(n2)>1):
                    continue
                n1=int(n1)
                n2=int(n2)
                k=j
                while k<n:
                    n3=n1+n2
                    n3=str(n3)
                    if not num.startswith(n3,k):
                        break
                    k+=len(n3)
                    n1,n2=n2,int(n3)
                if k==n:
                    return True
        return False
                

        