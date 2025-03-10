class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        if len(word)<5+k:
            return 0
        vowel_set=set(['a','e','i','o','u'])
        
        def atleast_k(k):
            count=defaultdict(int)
            cons=0
            l=0
            result=0
            s=word
            for r in range(len(word)):
                if s[r] not in vowel_set:
                    cons+=1
                elif s[r] in vowel_set:
                    count[s[r]]+=1
                while len(count)==5 and cons>=k:
                    result+=len(word)-r
                    if s[l] not in vowel_set:
                        cons-=1
                    elif s[l] in vowel_set:
                        count[s[l]]-=1
                    if count[s[l]]==0:
                        count.pop(s[l])
                    l+=1
            return result
        return atleast_k(k)-atleast_k(k+1)





        