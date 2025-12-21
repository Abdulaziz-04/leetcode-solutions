class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_tuple(s):
            chars=[0]*26
            for ch in s:
                chars[ord(ch)-ord('a')]+=1
            return tuple(chars)
        anagrams=defaultdict(list)
        for s in strs:
            anagrams[get_tuple(s)].append(s)
        result=[]
        for k,v in anagrams.items():
            result.append(v)
        return result
            
            
         