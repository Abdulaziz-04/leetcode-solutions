class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix=[]
        vowels=set(['a','e','i','o','u'])
        total=0
        for w in words:
            if w[0] in vowels and w[-1] in vowels: 
                total+=1
            prefix.append(total)
        print(prefix)
        result=[]
        for l,r in queries:
            if l==0:
                result.append(prefix[r])
            else:
                result.append(prefix[r]-prefix[l-1])
        return result

        