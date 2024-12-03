class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix=0
        mxPrefix=0
        for i in range(len(gain)):
            prefix+=gain[i]
            mxPrefix=max(prefix,mxPrefix)
        return mxPrefix
        