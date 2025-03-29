class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        prime_scores=[]
        for n in nums:
            score=0
            for f in range(2,int(sqrt(n))+1):
                if n%f==0:
                    score+=1
                    while n%f==0:
                        n=n//f
            if n>=2:
                score+=1
            prime_scores.append(score)
        
        # Preprocess the left and right bounds using monotonic stack
        N=len(nums)
        left_bounds=[-1]*N
        right_bounds=[N]*N
        stack=[]
        for i,s in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]]<s:
                idx=stack.pop()
                right_bounds[idx]=i
            if stack:
                left_bounds[i]=stack[-1]
            stack.append(i)

        # Create min heap and calculate subarrays for each max prime_score
        min_heap=[(-n,i) for i,n in enumerate(nums)]
        heapq.heapify(min_heap)
        result=1
        MOD=10**9+7
        while k>0:
            num,idx=heapq.heappop(min_heap)
            num*=-1
            left=idx-left_bounds[idx]
            right=right_bounds[idx]-idx
            ops=min(k,right*left)
            k-=ops
            result=(result*pow(num,ops,MOD))%MOD
        return result

        