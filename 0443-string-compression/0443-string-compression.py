class Solution:
    def compress(self, chars: List[str]) -> int:
        r=0
        i=0
        while i <len(chars):
            group=1
            while i+group<len(chars) and chars[i+group]==chars[i]:
                group+=1
            chars[r]=chars[i]
            r+=1
            if group>1:
                str_group=str(group)
                chars[r:r+len(str_group)]=list(str_group)
                r+=len(str_group)
            i+=group
        return r
        