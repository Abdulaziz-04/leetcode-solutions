class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx_alt=0
        alt=0
        for g in gain:
            alt+=g
            if alt>mx_alt:
                mx_alt=alt
        return mx_alt
        