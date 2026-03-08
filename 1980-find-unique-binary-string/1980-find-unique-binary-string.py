class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result=[]
        n=len(nums[0])
        for i in range(n):
            result.append(not int(nums[i][i]))
        return ''.join(list(map(lambda x : str(int(x)),result)))
