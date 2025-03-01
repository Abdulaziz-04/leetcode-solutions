class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_char={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        result=[]
        def dfs(i,curr):
            if len(curr)==len(digits):
                result.append(curr)
                return
            for c in digits_to_char[digits[i]]:
                dfs(i+1,curr+c)
        if digits:
            dfs(0,"")
        return result
        