class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        r,d=[],[]
        # Keep track of indices in 2 different queues
        for i in range(len(senate)):
            if senate[i]=='R':
                r.append(i)
            else:
                d.append(i)

        # while both queues exist, add the winner to end of the queue and pop the others
        while(r and d):
            if r[0]<d[0]:
                r.append(n)
            else:
                d.append(n)
            n+=1
            r.pop(0)
            d.pop(0)
            
        # Return the winner
        return 'Radiant' if len(r)>0 else 'Dire'


        
        