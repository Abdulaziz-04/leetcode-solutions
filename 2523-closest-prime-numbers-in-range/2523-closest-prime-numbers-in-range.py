class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def getPrimes():
            primes=[]
            is_prime=[True]*(right+1)
            is_prime[0]=is_prime[1]=False
            for i in range(2,int(right**0.5)+1):
                if not is_prime[i]:
                    continue
                for j in range(i+i,right+1,i):
                    is_prime[j]=False
            for i in range(left,right+1):
                if is_prime[i]:
                    primes.append(i)
            return primes
        primes=getPrimes()
        minDist=float('inf')
        result=[-1,-1]
        for i in range(len(primes)-1):
            diff=primes[i+1]-primes[i]
            if minDist<=2:
                break
            if diff<minDist:
                minDist=diff
                result=[primes[i],primes[i+1]]
        return result
        