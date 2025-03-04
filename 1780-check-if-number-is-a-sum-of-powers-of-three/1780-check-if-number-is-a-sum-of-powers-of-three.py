class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(power,total):
            if total==n:
                return True
            if  total>=n or 3**power>n:
                return False
            if backtrack(power+1,total+3**power):
                return True
            return backtrack(power+1,total)
        return backtrack(0,0)
        