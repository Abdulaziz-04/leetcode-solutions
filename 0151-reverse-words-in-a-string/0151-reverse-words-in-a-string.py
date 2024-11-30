class Solution:
    def reverseWords(self, s: str) -> str:
        # List of words
        result=[]

        # Index tracker
        i=0

        # Keep track of current word
        curr=""

        # Skip leading spaces
        while s[i]==' ':
            i+=1

        # Loop till end of string
        while i<len(s):
            # If space found
            if s[i]==' ':
                i+=1

                # append current word
                result.append(curr)

                # Clear it, to store the new word
                curr=""

                # Skip more than 1 spaces
                while i<len(s) and s[i]==' ':
                    i+=1
            else:
                # Just append the letter to string
                curr+=s[i]
                i+=1
                
        # Append last word after loop termination
        if curr:
            result.append(curr)

        # We want reverse order, reversing the words
        return ' '.join(result[::-1])
        