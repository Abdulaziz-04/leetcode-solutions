class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        def backtrack(i,path):
            if i==n:
                result.append(path.copy())
                return
            # take
            path.append(nums[i])
            backtrack(i+1,path)
            # not take
            path.pop()
            backtrack(i+1,path)
            
        backtrack(0,[])
        return result
        