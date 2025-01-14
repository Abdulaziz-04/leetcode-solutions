class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result=[]
        count=0
        a_set=set()
        b_set=set()
        for i in range(len(A)):
            a_set.add(A[i])
            b_set.add(B[i])
            if A[i]==B[i] and (A[i] in b_set or B[i] in a_set):
                count+=1
            else:
                if A[i] in b_set:
                    count+=1
                if B[i] in a_set:
                    count+=1
            result.append(count)
        return result
        