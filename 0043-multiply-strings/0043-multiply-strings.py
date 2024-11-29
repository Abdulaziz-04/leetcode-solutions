class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        n1,n2=len(num1),len(num2)
        num1,num2=num1[::-1],num2[::-1]
        result=[0]*(n1+n2)
        for i in range(n1):
            for j in range(n2):
                digit=int(num1[i])*int(num2[j])
                result[i+j]+=digit
                # Get carry
                result[i+j+1]+=(result[i+j]//10)
                # Get remainder
                result[i+j]=result[i+j]%10
        result=result[::-1]
        z_idx=0
        while z_idx<len(result) and result[z_idx]==0:
            z_idx+=1
        return ''.join(map(str,result[z_idx:]))
        