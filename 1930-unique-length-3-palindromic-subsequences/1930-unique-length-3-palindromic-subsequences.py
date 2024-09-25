from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result=set()
        left=set()
        right=Counter(s)
        for mid in range(len(s)):
            # Decrement from the right as we encounter
            right[s[mid]]-=1
            # If we don't have more characters in right, remove them
            if right[s[mid]]==0:
                right.pop(s[mid])
            for ch in left:
                if ch in right:
                    result.add((s[mid],ch))
            left.add(s[mid])
        return len(result)
        