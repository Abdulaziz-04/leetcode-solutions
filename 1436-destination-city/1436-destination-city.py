class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src_set=set()
        for src,dst in paths:
            src_set.add(src)
        for src,dst in paths:
            if dst not in src_set:
                return dst
        