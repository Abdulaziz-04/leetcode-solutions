class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq=[0]*26
        for word in words:
            for ch in word:
                freq[ord(ch)-ord('a')]+=1
        for f in freq:
            if f%len(words)!=0:
                return False
        return True

        