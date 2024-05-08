class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        idx=0
        mod_idx=0
        while idx<len(chars):
            curr_char=chars[idx]
            freq=1
            while idx+1<len(chars) and curr_char==chars[idx+1]:
                idx+=1
                freq+=1
            chars[mod_idx]=curr_char
            mod_idx+=1
            if freq>1:
                for f in str(freq):
                    chars[mod_idx]=f
                    mod_idx+=1
            idx+=1
        return mod_idx