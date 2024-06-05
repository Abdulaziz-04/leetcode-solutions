from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        curr_freq=[0 for i in range(26)]
        common_freq=[0 for i in range(26)]
        for c in words[0]:
            curr_freq[ord(c)-97]+=1
            common_freq[ord(c)-97]+=1
        for w in words[1:]:
            curr_freq=[0 for i in range(26)]
            for c in w:
                curr_freq[ord(c)-97]+=1
            for i in range(len(common_freq)):
                common_freq[i]=min(common_freq[i],curr_freq[i])
        result=[]
        for i in range(len(common_freq)):
            for j in range(common_freq[i]):
                result.append(chr(i+97))
        return result
        