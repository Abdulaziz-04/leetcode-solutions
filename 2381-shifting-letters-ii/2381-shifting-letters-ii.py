class Solution:
    def shiftingLetters(self,s, shifts):
        n = len(s)
        diff = [0]*(n+1)    
    
        for b, e, d in shifts:
            if d == 1:
                diff[b] += 1
                if e+1 < n:
                    diff[e+1] -= 1
            else:
                diff[b] -= 1
                if e+1 < n:
                    diff[e+1] += 1
    
        for i in range(1, n):
            diff[i] += diff[i-1]  # now diff[i] holds the net shift at index i
    
        arr = list(s)
        for i in range(n):
            # net shift could be positive or negative
            shift_val = diff[i] 
            # shift_val % 26 to wrap within [0..25]
            new_char_ord = (ord(arr[i]) - ord('a') + shift_val) % 26
            arr[i] = chr(new_char_ord + ord('a'))
    
        return ''.join(arr)
    