class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        beauty=0
        l=0
        total=0
        n_list=list(map(int, str(num)))
        for r in range(len(n_list)):
            if r-l+1>k:
                total-=n_list[l]*(10**(k-1))
                l+=1
            total=total*10+n_list[r]
            if r-l+1==k and total!=0 and num%total==0:
                beauty+=1
        return beauty

        