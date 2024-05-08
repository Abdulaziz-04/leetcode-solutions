class Solution:
    def compress(self, chars: List[str]) -> int:
        # current index
        idx=0
        # To modify input array
        mod_idx=0
        # Loop through all characters
        while idx<len(chars):
            # Keep track of current character
            curr_char=chars[idx]
            # Assign init freq
            freq=1
            # Check for consecutive characters
            while idx+1<len(chars) and curr_char==chars[idx+1]:
                idx+=1
                freq+=1
            # Update array and modification index
            chars[mod_idx]=curr_char
            mod_idx+=1
            # Update frequency information
            if freq>1:
                for f in str(freq):
                    chars[mod_idx]=f
                    mod_idx+=1
            # Move to next character
            idx+=1
        # Return length of modified array
        return mod_idx