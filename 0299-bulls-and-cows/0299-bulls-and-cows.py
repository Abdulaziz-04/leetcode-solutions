from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        gCount=defaultdict(int)
        sCount=defaultdict(int)
        bulls=0
        cows=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                gCount[guess[i]]+=1
                sCount[secret[i]]+=1
        for s in sCount.keys():
            cows+=min(gCount[s],sCount[s])
        return f"{bulls}A{cows}B"
            

        