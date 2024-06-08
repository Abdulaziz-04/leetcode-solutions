class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Compare a base string with all the other strings
        # If we reach a length index or if comparison fails return result
        result=''
        for i in range(len(strs[0])):
            for word in strs:
                if i==len(word) or word[i]!=strs[0][i]:
                    return result
            result+=strs[0][i]
        return result
           

        