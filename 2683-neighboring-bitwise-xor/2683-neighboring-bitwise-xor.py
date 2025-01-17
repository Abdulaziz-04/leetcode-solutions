class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        xor=0
        for d in derived:
            xor=xor^d
        return xor==0
        