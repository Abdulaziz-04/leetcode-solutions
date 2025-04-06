from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hmap=set()
        left=set()
        right=Counter(s)
        for i in range(len(s)):
            right[s[i]]-=1
            if right[s[i]]==0:
                right.pop(s[i])
            for j in range(26):
                ch=chr(ord('a')+j)
                if ch in left and ch in right:
                    hmap.add((s[i],ch))
            left.add(s[i])
        return len(hmap)
        