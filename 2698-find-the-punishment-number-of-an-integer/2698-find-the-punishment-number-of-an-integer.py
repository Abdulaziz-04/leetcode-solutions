class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(j,curr,target,given_str):
            if j>=len(given_str) and curr==target:
                return True
            for k in range(j,len(given_str)):
                if partition(k+1,curr+int(given_str[j:k+1]),target,given_str):
                    return True
            return False

        result=0
        for i in range(1,n+1):
            if partition(0,0,i,str(i*i)):
                result+=i*i
        return result

        
        